---
title: GameBoy Cartridge Reader/Writer
image: /assets/thumbnails/GameBoyCartridgeReaderThumbnail.png
---

[GitHub-Repository](https://github.com/FelixWeichselgartner/GB-Cartridge-Reader-Writer)

The project is based on this [tutorial](https://www.insidegadgets.com/2011/03/19/gbcartread-arduino-based-gameboy-cart-reader-%E2%80%93-part-1-read-the-rom/) from insideGadgets.

After drawing my schematics in [Eagle](https://www.autodesk.de/products/eagle/overview), I etched my PCB like shown in these videos:

<iframe width="420" height="315"
src="https://www.youtube.com/embed/YJgX9Na4rWw">
</iframe>

<iframe width="420" height="315"
src="https://www.youtube.com/embed/6uInan-TjiA">
</iframe>

My PCB before etching looked like this: 

![](/assets/img/CartridgeReader_pre_etching.jpg)

This is after etching:

![](/assets/img/CartridgeReader_raw_top.jpg)

![](/assets/img/CartridgeReader_raw_bottom.jpg)

This is the top side of my circuit board:

![](/assets/img/CartridgeReader_top.jpg)

And here the bottom side:

![](/assets/img/CartridgeReader_bottom.jpg)

With this self-build Arduino Uno shield I dumped my cartridge of Yoshi's Cookie (MBC1) and I was later able to play it on my own Emulator:

![](/assets/img/Yoshis_Cookie.bmp)

However, so far I was not able to dump games with MBC5 (like the Pokémon games).

To see how I solved this problem, jump the [second part](https://felixweichselgartner.github.io/2020/11/28/GB_Cartridge_Reader_Writer_continued.html)
