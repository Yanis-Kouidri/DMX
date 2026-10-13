import serial
import time
from gpiozero import DigitalOutputDevice

m0 = DigitalOutputDevice(23, initial_value=True)
m1 = DigitalOutputDevice(24, initial_value=True)

def configure():
    print("Mode Config activé. Attente de stabilisation...")
    time.sleep(1.5) # On est généreux sur le temps
    
    try:
        ser = serial.Serial("/dev/ttyAMA0", 9600, timeout=2)
        ser.flushInput() # On vide tout ce qui traîne
        
        command_instruction = bytes([0xc0]) #write
        starting_address = bytes([0x00])
        cmd_length = bytes([0x08])

        
        # Config parameters
        module_address = bytes([0x00, 0x00]) # ADDH + ADDL
        reg0 = bytes([0b011_00_010]) #001 => UART Rate 9600 (default) ; 00 => Serial parity bit 8N1 (default) ; 010 => Air Data Rate 2.4k bps (default)
        reg1 = bytes([0b00_1_000_00]) #00 => Sub-packet setting 200 bytes (default) ; 1 enable RSSI ; 000 => reserved ; 00 => Transmiting power 30dBm (default)
        reg2 = bytes([0x12]) # Channel 18
        reg3 = bytes([0b1_0_0_0_0_000]) # 1 => enable rssi 0 => transmission method ; 0 = Reserved ; 0 = LBT disable ; 0 = reserved ; 000 WOR cycle
        crypt = bytes([0x00, 0x00])

        cmd = command_instruction + starting_address + cmd_length + module_address + reg0 + reg1 + reg2 + reg3 + crypt
        
        print(f"Envoi config: {cmd.hex().upper()}")
        ser.write(cmd)
        
        # On attend la réponse byte par byte pour ne rien rater
        start_time = time.time()
        response = b""
        while (time.time() - start_time) < 2.0:
            if ser.in_waiting > 0:
                char = ser.read(1)
                response += char
                if char == b'\xC1': # On a trouvé le début !
                    response = char + ser.read(10) # On lit le reste (header + 8 octets)
                    break

        if response and response[0] == 0xC1:
            print(f"SUCCÈS ! Réponse complète : {response.hex().upper()}")
            # Vérification du bit RSSI dans la réponse (octet index 7)
            if response[7] & 0x40:
                print("Le bit RSSI est bien activé dans le module.")
        else:
            print(f"Échec. Réponse reçue incomplète : {response.hex().upper()}")

    finally:
        ser.close()

if __name__ == "__main__":
    configure()