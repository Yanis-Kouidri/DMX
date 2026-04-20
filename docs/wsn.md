# WSN

## Metrics

### Energy consumption metrics

- **Duty Cycle**: The ratio of time a node is active versus the time it is in sleep mode.
- **Average Energy Consumption**: The total energy consumed by all nodes divided by the number of nodes over a specific period.
- **Energy per Successful Data Packet**: The total energy spent (including overhead, retransmissions, and idle listening) to deliver one unit of payload.
- **Residual Energy**: The remaining battery power in each node. This helps identify "hotspots" where nodes are dying faster than others.

### Network lifetime metrics

- **First Node Dead (FND)**: The time elapsed until the first sensor node runs out of energy.
- **Half of Nodes Alive (HNA)**: The time until 50% of the nodes have depleted their batteries.
- **Last Node Dead (LND)**: The time until the entire network becomes non-functional.
- **Sensing Coverage Lifetime**: The duration for which the network can monitor a specific percentage of the target area.

### Reliability and Quality of Service (QoS)

- **Packet Delivery Ratio (PDR)**: The ratio of packets successfully received by the sink (gateway) to the total packets sent by the source nodes.
- **Packet Loss Rate**: The percentage of packets dropped due to collisions, interference, or buffer overflows.
- **Bit Error Rate (BER)**: The number of bit errors divided by the total number of transferred bits during a studied time interval.
- **Throughput**: The amount of data successfully moved from source to destination in a given time, usually measured in bits per second (bps).

### Temporal Metrics (Latency)

- **End-to-End (E2E) Delay**: The time taken for a packet to travel from the sensing node to the sink. This includes queuing, processing, and transmission delays.
- **Jitter**: The variation in the delay of received packets. High jitter can be problematic for real-time monitoring.
- **Settling Time**: The time required for the network to become fully operational after deployment or a major topology change.
- **Age of Information (AoI)**: This is currently a high-impact metric in research. It measures the "freshness" of the data at the receiver. Unlike delay, which starts when a packet is sent, AoI increases until a new update is received.

### Topological and Spatial Metrics

- **Sensing Coverage**: The fraction of the target area monitored by at least one sensor node.
- **Connectivity**: The ability of nodes to reach the sink through single or multi-hop paths.
- **Node Density**: The number of nodes per unit area. Higher density can improve reliability but increases the risk of signal collisions.
- **Network Scalability**: A measure of how the PDR and Latency are affected as the number of nodes increases from tens to thousands.
