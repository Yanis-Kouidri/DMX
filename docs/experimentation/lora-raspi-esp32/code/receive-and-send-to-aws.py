import asyncio
import serial
import time
import json
import math
import paho.mqtt.client as mqtt
from gpiozero import DigitalOutputDevice
from datetime import datetime

# ==========================================
# CONFIGURATION AWS IOT CORE
# ==========================================
AWS_IOT_ENDPOINT = "a13loltpsesfzp-ats.iot.eu-west-1.amazonaws.com"
MQTT_PORT = 8883
MQTT_TOPIC = "aquacheck/pub"
CLIENT_ID = "Pi5LoRaGatewayClient"

CA_CERT_PATH = "AmazonRootCA1.pem"
DEVICE_CERT_PATH = "device_cert.crt"
PRIVATE_KEY_PATH = "private_key.key"

# Configuration matérielle LoRa (Mode NORMAL : M0=0, M1=0)
m0 = DigitalOutputDevice(23, initial_value=False)
m1 = DigitalOutputDevice(24, initial_value=False)
BAUD_RATE = 9600

# Global MQTT Client
mqtt_client = None

# ==========================================
# FONCTIONS DE CALCULS DÉRIVÉS ET TEMPS
# ==========================================

def get_current_iso_timestamp():
    """
    Génère un timestamp au format ISO 8601 avec le fuseau horaire local 
    au moment exact de la réception (ex: 2026-06-02T15:45:00+0200).
    """
    return datetime.now().astimezone().strftime("%Y-%m-%dT%H:%M:%S%z")

def calculate_humidex(temperature, humidity):
    """
    Calcule l'humidex selon les formules du firmware C++
    """
    try:
        dew_point = temperature - ((100.0 - humidity) / 5.0)
        e = 6.11 * math.exp(5417.7530 * ((1.0 / 273.16) - (1.0 / (273.15 + dew_point))))
        humidex = temperature + 0.5555 * (e - 10.0)
        return round(humidex, 2)
    except Exception:
        return "NAN"

# ==========================================
# TRAITEMENT ET ENVOI DES DONNÉES
# ==========================================

def process_and_send_to_aws(decoded_msg):
    """
    Découpe la chaîne CSV reçue par LoRa, génère le timestamp de réception,
    calcule l'humidex et l'envoie à AWS IoT Core.
    """
    global mqtt_client
    if not mqtt_client or not mqtt_client.is_connected():
        print("[AWS] Erreur : Non connecté à AWS IoT Core. Message ignoré.")
        return

    try:
        # Nettoyage et découpage de la chaîne de caractères
        fields = decoded_msg.strip().split(';')
        
        if len(fields) < 5:
            print(f"[PARSE] Message incomplet (au moins 5 champs requis) : {decoded_msg}")
            return

        # Extraction des données utiles envoyées par le boîtier
        boitier_id = fields[0]
        temperature_raw = fields[1]
        humidity_raw = fields[2]
        soil_moisture_raw = fields[3]
        battery_raw = fields[4]

        # MODIFICATION : Génération du timestamp système au moment précis de la réception
        timestamp_reception = get_current_iso_timestamp()

        # Conversions numériques pour le calcul de l'humidex
        try:
            temp_f = float(temperature_raw)
            humi_f = float(humidity_raw)
            humidex_str = str(calculate_humidex(temp_f, humi_f))
        except ValueError:
            humidex_str = "NAN"

        # Reconstitution de la payload JSON attendue par AWS avec le nouveau timestamp
        payload_dict = {
            "timestamp": timestamp_reception,
            "ID": str(boitier_id),
            "type": "AquaCheck",
            "soilMoisture (%)": str(soil_moisture_raw),
            "temperature": str(temperature_raw),
            "humidity": str(humidity_raw),
            "humidex": humidex_str,
            "batteryLevel": str(battery_raw)
        }

        json_payload = json.dumps(payload_dict)
        print(f"[AWS] Envoi du payload vers le topic '{MQTT_TOPIC}'...")
        
        # Publication vers AWS (QoS 1)
        mqtt_client.publish(MQTT_TOPIC, json_payload, qos=1)

    except Exception as e:
        print(f"[AWS] Erreur lors du traitement du message : {e}")

# ==========================================
# CALLBACKS MQTT
# ==========================================

def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("[AWS] Connecté avec succès à AWS IoT Core !")
    else:
        print(f"[AWS] Échec de la connexion, code d'erreur : {rc}")

def on_publish(client, userdata, mid, reason_code=None, properties=None):
    print(f"[AWS] Message MQTT livré avec succès (mid: {mid})")

# ==========================================
# INITIALISATION MQTT
# ==========================================

def init_mqtt():
    global mqtt_client
    print("[AWS] Initialisation du client MQTT...")
    
    try:
        mqtt_client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2, client_id=CLIENT_ID)
    except AttributeError:
        mqtt_client = mqtt.Client(client_id=CLIENT_ID)

    mqtt_client.on_connect = on_connect
    mqtt_client.on_publish = on_publish

    # Configuration des certificats de sécurité TLS (mTLS)
    mqtt_client.tls_set(
        ca_certs=CA_CERT_PATH,
        certfile=DEVICE_CERT_PATH,
        keyfile=PRIVATE_KEY_PATH,
        tls_version=mqtt.ssl.PROTOCOL_TLSv1_2
    )

    print(f"[AWS] Connexion à l'endpoint {AWS_IOT_ENDPOINT}...")
    mqtt_client.connect(AWS_IOT_ENDPOINT, MQTT_PORT, keepalive=60)
    mqtt_client.loop_start()

# ==========================================
# BOUCLE PRINCIPALE LORA
# ==========================================

def run_lora_receiver():
    print("--- Pi 5 LoRa Receiver & AWS IoT Gateway Operational ---")
    
    # Connexion à AWS au démarrage
    init_mqtt()
    
    try:
        # Ouverture du port série du LoRa E220
        ser = serial.Serial("/dev/ttyAMA0", BAUD_RATE, timeout=1)
        
        while True:
            # Attend la fin de ligne (\n) envoyée par le LoRa émetteur
            header_data = ser.read_until(b'\n')
            
            if header_data:
                # Lecture immédiate de l'octet de signal RSSI arrivant juste après le \n
                rssi_byte = ser.read(1)
                
                if rssi_byte:
                    rssi_raw = rssi_byte[0]
                    # Calcul de la puissance en dBm spécifique au module E220
                    if rssi_raw == 0:
                        rssi_dbm = "No Data"
                    else:
                        rssi_dbm = -(256 - rssi_raw)
                    
                    try:
                        # Décodage et nettoyage de la chaîne brute du message
                        decoded_msg = header_data.decode('utf-8', errors='replace').strip()
                        
                        # Affichage et log local (Telegram)
                        log_message = f"[{time.strftime('%H:%M:%S')}] Message: {decoded_msg: <25} | Signal: {rssi_dbm} dBm"
                        print(log_message)
                        
                        # Traitement et envoi de la charge utile vers AWS avec le nouveau timestamp
                        process_and_send_to_aws(decoded_msg)
                        
                    except Exception as e:
                        print(f"Erreur décodage: {header_data.hex().upper()} | RSSI: {rssi_dbm} dBm | Erreur: {e}")
                
    except KeyboardInterrupt:
        print("\nArrêt de la passerelle...")
    finally:
        if 'ser' in locals() and ser.is_open:
            ser.close()
        if mqtt_client:
            mqtt_client.loop_stop()
            mqtt_client.disconnect()

if __name__ == "__main__":
    run_lora_receiver()