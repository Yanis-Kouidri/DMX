# Glossary

**DTN**: Delay Tolerant Network, DTN is a specific type of network architecture to operate where there is no guarantee of end to end communication such as on Intermittently Connected Networks (ICN). Whereas regular networks such as Internet will just drop a packet if the next hop is not connected, DTN will use the mechanism of **store-carry-and-forward** to transmit a packet when the next hop will be reachable. A node will receive data from another node, wait a time form minutes to days then, once connection is established, forward the packet to the next node. DTN use **bundle layer** on top of transport layer acting as an overlay.

**Bundle layer**: Bundle layer is used in DTN to perform **store-carry-and-forward**. It sits between application layer and lower-level networking layer. Whereas regular networks such as Internet, application layer (e.g., HTTP) talk directly to transport layer (e.g., TCP), DTN add bundle layer with bundle protocol and **Convergence Layer Adapters** (CLA). CLA enable **Bundle Protocol** to run on top of anything (e.g., TCP, UDP, CCSDS, Data mule).

**CLA**: Convergence Layer Adapter, the CLA act like glue between Bundle Protocol and anything under. Bundle Protocol is designed to be **agnostic**. The role of CLA is to encapsulate, manage connection, discover neighbor and sometimes add reliability. It exists different CLA such as TCP CLA, Bluetooth/BLE CLA, LTP CLA and HTTP/Web CLA.

**Data mule**:

**NTN**:

**WSN**:

**UAV**:

**Opportunistic routing**:
