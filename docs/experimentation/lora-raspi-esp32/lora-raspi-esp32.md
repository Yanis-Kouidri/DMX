# LoRa between ESP32 and Raspberry Pi 5

**Goal**: Use an ESP32 to send Aquacheck sensor data to a Raspberry Pi 5 gateway using LoRa. The Raspberry Pi will send sensing data to the MQTT AWS server through internet using Wi-Fi or Ethernet.

**Goal 2**: Compare the battery longevity of current Wi-Fi-based Aquacheck sensors against LoRa-based configurations to evaluate power efficiency.

## Sensor using Wi-Fi: issues

Currently, the Aquacheck sensor use ESP32 Wi-Fi to send his data to the MQTT AWS server. This is not ideal in terms of energy consumption for the following reason:

- At each wake-up (every 5 minutes) the ESP32 has to scan Wi-Fi networks, connect to the good one, wait for an IP address (DHCP). It can take seconds when radio interface is active and radio interface is what consume the most in a sensor.
- Wi-Fi consume more the other IoT oriented radio technology such as LoRa, Zigbee or Bluetooth Low Energy (BLE).
- TLS connection between ESP and AWS server involved handshake, encryption, and certificates which add overhead of data to transmit over the radio and CPU usage.

Using LoRa will reduce these problems.

## Experimentation details

To perform a comparison I will put the nominal Aquacheck on battery and measure the lifetime. Then I will use the same Aquacheck with the same battery in the same place and measure the lifetime. The only difference will be the code that no longer rely on Wi-Fi but on LoRa. The sleep cycle will remain the same. The idea is to measure approximately the difference of lifetime between Wi-Fi and LoRa not to perform a precise experimentation over dozen of sensors.

## Hardware used

- uPesy ESP32 Wroom Low Power DevKit (x1)
- E220-400T30D module from Ebyte (x2)
- Raspberry Pi 5 (x1)

## Connection ESP32 — LoRa

Pin connection tables

| LoRa Module Pins | ESP32 Wroom Low Power Dev Kit |
|------------------|-------------------------------|
| M0               | GPIO 13                       |
| M1               | GPIO 14                       |
| RXD              | GPIO 17 (TX2)                 |
| TDX              | GPIO 16 (RX2)                 |
| AUX              | GPIO 4                        |
| VCC              | VIN                           |
| GND              | GND                           |
