---
title: GameBoy Cartridge Reader/Writer continued
image: /assets/thumbnails/GameBoyCartridgeReaderThumbnail_continued.png
---

[GitHub-Repository](https://github.com/FelixWeichselgartner/GB-Cartridge-Reader-Writer)

If you have not seen the [first part](https://felixweichselgartner.github.io/2019/09/01/GB_Cartridge_Reader_Writer.html) then check this out first.

Because of a project im doing, in my first master semester of electrical engineering in the module embedded autonomous systems, I will be needing a working Cartridge dumper (a post on the project will be following). Therefore, I wanted to reuse the code from my Arduino shield cartridge dumper. However, I wasn't able to dump MCB5 roms, with it yet. So I was left to guess whether it was a hardware or a software issue...

Now my goal was to measure the voltage (or rather state) on every pin, but using a multimeter to measure the different states of 27 pins seemed insane for me. This brought me to the idea of using an Arduino Mega was a digital oszilloscope or logic analyzer. However, I was not able to find a properly working project on GitHub yet. This meant I had to create my own, which you can find [here](https://github.com/FelixWeichselgartner/Arduino_Logic_Analyzer). Another problem was that there was no proper way to connect all the pins to the Arduino Mega. To solve this problem, I was able to let a laboratory of my university mill a pcb of a debugging GameBoy cartridge.

![debug_cartridge](/assets/img/GameboyCartridgeDebug.jpg)

With help of this cartridge I was able to create a test bench, by connecting most pins of the cartridge to the Arduino Mega.

![test_bench](/assets/thumbnails/GameBoyCartridgeReaderThumbnail_continued.png)

A simple debug script for the Arduino Uno with the CartridgeShield set all pins to high and low and the Mega read the pin states and send them via the COM port to the computer. This result in a csv-file that can then be interpreted by the plot functionality of the logic analyzer.

![logic_analyer](/assets/img/CartridgeReader_LogicAnalyzer.png)

With this test bench, I was able to detect a missing connection between R26 and the 10K resistor. This basically mean that the WR-pin wasn't connected.

![layout](https://raw.githubusercontent.com/FelixWeichselgartner/GB-Cartridge-Reader-Writer/master/prototype/layout.png?token=AJ66GXZ4LUZLPHZ6WQAJ2S27YLLKW)

By soldering them together, I was able to finally dump MBC5 cartridges and I now know that the hardware was the problem.

Lessons learned: Always measure every pin of a hardware, to avoid wasting time fixing a code with no erros.
