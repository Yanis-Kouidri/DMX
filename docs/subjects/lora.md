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
