import serial
import time
from gpiozero import DigitalOutputDevice, DigitalInputDevice

# --- Configuration ---
SERIAL_PORT = "/dev/ttyAMA0" 
BAUD_RATE = 9600

# GPIO Pins (BCM Numbering)
M0_PIN = 23
M1_PIN = 24
AUX_PIN = 18

def run_test():
    # Initialize GPIOs using gpiozero
    # M0 and M1 are outputs. initial_value=False sets them to LOW (0)
    m0 = DigitalOutputDevice(M0_PIN, initial_value=False)
    m1 = DigitalOutputDevice(M1_PIN, initial_value=False)
    
    # AUX is an input
    aux = DigitalInputDevice(AUX_PIN)

    print("--- E220 LoRa Test (Pi 5 / RP1 Compatible) ---")
    print(f"Mode: Normal (M0=0, M1=0) | Pins: M0=G{M0_PIN}, M1=G{M1_PIN}, AUX=G{AUX_PIN}")

    try:
        # Initialize Serial
        ser = serial.Serial(
            port=SERIAL_PORT,
            baudrate=BAUD_RATE,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1
        )

        counter = 0
        while True:
            # 1. Wait for AUX to be High (Module is idle)
            # In gpiozero, .value is 1 for High, 0 for Low
            while aux.value == 0:
                time.sleep(0.01)
            
            # 2. Send the message
            message = f"Pi5 LoRa Message #{counter}\r\n"
            ser.write(message.encode('utf-8'))
            
            print(f"Sent: {message.strip()}")
            
            # 3. Wait for AUX to clear again (Transmission finished)
            while aux.value == 0:
                time.sleep(0.01)
            
            counter += 1
            time.sleep(5)

    except serial.SerialException as e:
        print(f"Serial Error: {e}")
    except KeyboardInterrupt:
        print("\nStopping script...")
    finally:
        ser.close()
        # gpiozero handles cleanup automatically when the script exits
        print("Serial closed and GPIO released.")

if __name__ == "__main__":
    run_test()