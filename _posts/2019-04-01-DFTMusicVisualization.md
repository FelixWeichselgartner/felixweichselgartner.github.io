---
title: DFT Music Visualization
image: /assets/thumbnails/DFTMusicVisualizationThumbnail.png
---

[GithubRepository](https://github.com/FelixWeichselgartner/DFTMusicVisualization)

This project is a music visualization with discrete fourier transformation on four rgb-led-matrices.

Here is a GIF of my result:

![GIF from GitHub Readme](https://raw.githubusercontent.com/FelixWeichselgartner/DFTMusicVisualization/master/resources/MyOutput.gif)

This program runs on a RaspberryPi 3B+ on Python. In the repository is also a C version, however I still having some trouble with the sound input there.

Here is a basic diagram of the function principle:

3.5mm Audio-Jack -> USB-Soundcard -> ALSA -> Python-script -> rpi_ws281x -> rgb-matrices

Basically I give an audio signal to the microphone input of my USB-Soundcard. With the ALSA (Advanced Linux Sound Architecture) library ([pyalsaaudio][https://github.com/larsimmisch/pyalsaaudio]) I can read the data from the soundcard. The soundcard samples 16-bit singed integer with a sampling rate of 44100Hz (normal CD quality). The here received data is then transformated with, my self implemented, discrete fourier transformation (acutally fast fourier transformation). As humans are only to hear from 20Hz to 20kHz, all frequencies higher than 20kHz are cut off and then formatted to a matrix fitting size. With the [rpi_ws281x][https://github.com/jgarff/rpi_ws281x] I was then able to display the fourier transformed signal to the matrices.

## What I Learned

* implementation of fourier transformation
* controlling led matrices with raspberrypi/arduino
* using CMake
* function principle behind audio files
* sampling audio files
* working with ALSA (Advanced Linux Sound Architecture)
