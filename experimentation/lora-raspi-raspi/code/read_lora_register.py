import serial
import time
from gpiozero import DigitalOutputDevice, DigitalInputDevice

# --- PIN Configuration ---
M0_PIN = 23
M1_PIN = 24
AUX_PIN = 18
SERIAL_PORT = "/dev/ttyAMA0"
BAUD_RATE_CONFIG = 9600 

def decode_config(data):
    """Decodes the received bytes according to the E220-400T30D manual"""
    if len(data) < 11:
        return print("Incomplete data.")

    regs = data[3:]
    address = (regs[0] << 8) | regs[1]
    
    uart_rates = {0: "1200", 1: "2400", 2: "4800", 3: "9600", 4: "19200", 5: "38400", 6: "57600", 7: "115200"}
    parity_bits = {0: "8N1", 1: "8O1", 2: "8E1", 3: "8N1 (Special)"}
    air_rates = {0: "2.4k", 1: "2.4k", 2: "2.4k", 3: "4.8k", 4: "9.6k", 5: "19.2k", 6: "38.4k", 7: "62.5k"}
    
    uart_baud = uart_rates.get((regs[2] >> 5) & 0x07)
    parity = parity_bits.get((regs[2] >> 3) & 0x03)
    air_rate = air_rates.get(regs[2] & 0x07)

    packet_sizes = {0: "200 bytes", 1: "128 bytes", 2: "64 bytes", 3: "32 bytes"}
    tx_powers = {0: "30dBm", 1: "27dBm", 2: "24dBm", 3: "21dBm"}
    
    packet_size = packet_sizes.get((regs[3] >> 6) & 0x03)
    rssi_noise = "Enabled" if (regs[3] >> 5) & 0x01 else "Disabled"
    tx_power = tx_powers.get(regs[3] & 0x03)

    channel = regs[4]
    frequency = 410.125 + channel 

    rssi_byte = "Enabled" if (regs[5] >> 7) & 0x01 else "Disabled"
    trans_mode = "Fixed" if (regs[5] >> 6) & 0x01 else "Transparent"
    lbt_enable = "Enabled" if (regs[5] >> 4) & 0x01 else "Disabled"
    wor_cycles = {i: f"{(i+1)*500}ms" for i in range(8)}
    wor_cycle = wor_cycles.get(regs[5] & 0x07)

    print("-" * 40)
    print(f"CURRENT MODULE CONFIGURATION")
    print("-" * 40)
    print(f"Module Address      : 0x{address:04X} ({address})")
    print(f"Frequency (Channel) : {frequency:.3f} MHz (Channel {channel})")
    print(f"UART Speed          : {uart_baud} bps")
    print(f"Serial Parity       : {parity}")
    print(f"Air Speed (LoRa)    : {air_rate} bps")
    print(f"Packet Size         : {packet_size}")
    print(f"TX Power            : {tx_power}")
    print(f"Transmission Mode   : {trans_mode}")
    print(f"Ambient RSSI (LBT)  : {rssi_noise}")
    print(f"RSSI at end of msg  : {rssi_byte}")
    print(f"LBT (Listen Before) : {lbt_enable}")
    print(f"WOR Cycle           : {wor_cycle}")
    print("-" * 40)

def read_registers():
    # Using 'with' for clean and immediate resource release
    try:
        with DigitalOutputDevice(M0_PIN, initial_value=True) as m0, \
             DigitalOutputDevice(M1_PIN, initial_value=True) as m1, \
             DigitalInputDevice(AUX_PIN) as aux, \
             serial.Serial(SERIAL_PORT, BAUD_RATE_CONFIG, timeout=2) as ser:

            print("Switching to Configuration mode (M0=1, M1=1)...")
            
            # Wait for AUX stabilization (High = ready)
            start_wait = time.time()
            while aux.value == 0:
                if time.time() - start_wait > 2.0:
                    print("Timeout: the module is not responding on the AUX pin.")
                    break
                time.sleep(0.01)
            
            time.sleep(0.1) 

            # Command: C1 (Read) + 00 (Start Addr) + 08 (Length) 
            cmd = bytes([0xC1, 0x00, 0x08])
            print(f"Sending read command: {cmd.hex().upper()}")
            
            ser.write(cmd)
            ser.flush()

            response = ser.read(11) 

            if response:
                print(f"Raw response received: {response.hex().upper()}")
                decode_config(response)
            else:
                print("Error: No serial response from the module.")

            # Before exiting the 'with' block, return to normal mode (optional but clean)
            print("Resetting pins to Normal mode (M0=0, M1=0)...")
            m0.off()
            m1.off()
            # Wait briefly for the module to validate the mode change
            time.sleep(0.1)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Here, the m0, m1, aux, and ser objects are already closed by the 'with' block
        print("Resources released.")

if __name__ == "__main__":
    read_registers()
    # A slight final sleep sometimes helps lgpio finish its internal threads
    time.sleep(0.1)