# LoRa and LoRaWAN

## LoRa

LoRa stand for Long Range. It's a **low power** and **long range** radiocommunication technique. It refers to the **physical layers**. LoRa is the radio signal that transmits the data over the air using a modulation called Chirp Spread Spectrum (CSS). It's a proprietary technology developed originally by the French start-up Cycléo in Grenoble in 2009 then acquire by US company [Semtech](https://semtech.fr) in 2012.

!!! warning

    “LoRa” is not short for “LoRaWAN”

## LoRaWAN

LoRaWAN stands for Long Range Wide Area Network. It defines the Media Access Control (MAC) and the network layer in top of LoRa. It handles the network architecture, device classes, frequency, security, adaptative data rate, message scheduling and acknowledgments and duty cycle. LoRaWAN is an open standard maintained by the [LoRa Alliance](https://lora-alliance.org/).

## Current issues

Whereas LoRa and LoRaWAN are mature, it remains issues. Here is a non-comprehensive list of them:

- **Scalability**: With the explosion of number of sensors in urban area the probability of packets collision increase drastically. Solution such as LR-FHSS (Long Range Frequency Hopping Spread Spectrum) or LBT (Listen-Before-Talk) are under studies.
- **Security**: Currently, LoRaWAN used AES-128 to encrypt data which is not post quantic. Moving to AES-256 could solve the problem but will drastically increase the CPU cost.
- **Maintainability**: It's possible to update firmware via FUOTA (Firmware Update Over The Air) but problems remains.
- **Satellites**: I could be interesting to add satellite connection, but problem appears such as Doppler effect with LEO satellite and intelligent handover between terrestrial network and NTN.
- **Edge computing and AI**: Reduce message to send using tiny ML model over sensor to do anomaly detection for example.
- **Zero-Power and energy harvesting**: The idea is to remove battery and to rely only on external source of power such as sun or vibration. That required an opportunistic protocol to send data when energy is available.

## Technical aspects

### Classes

In LoRaWAN, end-devices operate in one of three classes: A, B, or C. These classes define how devices communicate with and listen to the network. Class A is mandatory for all LoRaWAN devices, while Classes B and C are optional extensions.

#### Class A

The device opens two short reception windows (RX1 and RX2) only after transmitting a message. Outside of these windows, the device cannot receive any incoming messages. Class A is the most energy-efficient mode because continuously listening for downlink messages consumes significant battery power.

#### Class B

In addition to the standard RX1 and RX2 windows, the gateway regularly broadcasts a synchronization signal (a beacon). The device uses this beacon to open scheduled, periodic reception windows called Ping Slots. Class B consumes more power than Class A, but it enables reliable remote control with predictable latency on battery-powered devices.

#### Class C

The reception window is kept open almost continuously, closing only while the device is actively transmitting. This mode requires a constant power supply (typically mains power), but it offers near-zero latency for receiving commands or downlink data immediately.

### Spreading Factor (SF)
