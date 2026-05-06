# Radio

This section describes how radio links works.

## Link budget

Link budget defines how far your signal can go taking into account powers, gains, and losses.

Here is the equation
$$
P_{RX} = P_{TX} + G - L
$$

Where:

- $P_{RX}$: Received Power
- $P_{TX}$: Transmitter Output Power
- $G$: Total Gains (Antennas, amplifiers)
- $L$: Total Losses (Cables, distance, obstacles)

For a transmission to be received, the $P_{RX}$ must be greater than the receiver sensitivity.
