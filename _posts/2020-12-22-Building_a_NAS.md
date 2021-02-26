---
title: Building a NAS
image: /assets/img/NAS_rig.jpg
---

For long time I wanted to purchase a NAS. However, I never really found a device I liked. Either the OS was not fitting for my purposes or the hardware was to poor for the given price, which made me build a NAS on my own. Since electricity prices in Germany are one of the highest in Europe, I of course had a focus on low power consumption.

![NAS_rig](/assets/img/NAS_rig.jpg)

I build all this in an old PC case with the following components:

Parts:
* Mainboard, CPU, GPU (ASRock J4105M): [On Amazon](https://www.amazon.de/dp/B079GHR8L9/?coliid=I30FJ9H85WD60&colid=2BK8UBXGGIG6X&psc=1&ref_=lv_ov_lig_dp_it)
* 120 GB SSD (Kingston SV300S37A): [On Amazon](https://www.amazon.de/dp/B00A1ZTZOG/ref=twister_B00LA3SM10?_encoding=UTF8&psc=1)
* 2x 4GB RAM (Corsair Vengeance LPX DDR4 2400MHz): [On Amazon](https://www.amazon.de/dp/B019HVND88/?coliid=IDRBDE53P9ZE&colid=2BK8UBXGGIG6X&psc=1&ref_=lv_ov_lig_dp_it)
* PCIe SATA-Card (4 Ports, 6-Gbit/s-SATA 3.0): [On Amazon](https://www.amazon.de/dp/B07T8XNQT6/?coliid=I19X81MXIILA1G&colid=2BK8UBXGGIG6X&psc=0&ref_=lv_ov_lig_dp_it)
* 2x HDD (WD Red 4 TB, 5400 U/min, SATA 6 Gbit/s): [On Amazon](https://www.amazon.de/dp/B083XVY99B/?coliid=ITRJO66DRNE8X&colid=2BK8UBXGGIG6X&psc=1&ref_=lv_ov_lig_dp_it)
* OS ([OpenMediaVault](https://www.openmediavault.org/))

Power consumption:
* Idle without HDDs: 10W
* Idle with HDDs: 18W

Configuration:
* SSD connected on Mainboard SATA
* Both HDD connected to PCIe Card on IDE-Boot

