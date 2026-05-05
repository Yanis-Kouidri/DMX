# LoRa over Raspberry Pi and ESP32

## LoRa between Raspberry Pi 5 and Raspberry Pi 5

Goal: send messages between 2 Raspberry Pi 5 using LoRa.

### Step 1: Connect LoRa Module

I use E220-400T30D module from Ebyte and I have a Raspberry Pi 5.
In order to connect the LoRa module to the Raspi I have to use the 40-pin GPIO (General Purpose Input Output).

![Raspi-GPIO-Global](images/GPIO-Pinout-Diagram-2.png)

![Raspi-GPIO-Detail](images/GPIO.png)

And connect it the E220-400T30D LoRa module

![E220-400T30D-LoRa-module](images/LoRa-module.jpg)

Follow the following schema using Dupont cable to connect pins

![Pin-connection-schema](images/pin-connection-schema.jpg)

To summarize

| LoRa Module Pins | Raspberry Pi 5 pins      |
|------------------|--------------------------|
| M0               | Pin 16 (GPIO 23)         |
| M1               | Pin 18 (GPIO 24)         |
| RXD              | Pin 8 (GPIO 14 TDX)      |
| TDX              | Pin 10 (GPIO 15 RDX)     |
| AUX              | Pin 12 (GPIO 18 PXM_CLK) |
| VCC              | Pin 4 (5V)               |
| GND              | Pin 6 (Ground)           |

!!! warning

    RDX on LoRa module is connected to TDX on Raspberry, this is normal. And vice-versa for TDX.

### Step 2: Configure Raspi

1. Connect to the raspi over ssh for example the run

    ```bash
    sudo raspi-config
    ```

2. Navigate to Interface Options:

    Use your arrow keys to select `3 Interface Options` and press Enter.

3. Select Serial Port:

    Find `I6 Serial Port` and press Enter.

4. Answer "No" to the Login Shell:

    The tool will ask: "Would you like a login shell to be accessible over serial?"
    Select `<No>`.

5. Answer "Yes" to Enable Hardware:

    The tool will then ask: "Would you like the serial port hardware to be enabled?"
    Select `<Yes>`.
    Why? This ensures the GPIO pins (8 and 10) are actually powered and assigned to the UART controller.

6. Finish and Reboot:

    Select `<Finish>` on the main menu.  
    Select `<Yes>` when it asks if you would like to reboot now.

7. Install dependencies

    ```bash
    sudo apt update -y && sudo apt install -y python3-dev liblgpio-dev
    ```

### Step 3: Configure LoRa Module

Install uv once on each raspi

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Install dependencies, go in `DMX/docs/experimentation/code`

```bash
uv sync
```

In order to get RSSI and to set the same parameter such as UART rate (baud rate) and air date rate you have to flash to send a command to write the LoRa E220 module register.

To perform that, run on **both** receiver and sender:

```bash
uv run congigure_lora_register.py
```

### Step 4: Run the code

Go in `DMX/docs/experimentation/code` folder.

Then run `send.py` on one raspi and `receive.py`, one the other one.

```bash
uv run send.py
```

```bash
uv run receive.py
```

Then you should see on the receiver side:

```log
❯ uv run receive.py
--- Pi 5 LoRa Receiver Operational (RSSI Enabled) ---
[14:19:55] Message: Pi5 LoRa Message #1       | Signal: -9 dBm
[14:20:00] Message: Pi5 LoRa Message #2       | Signal: -10 dBm
[14:20:06] Message: Pi5 LoRa Message #3       | Signal: -10 dBm
^C
Stopping script...
```

!!! success

    Congratulation you have set up a LoRa connection between 2 Raspi.
