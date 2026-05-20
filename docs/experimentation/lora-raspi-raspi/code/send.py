import serial
import time
from gpiozero import DigitalOutputDevice, DigitalInputDevice
from signal import pause

# --- Configuration ---
SERIAL_PORT = "/dev/ttyAMA0" 
BAUD_RATE = 9600

# GPIO Pins (BCM Numbering)
M0_PIN = 23
M1_PIN = 24
AUX_PIN = 18

def run_test():
    print("--- E220 LoRa Test (Pi 5 / RP1 Compatible) ---")
    print(f"Mode: Normal (M0=0, M1=0) | Pins: M0=G{M0_PIN}, M1=G{M1_PIN}, AUX=G{AUX_PIN}")

    # Using 'with' to ensure proper closure even in the event of a Ctrl+C
    try:
        with DigitalOutputDevice(M0_PIN, initial_value=False) as m0, \
             DigitalOutputDevice(M1_PIN, initial_value=False) as m1, \
             DigitalInputDevice(AUX_PIN) as aux, \
             serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1) as ser:

            counter = 0
            while True:
                # 1. Wait until AUX is 1 (Module ready)
                # Use a small pause to avoid saturating the CPU
                while aux.value == 0:
                    time.sleep(0.01)
                
                # 2. Sending the message
                message = f"Pi5 LoRa Message #{counter}\r\n"
                ser.write(message.encode('utf-8'))
                ser.flush()  # Ensure data is actually sent over the wire
                
                print(f"Sent: {message.strip()}")
                
                # 3. Wait for the end of transmission (AUX returns to 1)
                # First, wait briefly for the module to drop to 0 (start of transmission)
                time.sleep(0.02) 
                while aux.value == 0:
                    time.sleep(0.01)
                
                counter += 1
                time.sleep(5)

    except serial.SerialException as e:
        print(f"\n[Serial Error] {e}")
    except KeyboardInterrupt:
        print("\n[Stopping] Stop requested by user...")
    finally:
        # With 'with' statements, .close() methods are called automatically here
        print("Resources successfully released.")

if __name__ == "__main__":
    run_test()