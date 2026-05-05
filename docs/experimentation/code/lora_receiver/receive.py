import serial
import time
from gpiozero import DigitalOutputDevice

# Configuration des pins pour le mode NORMAL (M0=0, M1=0)
m0 = DigitalOutputDevice(23, initial_value=False)
m1 = DigitalOutputDevice(24, initial_value=False)

def run_lora_receiver():
    print("--- Récepteur Pi 5 LoRa opérationnel (RSSI Activé) ---")
    
    try:
        # Ouverture du port série avec un timeout pour ne pas bloquer indéfiniment
        ser = serial.Serial("/dev/ttyAMA0", 9600, timeout=1)
        
        while True:
            # On utilise read_until pour attendre la fin de la ligne (\n)
            # Cette fonction est bloquante jusqu'au timeout ou la réception du caractère
            header_data = ser.read_until(b'\n')
            
            if header_data:
                # Si on a reçu quelque chose, l'octet RSSI arrive juste APRÈS le \n
                # On attend un tout petit peu ou on vérifie la disponibilité
                rssi_byte = ser.read(1)
                
                if rssi_byte:
                    rssi_raw = rssi_byte[0]
                    # Calcul RSSI pour E220 : -(256 - valeur)
                    rssi_dbm = -(256 - rssi_raw)
                    
                    try:
                        # Décodage du message (on enlève \r\n avec strip)
                        decoded_msg = header_data.decode('utf-8', errors='replace').strip()
                        
                        print(f"[{time.strftime('%H:%M:%S')}] "
                              f"Message: {decoded_msg: <25} | "
                              f"Signal: {rssi_dbm} dBm")
                    except Exception as e:
                        print(f"Erreur décodage : {header_data.hex().upper()} | RSSI: {rssi_dbm} dBm")
                
            # Pas besoin de sleep(0.05) ici car read_until est bloquant (plus efficace CPU)

    except KeyboardInterrupt:
        print("\nArrêt du script...")
    finally:
        if 'ser' in locals() and ser.is_open:
            ser.close()

if __name__ == "__main__":
    run_lora_receiver()