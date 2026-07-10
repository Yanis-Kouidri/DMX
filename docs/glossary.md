# Glossary

## DTN

 Delay Tolerant Network, DTN is a specific type of network architecture to operate where there is no guarantee of end to end communication such as on Intermittently Connected Networks (ICN). Whereas regular networks such as Internet will just drop a packet if the next hop is not connected, DTN will use the mechanism of **store-carry-and-forward** to transmit a packet when the next hop will be reachable. A node will receive data from another node, wait a time form minutes to days then, once connection is established, forward the packet to the next node. DTN use **bundle layer** on top of transport layer acting as an overlay.

## Bundle layer

 Bundle layer is used in DTN to perform **store-carry-and-forward**. It sits between application layer and lower-level networking layer. Whereas regular networks such as Internet, application layer (e.g., HTTP) talk directly to transport layer (e.g., TCP), DTN add bundle layer with bundle protocol and **Convergence Layer Adapters** (CLA). CLA enable **Bundle Protocol** to run on top of anything (e.g., TCP, UDP, CCSDS, Data mule).

## CLA

 Convergence Layer Adapter, the CLA act like glue between Bundle Protocol and anything under. Bundle Protocol is designed to be **agnostic**. The role of CLA is to encapsulate, manage connection, discover neighbor and sometimes add reliability. It exists different CLA such as TCP CLA, Bluetooth/BLE CLA, LTP CLA and HTTP/Web CLA.

## Data mule

 Data mule is a mobile node such as a person, a bus, a drone, etc. It carries physically the data from a source to a destination. It's particularly convenient in remote area where direct wires and wireless (e.g., 5G, 4G) communication are not possible.

## NTN

 Non-Terrestrial Network, NTN is a telecommunication system that uses spaceborne or airborne vehicle such as satellite or HAPS to transmit signals, rather than relying on traditional ground-based cell towers. It becomes handy in places where traditional networks are impossible to set up such as deep forest, ocean, remote area and high-altitude. NTN rely on LEO (Low Earth Orbit), MEO (Medium Earth Orbit) and GEO (Geostationary) satellites. It also relies on HAPS (High-Altitude Platform Stations).

## WSN

 Wireless Sensor Networks, a WSN is a self-organized collection of small physical devices called nodes. They work together to monitor an environmental phenomenon such as temperature, humidity, vibration, air quality etc. Most of the time these nodes aren't plugged to the grid so are energy-constrained. Nodes send their data using **radio frequency links** to one or several sinks that make the link between the WSN and another network such as internet. The sink can be fixed or mobile. Nodes can also be mobile for fauna monitoring for example.

## UAV

 Unmanned Aerial Vehicle, UAV are most commonly named drone. It's an aircraft that operates without human on board. However, it can be controlled remotely by a human pilot or flight autonomously by onboard computers and pre-programmed flight plans.

## Opportunistic routing (OR)

 Opportunistic routing is an approach to move data through a network using broadcast nature of wireless communications. In traditional routing approach. A single path is defined between source and destination and used to carry data. That works well and reliable infrastructure such as cable but in wireless communication, a link can fail. Therefore OR uses a candidate set of potential forwarders. It works in three step :

1. **Broadcast**: The sender broadcasts the data packet. Any neighbor in the “candidate set” that successfully receives it becomes a potential relay.
2. **Coordination**: The nodes that heard the message talk to each other (or use timers) to decide who is in the best position to move the data closer to the destination.
3. **Forwarding**: The “best” node (usually the one closest to the target) forwards the packet, and the other nodes discard their copies to avoid duplicates.

This approach is implemented in different protocol such as ExOR, MORE, EPIDEMIC, PROPHET etc.

## NDN

 Named Data Networking, in regular network such as IP, to access a data, you use its location, the where. In NDN, to get a data, you specify what you want, no matter where it is. There are neither source nor destination address, just interested data. Each NDN router record which port request which data on its Pending Interest Table (PIT) and forward it to the next interface using FIB (Forwarding Information Base). Router can cache data previously requested.

## HAPS

 High-Altitude Platform Stations, HAPS are unmaned vehicles that hover in the stratosphere, roughly 20 km above the Earth. It can be solar-powered drone or giant balloons.

## LoS

Line of Sight, in telecommunication, LoS refers to a clear and unobstructed path between the transmitter and the receiver antenna.

## DOP

Dilution Of Precision, In context of GNSS and wireless positioning, DOP is a mathematical value that represents the quality of geometry depending on anchors (such as satellites or UAV) position. When anchor are spread all around the user, geometry is good so DOP is low. If anchors are clustered close together or on a same line, geometry is poor, so DOP is high and the computed position of user is uncertain.

## Wireless M-Bus (WM-Bus)

Wireless M-Bus is an open standard (EN 13757-4) optimized for automatic reading of meter such heating meter or water consumption meter. It operates over free bands such as 868 MHz, and it's design to last for a long time (up to 10 years). It works with a star topology where it sends periodically his data to the gateway. Furthermore, it's always the meter who sends the data to the gateway, never the opposite. The WM-Bus range is around 40 meters indoors ans 800m outdoor in free field.

