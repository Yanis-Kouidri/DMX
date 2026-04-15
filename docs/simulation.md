# Simulation

This page sum up major simulation tool for networking purpose.

## NS-3

NS-3 stands for Network Simulation 3. It's a free open source software. It's widely used for research. There is no graphic interface, everything must be written in code.

NS-3 is written in C++ and python. It has a big community of developers who produce plugins for specific usage.

### Links

- [Website](https://www.nsnam.org/)
- [GitLab](https://gitlab.com/nsnam/ns-3-dev/)
- [Docs](https://www.nsnam.org/documentation/)

## OMNeT++

OMNeT++ stand for Objective Modular Network Testbed in C++. It's open source and free for academic usage. It comes with a graphical interface (Qtenv). The OMNeT++ IDE is based on eclipse.

OMNeT++ is divided in 3 parts:

- The NED (Network Description) that define the topology and the interconnection between equipments (computer, switch, router, etc.)
- The C++ that define the behavior of equipments such as router
- The .ini `file` who define the simulation parameter such as duration, the Wi-Fi signal strength, etc.

OMNeT++ is used for WSN with the framework Castalia

### Links

- [Website](https://omnetpp.org/)
- [GitHub](https://github.com/omnetpp/omnetpp)
- [Docs](https://omnetpp.org/documentation/)

## Cooja

Cooja stand for Contiki OS Java Simulator

Cooja is specialized in IoT simulation. It provides different views, allow exporting packet for a Wireshark analysis. Plus, it allows measuring energy consumption thanks to Energest.

Cooja is free and open-source.

### Links

- [Website](https://www.contiki-ng.org/)
- [GitHub](https://github.com/contiki-ng/cooja)
- [Docs](https://docs.contiki-ng.org/en/develop/)

## CupCarbon

CupCarbon is a simulation tool for IoT and Smart Cities. It's rely on a visual approach by opposition with NS-3 and OMNeT++.
It's open-source and free.

CupCarbon a made in France tool by l'Université de Bretagne Occidentale.

### Links

- [Website](https://cupcarbon.com/)
- [GitHub](https://github.com/bounceur/cupcarbon)
- [Docs](https://cupcarbon.com/CupCarbon-Tutorials_7.html)

## Mininet-WiFi

Mininet-WiFi is an extension of Mininet for wireless connection. It works mainly with python and has graphical interface to visualize in real time the simulation.

### Links

- [Website](https://mininet-wifi.github.io/)
- [GitHub](https://github.com/intrig-unicamp/mininet-wifi)
- [Docs](https://mininet-wifi.github.io/)

## STK

STK stands for System Tool Kit, it's a tool developed by AGI (Analytical Graphics, Inc.) that allow to modelize complex systems with satellites, planes, sensors, cars, etc. It can predict position of a satellite at an instant T, check if a signal can pass through a mountain or a building, compute link quality and some other think.

It cost up de 100 000 € so not interesting for research.

### Links

- [Website](https://www.ansys.com/fr-fr/products/missions/ansys-stk)

## OpenSatKit

OpenSatKit is an open source software to modelize satellites communication. To make a long story short, OpenSatKit is the free alternative of STK.

### Links

- [Website](https://opensatkit.github.io/)
- [GitHub](https://github.com/OpenSatKit/OpenSatKit)
- [Docs](https://opensatkit.github.io/docs/)

## ONE

ONE stand for Opportunistic Network Environment simulator. It's a simulator specialized in DTN simulation. ONE is not actively maintained but can still be useful for specific scenario including DTN.

It provides a real time GUI to see packet mobility.

The [original paper](https://www.netlab.tkk.fi/tutkimus/dtn/theone/pub/the_one_simutools.pdf) introducing the ONE software has received over 3,000 citations.
Its name is: *The ONE simulator for DTN protocol evaluation*.

### Links

- [Website](https://akeranen.github.io/the-one/)
- [GitHub](https://github.com/akeranen/the-one)
- [Docs](https://akeranen.github.io/the-one/)
