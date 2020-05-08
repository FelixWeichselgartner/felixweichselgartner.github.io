---
title: GameBoy Classic Emulator
image: /assets/thumbnails/GameBoyClassicEmulatorThumbnail.png
---

[GitHub Repository](https://github.com/FelixWeichselgartner/GameBoy-Classic-Emulator)

For a while I have been thinking about creating an Emulator for one of my most beloved handheld systems. I started this project in the beginning of March 2019, when I underestimated the amount of lines of codes for this to work. However I kept working on it. Hint: currently 6755 lines of code (2020-05-08).

All CPU instructions are implemented correctly, as my emulator is passing Blargg's cpu_instrs test.

![](/assets/img/04b0382e-acc7-4381-b469-3ba1b6c15255.png)

Furthmore all CPU instructions all handled with the right timing, as my emulator is passing Blargg's instr_timing (2019-05-18).

![](/assets/img/1b7c192f-0c23-49eb-86da-9db3dd4a832a.png)

### Achievements so far:

#### Passing Blargg's halt_bug test rom:

![](/assets/img/5cd5efaf-c9b8-4b57-b3fa-1b48d2111440.png)

#### Pokémon Yellow:

The main menu of the game:

![](/assets/img/Yellow_0.bmp)

Selection of the saved game:

![](/assets/img/Yellow_1.bmp)

Saved game was loaded:

![](/assets/img/Yellow_2.bmp)

Pokémon in team:

![](/assets/img/Yellow_3.bmp)

This game is saving properly and loading the saved game back in. The game is based on MBC5, which is most likely implemented properly.

#### Pokémon Red:

![](/assets/img/Red_0.bmp)

#### Tetris - Loading Screen:

![](/assets/img/a71e0f5e-81b3-4aa6-aa23-17d5fcbc632f.png)

#### Tetris - Menu:

![](/assets/img/d9b76f5c-2be8-40a9-8e88-b27dfd0c60cb.png)

#### Dr. Mario - Menu:

![](/assets/img/b0f8e811-818d-40a7-a315-71f117d49859.png)

#### Minesweeper - Loading Screen:

![](/assets/img/95c2a7ea-0ff0-4ade-8f10-78f52beb46c9.png)

#### Minesweeper - Menu:

![](/assets/img/28f172f9-5700-450e-9dea-bae4d31cc402.png)

#### Asterix - Loading Screen:

![](/assets/img/49902649-a70e-41b4-967a-a8451a040fcc.png)