## Duty-cycling (sleep/wake up)

In case of a sensor, it's a technic to alternate between wake and sleep cycle in order to save battery instead of being always wake. However, during sleep cycle sensor cannot sense neither communicate through radio.

## Regulatory Duty-cycle

It can also refer to legal regulations that restrict a device's transmission time on free frequency bands (e.g., limiting transmission to no more than 1% of the time) to prevent network congestion.

## WuR

Wake up Radio, low-energy radio in order to listen and wake up the sensor when a mobile sink come close. No payload data will be transmitted through this radio, its only role is to be able to wake up the sensor during its sleeping cycle.

## SAW sensor

Surface Acoustic Wave sensor, it's a passive sensor (without battery) that can perform a measure and sent back the information only thanks to an electromagnetic wave sent by the collector.

## RFID

Radio Frequency Identification, method to memorize and give back data in a chip without battery.

## RFID UHF

RFID Ultra High Frequency, technology using RFID chip to identify object using UHF bands that allow range until 15 meters.

## RFID NFC

RFID Near Field Communication, technology using RFID chip to communicate on a very short distance (few centimeters). Used in debit card and transport pass for example.

## AUV

Autonomous Underwater Vehicle

## FANET

Flying Ad-hoc Network, drones swarm that communicate together.

## VANET

Vehicle Ad-hoc Network, network of terrestrial vehicles that communicate together.

## MBN

Mobile Backbone Network, mobile communication backbone by opposition of static communication backbone such as 4G/5G antennas.

## LWSN

Linear Wireless Sensor Network, network of wireless sensors arrange linearly.

## MWSN

Mobile Wireless Sensor Network, network of mobile wireless sensors by opposition of fixed sensors.

## WSN-MS

Wireless Sensors Network with Mobile Sinks.

## ETX

Expected Transmission Count, metric that estimate the number of transmission required to send a message over one link at an instant T. ETX = 1 → perfect link, ETX = 2 → 50% of packets are lost, etc.

## CA-ETX

Contact Aware Expected Transmission Count, improvement of ETX metric by taking into account the possibility the link may be cut due to the physical distance. Useful for mobile sink in WSN for example.

## OBC

Opportunistic Backpressure Protocol, routing protocol using CA-ETX metric.

## KNN

K-Nearest Neighbor, algorithm used to identify if a variable or a vector (several variables) is normal or is abnormal (anomaly detection)

## LSTM

Long Short-Therm Memory, IA model to perform prediction

## MEC

Mobile Edge Computing, strategy focussing on binging computational power closer the network border (therefore closer to the user)

## SCA

Successive Convex Approximation, operations research algorithm that allow to transform a complex problem (non-convex) into a simple one (convex)

## LPWAN

