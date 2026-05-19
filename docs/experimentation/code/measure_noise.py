import serial
import time
import asyncio
from gpiozero import DigitalOutputDevice, DigitalInputDevice
from telegram_forward import send_telegram_message

# --- Pin Configuration (Matches your other scripts) ---
SERIAL_PORT = "/dev/ttyAMA0"
BAUD_RATE = 9600
M0_PIN = 23
M1_PIN = 24
AUX_PIN = 18

def measure_rssi_noise():
    print("--- Ambient Noise Diagnosis (RSSI Noise) ---")
    
    # Mode configuration (Normal Mode: M0=0, M1=0)
    # Using 'with' to ensure GPIOs are properly released at the end
    try:
        with DigitalOutputDevice(M0_PIN, initial_value=False) as m0, \
             DigitalOutputDevice(M1_PIN, initial_value=False) as m1, \
             DigitalInputDevice(AUX_PIN) as aux, \
             serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1) as ser:

            print("Normal Mode activated. Waiting for module...")
            time.sleep(0.5) # Stabilization time

            # Command to read RSSI Noise according to manual (Page 15)
            # Format: C0 C1 C2 C3 + Starting address + Length
            # 00H corresponds to "Current environmental noise RSSI"
            read_noise_cmd = bytes([0xC0, 0xC1, 0xC2, 0xC3, 0x00, 0x01])

            while True:
                # 1. Wait until the module is ready
                while aux.value == 0:
                    time.sleep(0.01)

                # 2. Send the read request
                ser.write(read_noise_cmd)
                ser.flush()

                # 3. Read the response (Manual says: C1 + Address + Length + Value)
                # Expecting 4 bytes in return
                response = ser.read(4)

                if len(response) == 4 and response[0] == 0xC1:
                    rssi_raw = response[3]
                    # Calculation: -(256 - RSSI_raw)
                    rssi_dbm = -(256 - rssi_raw)
                    
                    message = f"[{time.strftime('%H:%M:%S')}] Ambient noise (Noise Floor): {rssi_dbm} dBm"
                    print(message)
                    asyncio.run(send_telegram_message(message))
                else:
                    # If other data arrives (like messages from a sender), it will be caught here
                    print(f"Read error or no response: {response.hex().upper()}")

                time.sleep(2) # Measure every 2 seconds

    except serial.SerialException as e:
        print(f"\n[Serial Error] {e}")
    except KeyboardInterrupt:
        print("\nStopping diagnostic.")

if __name__ == "__main__":
    measure_rssi_noise()