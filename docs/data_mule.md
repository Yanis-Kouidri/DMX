# Data mule

## Why data mule ?

**Hot spot issue**: In traditional WSN, a single fix sink collects data from all sensor. This situation creates the *Hot Spot Problem* or *Energy Hole Problem*. Because the sink is fixed, all data converge to few sensors near the sink to reach it, so these sensors batteries die prematurely compared to sensors in border of the network. No matter which architecture is used to define the WSN (cluster, tree or mesh), the problem remains the same. To address this issue, an option is to make the sink become mobile using data mule for example. This solution can spread the data collection load over the entire network.
