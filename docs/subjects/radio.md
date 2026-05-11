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

## Radio waves

Officially, radio wave are electromagnetic waves between **3 Hz and 3 GHz**. Between 3 GHz and 300 GHz it's microwave. However, 5 GHz Wi-Fi is still considered as radio waves.

The energy of a photon in an electromagnetic wave is :
$$
E = h \cdot f
$$

Where:

- $E$: The energy of the photon in Joules ($J$)
- $h$: The Planck constant in $J\cdot s$
- $f$: The frequency in Hz ($s^{-1}$)

The frequency and the wave length are linked according to this equation:
$$
c = \lambda \cdot f
$$

Where:

- $c$: The celerity of the light ($m \cdot s^{-1}$)
- $\lambda$: The wave length in meter ($m$)
- $f$: The frequency in Hz ($s^{-1}$)
