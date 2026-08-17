# Reset factory for E220 LoRa module

import serial
import time
from gpiozero import DigitalOutputDevice

# Configuration des pins pour le Pi 5
M0_PIN = 23
M1_PIN = 24

# Forcer le mode CONFIGURATION (M0=1, M1=1)
m0 = DigitalOutputDevice(M0_PIN, initial_value=True)
m1 = DigitalOutputDevice(M1_PIN, initial_value=True)

time.sleep(0.5) # Laisser le temps au module de changer de mode

try:
    ser = serial.Serial("/dev/ttyAMA0", 9600, timeout=1)
    
    # Commande de réinitialisation d'usine pour E220
    # C0 00 00 ... est la structure habituelle. 
    # Pour remettre à zéro : on envoie les paramètres par défaut
    # Voici la trame standard (Adresse 0, 9600bps, 2.4kbps, RSSI OFF)
    reset_cmd = bytes([0xC0, 0x00, 0x08, 0x00, 0x00, 0x62, 0x00, 0x12, 0x03, 0x00, 0x00])
    
    print("Envoi de la configuration par défaut...")
    ser.write(reset_cmd)
    
    time.sleep(0.2)
    response = ser.read(ser.in_waiting)
    
    if response:
        print(f"Réponse du module (Hex): {response.hex().upper()}")
        print("Réinitialisation réussie !")
    else:
        print("Aucune réponse. Vérifiez les branchements M0/M1.")

except Exception as e:
    print(f"Erreur : {e}")
finally:
    ser.close()