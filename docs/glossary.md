# Glossary

## 3GPP

3rd Generation Partnership Project, organization that standardized mobile networks (3G/4G/5G/6G)

## ABP (Activation By Personalization)

ABP is a LoRaWAN acronym contrasting with OTAA. While OTAA uses a Join-Request message to negotiate session keys dynamically, ABP relies on pre-configuring keys directly on the device so it can communicate immediately without prior negotiation. It is less secure because session keys never rotate, and less flexible because changing network servers requires physically re-provisioning the device.

## Adaptive Data Rate (ADR)

Adaptive Data Rate (ADR) is a radiocommunication concept where the data rate is dynamically adapted depending on radio link metrics. Basically, if the radio link is bad, the ADR mechanism will reduce the data rate in order to successfully reach the destination. Conversely, if the radio link is good, it will raise the data rate.

## Agent

In AI, an Agent is a system that can **perceive** its environment and take **actions** to achieve a specific goal.  
Examples:

- Physical Agent: A Roomba vacuum. Its goal is to clean the floor. Its sensors (bumpers/lasers) provide the observations, and its motors provide the actions.
- Digital Agent: A trading bot on the stock market. Its goal is profit. Its observations are stock prices, and its actions are buy/sell orders.
- AI Agent (LLM-based): A tool that you ask to "Book a flight." It doesn't just talk about flights; it actually goes to websites, searches for dates, and interacts with the booking system until the task is done.

## ALOHA

ALOHA is a very simple Medium Access Control (MAC) protocol. It works with random access to support, when a station has to transmit a message, it transmits without sensing the channel prior. Collisions are frequent, so the reliability relies on ACK messages. In pure ALOHA the maximum throughput is about 18.4% of the channel bandwidth. Pure ALOHA is used in LoRaWAN.

## ATSR

Ambient Trust Sensor Routing. A routing protocol specifically designed for Wireless Sensor Networks (WSNs). Instead of simply finding the shortest path, it searches for the most reliable path by assigning a trust score to neighboring nodes based on factors like battery level, link quality, and packet delivery success rate.

## ATSSS

Access Traffic Steering Switching and Splitting, it's a functionality introduced by 3GPP (release 16) to allow User Equipment (UE) to be connected to internet through different access network such as 5G and Wi-Fi.

## ATSSS-LL

ATSSS-Low Level is a lightweight alternative to MPTCP for non TCP traffic such as UDP.

## AUV

Autonomous Underwater Vehicle

## Bundle layer

Bundle layer is used in DTN to perform **store-carry-and-forward**. It sits between application layer and lower-level networking layer. In regular networks such as the Internet, the application layer (e.g., HTTP) talks directly to transport layer (e.g., TCP), DTN add bundle layer with bundle protocol and **Convergence Layer Adapters** (CLA). CLA enable **Bundle Protocol** to run on top of anything (e.g., TCP, UDP, CCSDS, Data mule).

## CA-ETX

Contact Aware Expected Transmission Count, improvement of ETX metric by taking into account the possibility the link may be cut due to the physical distance. Useful for mobile sink in WSN for example.

## CLA

Convergence Layer Adapter, the CLA acts as glue between Bundle Protocol and anything under. Bundle Protocol is designed to be **agnostic**. The role of CLA is to encapsulate, manage connection, discover neighbor and sometimes add reliability. There are different CLAs such as TCP CLA, Bluetooth/BLE CLA, LTP CLA and HTTP/Web CLA.

## CoAP

CoAP stands for Constrained Application Protocol, it's a web protocol tailored for IoT. Whereas HTTP is heavyweight, CoAP is lightweight. For example, it uses UDP instead of TCP, short headers, and DTLS for security.
CoAP uses the same REST architecture as HTTP (it natively supports GET, POST, PUT, DELETE).

## CSA

CSA stands for Connectivity Standards Alliance. It's a non-profit organization that gathers over 600 companies working on IoT. Its goal is to create and maintain standards to facilitate communication between IoT devices.

## CSMA

CSMA (Carrier Sense Multiple Access) is a Medium Access Control (MAC) protocol where nodes check (sense) the shared channel for activity before transmitting to reduce collisions. If the channel is busy, the node waits; if idle, it transmits. Common variants handle collision handling differently:

- CSMA/CD (Collision Detection): Aborts transmission immediately when a collision is detected (legacy Ethernet).
- CSMA/CA (Collision Avoidance): Uses random back off times and acknowledgments to avoid collisions altogether (Wi-Fi).
- CSMA/CR (Collision Resolution / Bitwise Arbitration): Uses priority-based arbitration, so dominant bits overwrite recessive bits without destroying the message (CAN bus).

## Data mule

Data mule is a mobile node such as a person, a bus, a drone, etc. It carries physically the data from a source to a destination. It's particularly convenient in remote area where direct wires and wireless (e.g., 5G, 4G) communication are not possible.

## DECT

DECT stands for Digital Enhanced Cordless Telecommunications. It is the primary wireless technology used by landline phones to communicate with their base stations. Because DECT operates on dedicated frequency bands, it is far less subject to signal interference than standard Wi-Fi or Bluetooth devices. DECT remains widely used today and has evolved into CAT-iq (for high-definition IP voice) and DECT NR+ (for non-cellular 5G IoT networks).

## Deep Learning (DL)

In traditional ML, humans perform Feature Engineering. You have to identify the most important characteristics of the data before feeding it into the algorithm. If you choose the wrong features, the model won't work well, regardless of how good the algorithm is.  
Deep Learning uses Artificial Neural Networks with many layers (hence the "Deep") to perform by itself the feature extraction. It requires massive amounts of data, GPUs and can take days or weeks to train.  
Whereas classical ML is excellent for Structured Data (things you find in Excel sheets or SQL databases). Deep Learning excels at Unstructured Data, which is data that doesn't fit neatly into a table.

## DER (Data Extraction Rate)

DER is the equivalent of PDR (Packet Delivery Ratio) at an applicative layer such as Network Server in LoRaWAN.

## DOP

Dilution Of Precision, In context of GNSS and wireless positioning, DOP is a mathematical value that represents the quality of geometry depending on anchors (such as satellites or UAV) position. When anchors are spread all around the user, geometry is good so DOP is low. If anchors are clustered close together or on a same line, geometry is poor, so DOP is high and the computed position of user is uncertain.

## DTN

Delay Tolerant Network, DTN is a specific type of network architecture to operate where there is no guarantee of end to end communication such as on Intermittently Connected Networks (ICN). Whereas regular networks such as Internet will just drop a packet if the next hop is not connected, DTN will use the mechanism of **store-carry-and-forward** to transmit a packet when the next hop will be reachable. A node will receive data from another node, wait a time from minutes to days then, once connection is established, forward the packet to the next node. DTN use **bundle layer** on top of transport layer acting as an overlay.

## Duty-cycling (sleep/wake up)

In case of a sensor, it's a technique to alternate between wake and sleep cycles in order to save battery instead of being always awake. However, during the sleep cycle the sensor can neither sense nor communicate through radio.

## EMQX

