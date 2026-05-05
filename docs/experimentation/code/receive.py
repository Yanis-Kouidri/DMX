import serial
import time
from gpiozero import DigitalOutputDevice

# Pin configuration for NORMAL mode (M0=0, M1=0)
m0 = DigitalOutputDevice(23, initial_value=False)
m1 = DigitalOutputDevice(24, initial_value=False)
BAUD_RATE = 9600


def run_lora_receiver():
    print("--- Pi 5 LoRa Receiver Operational (RSSI Enabled) ---")
    
    try:
        # Opening the serial port with a timeout to avoid blocking indefinitely
        ser = serial.Serial("/dev/ttyAMA0", BAUD_RATE, timeout=1)
        
        while True:
            # Using read_until to wait for the end of the line (\n)
            # This function blocks until the timeout or the character is received
            header_data = ser.read_until(b'\n')
            
            if header_data:
                # If data is received, the RSSI byte arrives immediately AFTER the \n
                # Wait briefly or check for availability
                rssi_byte = ser.read(1)
                
                if rssi_byte:
                    rssi_raw = rssi_byte[0]
                    # RSSI calculation for E220: -(256 - value)
                    rssi_dbm = -(256 - rssi_raw)
                    
                    try:
                        # Message decoding (stripping \r\n with strip)
                        decoded_msg = header_data.decode('utf-8', errors='replace').strip()
                        
                        print(f"[{time.strftime('%H:%M:%S')}] "
                              f"Message: {decoded_msg: <25} | "
                              f"Signal: {rssi_dbm} dBm")
                    except Exception as e:
                        print(f"Decoding error: {header_data.hex().upper()} | RSSI: {rssi_dbm} dBm")
                
            # No need for sleep(0.05) here because read_until is blocking (more CPU efficient)

    except KeyboardInterrupt:
        print("\nStopping script...")
    finally:
        if 'ser' in locals() and ser.is_open:
            ser.close()

if __name__ == "__main__":
    run_lora_receiver()