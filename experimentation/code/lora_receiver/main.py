import serial
import time
from gpiozero import DigitalOutputDevice, DigitalInputDevice

# Explicit BCM Configuration
M0_PIN = 23 # Physical 16
M1_PIN = 24 # Physical 18
AUX_PIN = 18 # Physical 12

# Use the direct hardware UART address for Pi 5
UART_PORT = "/dev/ttyAMA0" 
BAUD_RATE = 9600

def run_diagnostic_receiver():
    print("--- Pi 5 LoRa Diagnostic Receiver ---")
    
    # Initialize Pins
    m0 = DigitalOutputDevice(M0_PIN, initial_value=False)
    m1 = DigitalOutputDevice(M1_PIN, initial_value=False)
    aux = DigitalInputDevice(AUX_PIN)

    # Double check state
    print(f"Pins Set: M0(BCM{M0_PIN})=LOW, M1(BCM{M1_PIN})=LOW")
    
    try:
        ser = serial.Serial(UART_PORT, BAUD_RATE, timeout=0.1)
        print(f"Connected to {UART_PORT} at {BAUD_RATE} baud.")
        print("Waiting for data... (Press Ctrl+C to stop)")

        while True:
            # Monitoring AUX - if it blinks, the module IS receiving radio waves
            if aux.value == 0:
                print("DEBUG: AUX Pin went LOW (Module is busy/receiving!)")

            if ser.in_waiting > 0:
                data = ser.read(ser.in_waiting)
                try:
                    # Try to decode, but show raw hex if it fails
                    decoded = data.decode('utf-8', errors='replace')
                    print(f"Received String: {decoded.strip()}")
                except:
                    print(f"Received Hex: {data.hex().upper()}")
            
            time.sleep(0.05)

    except Exception as e:
        print(f"Hardware Error: {e}")
    finally:
        if 'ser' in locals(): ser.close()

if __name__ == "__main__":
    run_diagnostic_receiver()