Low Power Wide Area Network, network using long range and low power wireless communications such as LoRaWan, LTE-M, NB-IoT, Sigfox. See [Wikipedia](https://en.wikipedia.org/wiki/Low-power_wide-area_network)

## RSSI

Received Signal Strength Indicator, power of received signal by an equipment, often measure in dBm.

## NB-IoT

Narrow Band Internet of Things, is a LPWAN technology developed by the 3GPP for IoT using 4G and 5G bands.

## 3GPP

3rd Generation Partnership Project, organism that standardized mobile networks (3G/4G/5G/6G)

## LTE-M

Long Term Evolution for Machine, LPWAN technology developed by the 3GPP for IoT connection using 4G band (LTE). It provides a good mobility management.

## Sigfox

Sigfox is a proprietary LPWAN technology that works over unlicenced bands. Sigfox is a company that's own it's private network and managed it. The user only has to by a Sigfox antenna and a subscription to the service, then Sigfox relay the received data to an internet endpoint the client choose.

## ISM bands

Industry Science and Medical frequency bands open to used without any prior authorization or license.

## SNR

Signal to Noise Ration, metric to evaluate the quality of a radio link. Higher is better.

## Spreading Factor (SF)

The Spreading Factor is a parameter that defined the ratio between the transmission (throughput) and range. In LoRa, the Spreading Factor is between 7 and 12. At SF7 the throughput is high (~5 kbps) but the range is low (~2 km). At SF12 the throughput is low (~250 bps) but the range is high (+15 km). A high SF (SF12) lead to higher time on air and higher consumption. That's also consume more of the device duty cycle.

## mMTC

mMTC stands for massive Machine Type Communication. It's a type of network that allow huge number of IoT device in the same area such as 1 million by km². It's a core part of 5G and 6G, defined by 3GPP.

## ATSSS

Access Traffic Steering Switching and Splitting, it's a functionality introduced by 3GPP (release 16) to allow User Equipment (UE) to be connected to internet through different access network such as 5G and Wi-Fi.

## MPTCP

Multi-Path Transmission Control Protocol, an extension of standard TCP allowing to use simutiniouslty multiple network paths to reach the destination.

## ATSSS-LL

## Matter

## CSA

## MNT

## PDR

Packet Delivery Ration also called PSR (Packet Success Ration). Network metric to measure how much packet are successfully delivered to the destination compared to the total number of packet sent.

$$
PDR = \frac{Number\ Of\ Packet\ Successufly\ Received}{Number\ Of\ Packet\ Sent} * 100
$$

## FLB

## Stochastic

## TOPSIS

## RODENT

## Uruha

## ATSR

## Hop-by-hop routing

## Source routing

## Mote

A mote is a sensor that have 4 things:

- A sensor equipment to measure a metric such as temperature or humidity.
- A radio module to communicate remotely.
- A source of energy such has battery.
- A microcontroller unit to handle sensing, data transmission and sleep cycle.

Mote are end device on an IoT network.

## ALOHA

ALOHA is a very simple Medium Access Control (MAC) protocol. It works with random access to support, when a station has to transmit it transmit without sensing the channel prior. Collision are frequent, so the reliability rely on ACK messages. In pure ALOHA the maximum throughput is about 18.4% of the channel bandwidth. Pure ALOHA is used in LoRaWAN.

## Machine Learning (ML)

Machine Learning is a branch of Artificial Intelligence (AI) focused on developing systems that can learn from data and improve their performance without being explicitly programmed. Instead of following rigid, hand-coded instructions, ML systems use statistical algorithms to identify patterns and perform feature extraction. This process results in a trained model: a mathematical representation that can generalize from its training to make predictions or automate decisions on new, unseen data (such as performing image classification to distinguish between a dog and a cat).
The learning can be:

- **Supervised Learning**: In this approach, the algorithm is trained on a labeled dataset, where each input is paired with its corresponding correct output (ground truth). The goal is for the model to learn a mapping function that can predict labels for new data. Example: Feeding an algorithm thousands of images tagged "dog" or "cat" so it learns to classify future images.
- **Non supervised Learning**: This paradigm involves training on unlabeled data. The algorithm must independently discover the underlying structure or hidden patterns within the data. Primary Technique: **Clustering**, which groups data points based on shared characteristics or features (e.g., grouping photos by visual similarity without knowing what the objects are).
- **Reinforcement Learning (RL)**: This is an agent-based learning method where a system learns to achieve a goal in a dynamic environment through trial and error. The agent receives feedback in the form of rewards or penalties based on the actions it takes, allowing it to optimize its strategy (policy) over time.

Traditional programming uses Rules + Data = Answers. Machine Learning flips the script: Data + Answers = Rules.

## Deep Learning (DL)

In traditional ML, humans perform Feature Engineering. You have to identify the most important characteristics of the data before feeding it into the algorithm. If you choose the wrong features, the model won't work well, regardless of how good the algorithm is.  
Deep Learning uses Artificial Neural Networks with many layers (hence the "Deep") to perform by itself the feature extraction. It requires massive amounts of data, GPUs and can take days or weeks to train.  
Whereas classical ML is excellent for Structured Data (things you find in Excel sheets or SQL databases). Deep Learning excels at Unstructured Data, which is data that doesn't fit neatly into a table.

## Agent

In AI, an Agent is a system that can **perceive** its environment and take **actions** to achieve a specific goal.  
Examples:

- Physical Agent: A Roomba vacuum. Its goal is to clean the floor. Its sensors (bumpers/lasers) provide the observations, and its motors provide the actions.
- Digital Agent: A trading bot on the stock market. Its goal is profit. Its observations are stock prices, and its actions are buy/sell orders.
- AI Agent (LLM-based): A tool that you ask to "Book a flight." It doesn't just talk about flights; it actually goes to websites, searches for dates, and interacts with the booking system until the task is done.

## Feature extraction

Feature extraction is the process to extract key characteristics from raw data for the computer to use them to take decision. Example: for dog Vs. cat model, feature could be shape, size and textures.  
In ML, it is to the user to extract features. This is called feature engineering. In DL it's the role of the neural network.

## Neural network

A neural network is a digital imitation of the human brain. It is composed of several layers of neurons where each neuron takes several inputs, calculates their importance, and decides if it should "fire" a signal to the next layer. The final layer gives you the answer (e.g., "98% Dog, 2% Cat"). Each neuron has weights that represent the importance of an input. These weights are initially random and thanks to feedback weight are adjusted.

## Adaptative Date Rate (ADR)

Adaptive Data Rate (ADR) is a radiocommunication concept where the data rate is dynamically adapted depending on radio link metrics. Basically, if the radio link is bad, the ADR mechanism will reduce the data rate in order to successfully reach the destination. Conversely, if the radio link is good, it will raise the data rate.

## End device, end node

In an LPWAN context, an end device (or end node) refers to IoT device and are connected to one or several gateways.

## SCHS

SCHC stands for Static Context Header Compression and Fragmentation ([RFC 8724](https://datatracker.ietf.org/doc/html/rfc8724)). It enables resource-constrained IoT devices to connect to the Internet over Low-Power Wide-Area Networks (LPWAN). It works by compressing large network headers (like IPv6/UDP) over the constrained radio segment between the sensor and a gateway. Both the sensor and the gateway share a pre-configured Static Context (a set of rules). Instead of transmitting the full header, the sensor only sends a short Rule ID, allowing the gateway to fully reconstruct the original Internet packet.
