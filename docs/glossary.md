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

1. **Broadcast**: The sender broadcasts the data packet. Any neighbor in the "candidate set" that successfully receives it becomes a potential relay.
2. **Coordination**: The nodes that heard the message talk to each other (or use timers) to decide who is in the best position to move the data closer to the destination.
3. **Forwarding**: The "best" node (usually the one closest to the target) forwards the packet, and the other nodes discard their copies to avoid duplicates.

This approach is implemented in different protocol such as ExOR, MORE, EPIDEMIC, PROPHET etc.

## NDN

 Named Data Networking, in regular network such as IP, to access a data, you use its location, the where. In NDN, to get a data, you specify what you want, no matter where it is. There are neither source nor destination address, just interested data. Each NDN router record which port request which data on its Pending Interest Table (PIT) and forward it to the next interface using FIB (Forwarding Information Base). Router can cache data previously requested.

## HAPS

 High-Altitude Platform Stations, HAPS are unmaned vehicles that hover in the stratosphere, roughly 20 km above the Earth. It can be solar-powered drone or giant balloons.
