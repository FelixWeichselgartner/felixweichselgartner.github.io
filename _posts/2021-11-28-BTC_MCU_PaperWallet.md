---
title: Microcontroller based Private/Public key generation
image: /assets/img/btc_top_led.jpg
---

You ever felt unsafe creating a Bitcoin wallet on your desktop computer or on your smartphone? As such devices are often connected to the internet there might be a chance you have already been hacked and somebody could be stealing your private key(s). The solution is to create your private keys on a device that cannot be hacked because it is not connected to any other devices (e.g. no internet, ...).
This project aims for a microcontroller-based private key generation. The private key will be generated using rng. Your bitcoin address will then be calculated from your private key. Both will then be displayed on a display, for you to transfer on a piece of paper, which you will keep safe. You can now use the address to transfer your bitcoins. Once you need your bitcoins, you simply import your private key in a wallet program and for safety reasons create a new paper wallet with this device. You can then use the bitcoins you need and transfer the rest to your new save bitcoin address.
All the code and schematics are Open Source and can be found on my GitHub:
https://github.com/FelixWeichselgartner/BitcoinOfflinePaperWalletGenerator

Here are some images of the PCB:

![top_led](/assets/img/btc_top_led.jpg)

![top_lcd](/assets/img/btc_top_lcd.jpg)

![bottom](/assets/img/btc_bottom.jpg)
