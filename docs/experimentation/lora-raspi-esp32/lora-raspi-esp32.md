# Experimental Plan: Battery Lifetime Comparison of an AMK3 IoT Sensor (Wi-Fi vs. LoRa)

---

## 1. Statistical Hypothesis Formulation

In the context of a scientific publication, the experiment must validate or invalidate a formal hypothesis:

* **Null Hypothesis ($H_0$):** At an equal transmission interval (5 minutes), payload reduction, the absence of TLS handshake, the delegation of timestamping to the LoRa gateway, and the use of the LoRa protocol on the physical layer do not lead to a significant reduction in the system's battery lifetime compared to a Wi-Fi 4 (802.11 b/g/n 2.4GHz) / MQTT / TLS architecture.
* **Alternative Hypothesis ($H_1$):** The overall system architecture using LoRa for the physical layer significantly increases battery lifetime. This gain is the combined result of a physical layer optimized for low power consumption and the elimination of the listening (RX) and processing (CPU) phases required by the TLS protocol and MQTT session maintenance.

---

## 2. Specification of the Two Systems (Object of Comparison)

### System A: The Wi-Fi Architecture

* **Physical Layer (PHY):** ESP32 Wi-Fi Module: Wi-Fi 4 (802.11 b/g/n 2.4GHz)
* **Software Stack:** AP Association + DHCP + TLS Handshake (Certificate Exchange) + MQTT Connection + MQTT Publish + NTP Server
* **Payload (JSON):**

    ```json
    {
      "timestamp": "2026-06-04T00:19:55+0200",
      "ID": "20250520165000",
      "type": "AquaCheck",
      "soilMoisture (%)": "71.00",
      "temperature": "24.21",
      "humidity": "48.86",
      "humidex": "27.57",
      "batteryLevel": "100.00"
    }
    ```

* **Hardware Impact:** The CPU remains awake in active mode to handle TLS cryptographic calculations and wait for TCP acknowledgments.

### System B: The LoRa Architecture

* **Physical Layer (PHY):**
  * **LoRa Module:** E220-400T30D module from Ebyte
  * **Carrier Frequency:** 428.125 MHz (Channel 18)
  * **UART Baud Rate:** 9600 bps
  * **Serial Format:** 8N1
  * **Modulation Speed (Air Speed):** 2.4k bps
  * **Frame Size:** 200 bytes
  * **Transmission Power (TX):** 30dBm
  * **Operating Mode:** Transparent transmission
  * **Ambient RSSI (LBT):** Enabled
  * **RSSI at end of message:** Enabled
  * **LBT Mechanism:** Disabled
  * **WOR Cycle:** 500ms
* **Software Stack:** None (pure LoRa communication)
* **Payload (CSV):**
  * *Format:* `Sensor_ID;Temperature,Humidity;Soil_Moisture;Battery_Percentage;\n`
  * *Example:* `20250513142900;26.4;64.5;70;82.8;\n`
* **Hardware Impact:** Minimal CPU wake-up time. The node transmits blindly (ALOHA mode) and immediately returns to deep sleep.

---

## 3. Specification and Control of Variables

To isolate the impact of the global architecture, variables are classified as follows:

### A. Independent Variable

* **System A (Wi-Fi 4 / MQTT / TLS / JSON):** Based on the ESP32, requiring an IP infrastructure and a verbose TLS security layer.
* **System B (Pure LoRa / CSV):** Based on the Ebyte module, utilizing point-to-point communication without any software network layer.

### B. Dependent Variables (Measured Results)

These are the physical/biological indicators of the system that react to the change in architecture:

* **Operating Time ($T_{Fail}$):** Total duration between the first transmitted message and hardware shutdown due to power depletion.
* **Message Count:** Final tally of successfully recorded transmissions on the server.

### C. Derived Design Variables (Imposed by the Architecture)

Variables intrinsic to the compared architectures:

* **Payload Size:** ~180 bytes (System A) vs. ~35 bytes (System B).
* **Peak Current:** Wi-Fi is inherently power-hungry, whereas LoRa transmits here at a high power of 30 dBm (1W), which is counterbalanced by an extremely short time-on-air.

### D. Controlled Variables (Strictly Identical or Neutralized)

Factors kept rigorously identical to eliminate experimental bias:

* **Cycle Interval:** 5 minutes (300 s) in *Deep Sleep*.
* **Power Source:** Identical batteries with equal initial nominal voltage.
* **Environment:** Thermal chamber at a constant temperature.
* **Sensors:** Identical measurement hardware providing the raw data values.
* **RF Environment:** Fixed, short distances (3m) to prevent automatic retransmissions caused by fading.

---

## 4. Execution and Collection Protocol

1. Simultaneous deployment of both systems.
2. Recharge and swapping of batteries for a second test run to eliminate any hardware bias tied to specific battery cell discrepancies.

The experimental process allows the collection of 4 distinct $T_{Fail}$ values:

* LoRa (Battery A & Battery B)
* Wi-Fi (Battery A & Battery B)

This enables a direct comparison using the exact same batteries:

* LoRa vs. Wi-Fi (Battery A)
* LoRa vs. Wi-Fi (Battery B)

---

## 5. Results and Measurements

**Expected Result:** A significantly higher $T_{Fail}$ for the LoRa system compared to the Wi-Fi system.

### Raw Experimental Data

| System Configuration | Battery Used | Operating Time ($T_{Fail}$) |
| :------------------- | :----------- | :-------------------------- |
| **System B (LoRa)**  | Battery A    | ...                         |
| **System A (Wi-Fi)** | Battery A    | ...                         |
| **System B (LoRa)**  | Battery B    | ...                         |
| **System A (Wi-Fi)** | Battery B    | ...                         |
