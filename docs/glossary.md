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

## Duty-cycling

In case of a sensor, it's a technic to alternate between wake and sleep cycle in order to save battery instead of being always wake. However, during sleep cycle sensor cannot sense neither communicate through radio.

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

Low Power Wide Area Network, network using long range and low power wireless communications such as LoRaWan, LTE-M, NB-IoT, Sigfox.

## RSSI

Received signal strength indicator, power of received signal by an equipment, often measure in dBm.

## NB-IoT

## 3GPP

## LTE-M

## Sigfox

## ISM bands

## SNR

## Spreading Factor (SF)

## mMTC

## ATSSS

## MPTCP

## ATSSS-LL

## Matter

## CSA

## MNT

## PDR

## FLB

## Stochastic

## TOPSIS

## RODENT

## Uruha

## ATSR

## Hop-by-hop routing

## Source routing