[EMQX](https://github.com/emqx/emqx) is an open-source MQTT broker for IoT. It is highly scalable, clusters well, and can handle up to 100 million concurrent MQTT connections per cluster. Beyond MQTT and WebSockets, it also supports CoAP, LwM2M, and HTTP via protocol gateways.

## End device, end node

In an LPWAN context, an end device (or end node) refers to an IoT device connected to one or several gateways.

## ETX

Expected Transmission Count, metric that estimates the number of transmissions required to send a message over one link at an instant T. ETX = 1 → perfect link, ETX = 2 → 50% of packets are lost, etc.

## FANET

Flying Ad-hoc Network, drones swarm that communicate together.

## FBL

FBL stands for Finite BlockLength. A paradigm contrasted with Infinite Blocklength (which assumes arbitrarily long messages where traditional error-correcting codes achieve near-perfect reliability). FBL applies heavily to IoT because messages are extremely short (often just a few bytes). In short packets, overhead is high, and a single burst of noise can degrade a huge portion of the payload, requiring specialized short-block channel coding.

## Feature extraction

Feature extraction is the process to extract key characteristics from raw data for the computer to use them to take decision. Example: for dog Vs. cat model, feature could be shape, size and textures.  
In ML, it is up to the user to extract features. This is called feature engineering. In DL it's the role of the neural network.

## FUOTA

FUOTA stands for Firmware Update Over-The-Air. It's a technique to update an IoT device without plugging any cable. It uses regular wireless access such as Wi-Fi, LoRaWAN or Sigfox to send the new firmware.

## GDR RSD

GDR RSD stands for Groupement De Recherche Réseaux et Systèmes Distribués. It's a research network attached to the CNRS. Its goal is to animate and federate the French research community around network and distributed systems. It organizes for example the GDR RSD Days.

## HAPS

High-Altitude Platform Stations, HAPS are unmanned vehicles that hover in the stratosphere, roughly 20 km above the Earth. It can be solar-powered drone or giant balloons.

## Hop-by-hop routing

Hop-by-hop routing is a network routing technique where a data packet is forwarded through a series of intermediate routers (called "hops") toward its final destination.
Instead of the sender pre-mapping the entire path, each router along the way independently inspects the packet and decides only the single next best step to forward it. Internet mainly uses hop-by-hop routing through IP.

## ISM bands

Industry Science and Medical frequency bands open to use without any prior authorization or license.

## KNN

K-Nearest Neighbors, algorithm used for classification and regression that labels a sample according to its K closest neighbors. It can also be used for anomaly detection, to identify if a variable or a vector (several variables) is normal or abnormal.

## LNS (LoRaWAN Network Server)

The LNS is the core of a LoRaWAN network. It receives the frames forwarded by the gateways, removes duplicates when several gateways receive the same frame, verifies message integrity (MIC) with the network session keys, manages Adaptive Data Rate (ADR) and MAC commands, and routes the payloads to the appropriate Application Server. It also selects the best gateway to send downlink messages. Examples of LNS include The Things Stack (used by TTN), ChirpStack and AWS IoT Core for LoRaWAN. See [Network Server (NS)](subjects/lora.md#network-server-ns).

## LoS

Line of Sight, in telecommunication, LoS refers to a clear and unobstructed path between the transmitter and the receiver antenna.

## LPWAN

Low Power Wide Area Network, network using long range and low power wireless communications such as LoRaWAN, LTE-M, NB-IoT, Sigfox. See [Wikipedia](https://en.wikipedia.org/wiki/Low-power_wide-area_network)

## LR-FHSS

LR-FHSS stands for Long Range — Frequency Hopping Spread Spectrum. It's a radio protocol designed to extend LoRaWAN network capacity. It's an alternative to legacy CSS (Chirp Spread Spectrum) used by default in LoRaWAN. It's mainly used for Direct-to-Satellite communication. LR-FHSS is highly resistant to the Doppler effect, more resistant to interference and has approximately the same range as CSS but a lower throughput.

## LSTM

Long Short-Term Memory, AI model to perform prediction

## LTE-M

Long Term Evolution for Machine, LPWAN technology developed by the 3GPP for IoT connection using 4G band (LTE). It provides a good mobility management.

## LWSN

Linear Wireless Sensor Network, network of wireless sensors arranged linearly.

## Machine Learning (ML)

Machine Learning is a branch of Artificial Intelligence (AI) focused on developing systems that can learn from data and improve their performance without being explicitly programmed. Instead of following rigid, hand-coded instructions, ML systems use statistical algorithms to identify patterns and perform feature extraction. This process results in a trained model: a mathematical representation that can generalize from its training to make predictions or automate decisions on new, unseen data (such as performing image classification to distinguish between a dog and a cat).
The learning can be:

- **Supervised Learning**: In this approach, the algorithm is trained on a labeled dataset, where each input is paired with its corresponding correct output (ground truth). The goal is for the model to learn a mapping function that can predict labels for new data. Example: Feeding an algorithm thousands of images tagged "dog" or "cat" so it learns to classify future images.
- **Unsupervised Learning**: This paradigm involves training on unlabeled data. The algorithm must independently discover the underlying structure or hidden patterns within the data. Primary Technique: **Clustering**, which groups data points based on shared characteristics or features (e.g., grouping photos by visual similarity without knowing what the objects are).
- **Reinforcement Learning (RL)**: This is an agent-based learning method where a system learns to achieve a goal in a dynamic environment through trial and error. The agent receives feedback in the form of rewards or penalties based on the actions it takes, allowing it to optimize its strategy (policy) over time.

Traditional programming uses Rules + Data = Answers. Machine Learning flips the script: Data + Answers = Rules.

## Matter

Application layer protocol working over IPv6. It comes from an open standard designed to connect smart home devices from different brands. Created by the CSA.

## MBN

Mobile Backbone Network, mobile communication backbone as opposed to a static communication backbone such as 4G/5G antennas.

## MEC

Multi-access Edge Computing (formerly Mobile Edge Computing), strategy focusing on bringing computational power closer to the network edge (therefore closer to the user)

## Meshcore

Meshcore is an alternative to MeshTastic, it works on the same devices and uses LoRa but includes more hierarchy and structure to reduce the noise due to flooding. Clients don't repeat received messages, only repeaters can do that, and a room server stores the messages.

## MeshTastic

MeshTastic is an open source project to create a decentralized wireless communication network without any physical infrastructure. It uses LoRa over a mesh network. MeshTastic is a MANET (Mobile Ad hoc NETwork) because nodes are mobile, and it doesn't rely on a preexisting physical infrastructure.

## mioty

mioty is an LPWAN technology developed by the German institute Fraunhofer IIS and standardized by ETSI. The physical layer relies on TSMA (Telegram Splitting Multiple Access), a patented transmission method that splits messages into tiny sub-packets. It operates on **unlicensed ISM bands**, has **extreme resistance** to noise and interference, and was designed for **massive IoT deployment**.

Unlike LoRa, which requires proprietary Semtech hardware, mioty’s physical layer is software-defined and can run on standard sub-GHz radio chips from multiple vendors. However, the core TSMA technology is protected by patents (licensed through a Sisvel patent pool), and commercial software stacks usually need to be purchased from stack vendors while LoRaWAN stack is completely open. That said, it is still possible to use basic mioty stacks for free in non-commercial or academic contexts.

## mMTC

mMTC stands for massive Machine Type Communication. It's a type of network that allows a huge number of IoT devices in the same area, such as 1 million per km². It's a core part of 5G and 6G, defined by 3GPP.

## MNT

MNT stands for Multi Technology Network, it means a network that relies on several underlying technologies such as Wi-Fi, Ethernet, LoRaWAN etc.

## Mote

A mote is a sensor that has 4 things:

- A sensor equipment to measure a metric such as temperature or humidity.
- A radio module to communicate remotely.
- A source of energy such as a battery.
- A microcontroller unit to handle sensing, data transmission and sleep cycle.

Motes are end devices on an IoT network.

## MPLS

MPLS (Multiprotocol Label Switching) is a traditional networking technique designed to speed up and direct network traffic by using short path labels instead of long network addresses.

Instead of having every intermediate router read the full IP destination and consult a complex routing table at each hop, the ingress router assigns a fixed label (a number) to the packet header. Intermediate routers simply swap this label and forward the packet at hardware speeds along a predetermined path (LSP), making it an ideal technology for building private WANs and VPNs across service provider networks.

## MPTCP

Multi-Path Transmission Control Protocol, an extension of standard TCP allowing the simultaneous use of multiple network paths to reach the destination.

## Multi-armed bandit (MAB)

In AI, the Multi-Armed Bandit is a classic reinforcement learning problem where an agent must maximize total reward when faced with multiple options (arms) of unknown reward probabilities. The agent must continuously balance exploration (trying under-tested arms to find better rewards) and exploitation (choosing the current highest-yielding arm).

## MWSN

Mobile Wireless Sensor Network, network of mobile wireless sensors as opposed to fixed sensors.

## NB-IoT

Narrow Band Internet of Things, is a LPWAN technology developed by the 3GPP for IoT using 4G and 5G bands.

## NDN

Named Data Networking, in regular network such as IP, to access a data, you use its location, the where. In NDN, to get a data, you specify what you want, no matter where it is. There are neither source nor destination address, just interested data. Each NDN router records which port requests which data in its Pending Interest Table (PIT) and forwards it to the next interface using FIB (Forwarding Information Base). Routers can cache data previously requested.

## Neural network

A neural network is a digital imitation of the human brain. It is composed of several layers of neurons where each neuron takes several inputs, calculates their importance, and decides if it should "fire" a signal to the next layer. The final layer gives you the answer (e.g., "98% Dog, 2% Cat"). Each neuron has weights that represent the importance of an input. These weights are initially random and thanks to feedback weight are adjusted.

## NTN

Non-Terrestrial Network, NTN is a telecommunication system that uses spaceborne or airborne vehicle such as satellite or HAPS to transmit signals, rather than relying on traditional ground-based cell towers. It becomes handy in places where traditional networks are impossible to set up such as deep forest, ocean, remote area and high-altitude. NTN rely on LEO (Low Earth Orbit), MEO (Medium Earth Orbit) and GEO (Geostationary) satellites. It also relies on HAPS (High-Altitude Platform Stations).

## OBC

Opportunistic Backpressure Collection, routing protocol using CA-ETX metric.

## Opportunistic routing (OR)

Opportunistic routing is an approach to move data through a network using broadcast nature of wireless communications. In the traditional routing approach, a single path is defined between source and destination and used to carry data. That works well on reliable infrastructure such as cable but in wireless communication, a link can fail. Therefore OR uses a candidate set of potential forwarders. It works in three steps:

1. **Broadcast**: The sender broadcasts the data packet. Any neighbor in the “candidate set” that successfully receives it becomes a potential relay.
2. **Coordination**: The nodes that heard the message talk to each other (or use timers) to decide who is in the best position to move the data closer to the destination.
3. **Forwarding**: The “best” node (usually the one closest to the target) forwards the packet, and the other nodes discard their copies to avoid duplicates.

This approach is implemented in different protocol such as ExOR, MORE, EPIDEMIC, PROPHET etc.

## OTAA (Over-The-Air Activation)

OTAA is a dynamic and secure authentication method used in LPWANs such as LoRaWAN to onboard a device to the network. It relies on a Pre-Shared Key (PSK) known by both the server and the device to generate session keys that secure communication.

## PDR

Packet Delivery Ratio also called PSR (Packet Success Ratio). Network metric to measure how many packets are successfully delivered to the destination compared to the total number of packets sent.

$$
PDR = \frac{Number\ Of\ Packet\ Successfully\ Received}{Number\ Of\ Packet\ Sent} * 100
$$

## Regulatory Duty-cycle

Duty-cycle can refer to legal regulations that restrict a device's transmission time on free frequency bands (e.g., limiting transmission to no more than 1% of the time) to prevent network congestion.

## RFID

Radio Frequency Identification, method to memorize and give back data in a chip without battery.

## RFID NFC

RFID Near Field Communication, technology using RFID chip to communicate on a very short distance (few centimeters). Used in debit card and transport pass for example.

## RFID UHF

RFID Ultra High Frequency, technology using RFID chip to identify object using UHF bands that allow a range up to 15 meters.

## RODENT

Routing Over Different Existing Network Topologies. A routing protocol designed to route across multiple topologies, making it well-suited for Multi-RAT (Multi-Radio Access Technology).

## RSSI (Received Signal Strength Indicator)

RSSI (Received Signal Strength Indicator) is a relative measurement of the total radio power received by an antenna, expressed in dBm.

It measures all incoming energy on the channel, combining the desired signal, background noise, and interference. Because of this, **a strong RSSI does not guarantee a good connection**; if the signal is strong but drowned in heavy interference, performance will still be poor.

Values typically range from around $-30\text{ dBm}$ (very strong) to $-100\text{ dBm}$ (extremely weak).

## SAW sensor

Surface Acoustic Wave sensor, it's a passive sensor (without battery) that can perform a measurement and send back the information only thanks to an electromagnetic wave sent by the collector.

## SCA

Successive Convex Approximation, operations research algorithm that allows transforming a complex problem (non-convex) into a simple one (convex)

## SCHC

SCHC stands for Static Context Header Compression and Fragmentation ([RFC 8724](https://datatracker.ietf.org/doc/html/rfc8724)). It enables resource-constrained IoT devices to connect to the Internet over Low-Power Wide-Area Networks (LPWAN). It works by compressing large network headers (like IPv6/UDP) over the constrained radio segment between the sensor and a gateway. Both the sensor and the gateway share a pre-configured Static Context (a set of rules). Instead of transmitting the full header, the sensor only sends a short Rule ID, allowing the gateway to fully reconstruct the original Internet packet.

## Segment Routing

Segment Routing is a specific implementation of source routing where the source specifies the segments to use instead of specifying the whole IP address stack of each router to cross.

## SID

A SID (Segment Identifier) is a fundamental instruction in Segment Routing that tells the network where to send a packet or what action to perform on it.

Instead of just pointing to a destination address, a SID represents a specific node, a physical link, or a service (like a VPN or firewall). In SR-MPLS, SIDs are encoded as MPLS labels, while in SRv6, they are represented as 128-bit IPv6 addresses. By chaining multiple SIDs together at the source router, the network can steer traffic along precise, customized paths.

## Sigfox

Sigfox is a proprietary LPWAN technology that works over unlicensed bands. Sigfox is a company that owns its private network and manages it. The user only has to buy a Sigfox antenna and a subscription to the service, then Sigfox relays the received data to an internet endpoint the client chooses.

## SINR (Signal to Interference plus Noise Ratio)

A mix between SNR and SIR.

## SIR (Signal-to-Interference Ratio)

SIR is the ratio between the signal strength a receiver wants to pick up and the strength of other unwanted signals. It differs from SNR (Signal-to-Noise Ratio), which measures the ratio of signal strength to background noise. Unlike interference, noise is a natural phenomenon that does not come from other transmitting stations.

## SNR (Signal-to-Noise Ratio)

SNR (Signal-to-Noise Ratio) is a metric used to evaluate the quality of a radio link. It compares the power of the desired signal to the power of the background noise (thermal noise from the environment and the receiver electronics). Higher is better. It is usually expressed in decibels (dB):

$$
SNR_{dB} = 10 \log_{10}\left(\frac{P_{signal}}{P_{noise}}\right) = P_{signal\ (dBm)} - P_{noise\ (dBm)}
$$

Unlike RSSI, which measures the total received power (signal + noise + interference), SNR tells how distinguishable the signal is from the noise. Therefore, a link can have a weak RSSI but still a good SNR in a quiet environment, and conversely. When interference from other transmitters is also taken into account, SIR and SINR are used instead.

An SNR of $0\text{ dB}$ means the signal and the noise have the same power. Most modulations (e.g., Wi-Fi, Bluetooth) need a positive SNR to decode a packet, whereas LoRa, thanks to its Chirp Spread Spectrum (CSS) modulation, can demodulate signals **below the noise floor**. The minimum SNR required depends on the Spreading Factor: from about $-7.5\text{ dB}$ at SF7 to $-20\text{ dB}$ at SF12. This is one of the reasons why LoRa reaches long ranges, and why LoRaWAN uses the SNR margin in its ADR mechanism to choose the most suitable SF.

## Source routing

Source routing is the opposite approach to hop-by-hop routing: instead of relying on each router to decide the next hop, the sender (the source) pre-determines the entire path the packet must take across the network.

The sender embeds an ordered list of router IP addresses or interfaces directly into the packet's header. As intermediate routers receive the packet, they simply follow the explicit turn-by-turn directions written on the packet itself rather than performing independent routing decisions.

There are two main variations:

- Strict Source Routing: The sender specifies the exact sequence of every single router along the path. If a packet cannot hit a listed node in exact order, it is dropped.
- Loose Source Routing: The sender specifies key landmark nodes (waypoints) that the packet must visit, but intermediate routers can choose how to hop between those mandatory waypoints.

## Spreading Factor (SF)

The Spreading Factor is a parameter that defines the trade-off between throughput and range. In LoRa, the Spreading Factor is between 7 and 12. At SF7 the throughput is high (~5 kbps) but the range is low (~2 km). At SF12 the throughput is low (~250 bps) but the range is high (+15 km). A high SF (SF12) leads to higher time on air and higher consumption. It also consumes more of the device duty cycle.

## SRv6

SRv6 (Segment Routing over IPv6) is a modern network routing architecture that applies the principles of source routing natively over a pure IPv6 network.

Instead of relying on the default shortest path or layering complex protocols (like MPLS), the ingress router inserts an ordered list of IPv6 addresses (called SIDs) directly into the packet header. These addresses act as instructions to guide the traffic through key waypoints (traffic engineering) and trigger specific network services (VPNs, security) seamlessly.

## Stochastic

Occurring as a result of chance; random. Example: Stochastic packet arrivals—packets do not arrive at fixed intervals, but rather according to a probability distribution, such as a Poisson distribution.

## ToA (Time on Air)

ToA is the exact duration a radio transmitter actively occupies a channel to send a packet of data, from the first bit to the last.

## TOPSIS

TOPSIS stands for Technique for Order of Preference by Similarity to Ideal Solution. A mathematical multi-attribute decision-making method. Example: Selecting a route for a routing protocol.

## TTN (The Things Network)

The Things Network (TTN) is a global, open and community-driven LoRaWAN network. Anyone can deploy a gateway and connect it to TTN, which extends the shared coverage for every user. TTN provides the LoRaWAN backend (Network Server, Application Server and Join Server) based on the open-source **The Things Stack** developed by The Things Industries. End devices are registered on the TTN console and usually joined with OTAA, then their uplinks are forwarded to applications through integrations such as MQTT, HTTP webhooks or cloud platforms. TTN is free to use but applies a Fair Use Policy (about 30 seconds of uplink airtime per device per day and 10 downlink messages per day), which makes it well-suited for prototyping, research and community projects rather than critical commercial deployments. See [The Things Network](https://www.thethingsnetwork.org/).

## UART (Universal Asynchronous Receiver-Transmitter)

UART is a hardware serial communication protocol used for data transmission. It is widely used in IoT with boards such as Arduino, ESP32, and Raspberry Pi. It doesn't require a clock signal, but it requires a common ground (GND) and the same baud rate configured on both sides.

## UAV

Unmanned Aerial Vehicle, UAVs are commonly called drones. It's an aircraft that operates without a human on board. However, it can be controlled remotely by a human pilot or fly autonomously by onboard computers and pre-programmed flight plans.

## Uruha

A physical layer abstraction framework designed to simplify Multi-RAT usage in Machine-to-Machine (M2M) Air-to-Air, Air-to-Ground, and Ground-to-Ground contexts. This framework originates from a research paper and is not yet available online, though it may be possible to request it directly from the authors.

## VANET

Vehicle Ad-hoc Network, network of terrestrial vehicles that communicate together.

## VSAT (Very Small Aperture Terminal)

VSAT stands for Very Small Aperture Terminal. It's a small satellite dish (typically 0.6 to 2.4 meters in diameter) that establishes bidirectional satellite communication. It's particularly useful in remote areas where terrestrial networks (e.g., fiber, 4G/5G) are not available. A VSAT terminal communicates with a satellite in geostationary orbit (GEO), which relays the signal to a hub (or gateway) that makes the link with the Internet. VSAT is used in applications such as rural connectivity, maritime and aeronautical communications, and enterprise networks.

## Wireless M-Bus (WM-Bus)

Wireless M-Bus is an open standard (EN 13757-4) optimized for automatic reading of meters such as heating meters or water consumption meters. It operates over free bands such as 868 MHz, and it's designed to last for a long time (up to 10 years). It works with a star topology where it periodically sends its data to the gateway. Furthermore, it's always the meter who sends the data to the gateway, never the opposite. The WM-Bus range is around 40 meters indoors and 800 m outdoor in free field.

## WSN

Wireless Sensor Networks, a WSN is a self-organized collection of small physical devices called nodes. They work together to monitor an environmental phenomenon such as temperature, humidity, vibration, air quality etc. Most of the time these nodes aren't plugged to the grid so are energy-constrained. Nodes send their data using **radio frequency links** to one or several sinks that make the link between the WSN and another network such as internet. The sink can be fixed or mobile. Nodes can also be mobile for fauna monitoring for example.

## WSN-MS

Wireless Sensors Network with Mobile Sinks.

## WuR

Wake up Radio, low-energy radio in order to listen and wake up the sensor when a mobile sink comes close. No payload data will be transmitted through this radio, its only role is to be able to wake up the sensor during its sleeping cycle.
