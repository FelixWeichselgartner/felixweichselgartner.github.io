---
title: CNC Milling (PCB) and laser engraving
image: /assets/thumbnails/WSB_engraving.jpg
---

# Laser engraving

Without any modifications:
![bottom](/assets/thumbnails/WSB_engraving.jpg)

# PCB (Isolation) Milling

So far I'm not compeletely successfull, so take the next information with caution.

My settings (so far):
* Tool dia: 0.2
* Cut Z: 0.15
* Travel Z: 0.3
* Feed Rate: 500.0

Tricks:
* For debugging: Start the job in the air with the spindle disconnected if problems with USB occur (twist wires).
* Start the spindle before starting the milling job with bCNC. For me it did not start on its own. 
* Tips from bCNC: https://github.com/vlachoudis/bCNC/wiki/Tutorials:-PCB-101-First-time

Modifications:
* Twist the power wires for the spindle. Otherwise EMI problems can occure on the Serial/USB-Port.
* End stops (3D prints): https://www.thingiverse.com/thing:4101947
* End stops: https://de.aliexpress.com/item/32273125391.html?gatewayAdapt=glo2deu&spm=a2g0o.order_list.0.0.21ef5c5frZflMZ
* [Genmitsu GS-775M](https://www.amazon.de/gp/product/B08DTHDSMV/ref=ppx_yo_dt_b_asin_title_o03_s00?ie=UTF8&psc=1) spindle motor
* Opto coupler to avoid ESD damage to z-probe pin: https://de.aliexpress.com/item/1005002783607885.html?gatewayAdapt=glo2deu&spm=a2g0o.order_list.0.0.21ef5c5frZflMZ
* Wifi plug (with Tasmota flashed): https://de.aliexpress.com/item/32939654903.html?gatewayAdapt=glo2deu&spm=a2g0o.order_list.0.0.21ef5c5frZflMZ

Bits and raw PCBs:
* https://de.aliexpress.com/item/1005002376179274.html?gatewayAdapt=glo2deu&spm=a2g0o.order_list.0.0.21ef5c5frZflMZ
* https://de.aliexpress.com/item/32954527473.html?gatewayAdapt=glo2deu&spm=a2g0o.order_list.0.0.21ef5c5frZflMZ
