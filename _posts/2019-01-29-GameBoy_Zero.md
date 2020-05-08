---
title: GameBoy Zero
image: /assets/thumbnails/GameBoyZeroThumbnail.png
---

## Teile:

Das Gehäuse des GameBoy Classic:

![](/assets/img/5584f59d-0614-4cf3-87d0-e8e3191522d8.jpg)

![](/assets/img/44dc4d00-387b-4f61-9676-7b3babc4399b.jpg)

Rückfahrbildschirm für ein KFZ:

![](/assets/img/49f83f94-29de-4908-b278-8278efcc4dde.jpg)

Entgegen meiner Erwartung war es bei dem Modul auf der Rückseite des Displays nicht möglich einen Spannungswandler von 12V auf 5V auszulöten. Aus diesem Grund habe ich 2 Spannungswandler gebraucht.

![](/assets/img/ca122b58-c53d-4c96-b788-8d2d7926f13d.jpg)

Der Spannungswandler für den Bildschirm:

![](/assets/img/5e5dc5d0-5efc-4a40-b780-76318a99b8c7.jpg)

Die Button-PCB, die bei Knopfdruck die Leiterbahnen kurzschließt:

![](/assets/img/d2267bd7-a2cb-4896-aa49-5c8575e4cd3f.jpg)

Lithium Polymer Batterie mit 2700mAh und 3,7V und ein dazu passendes Lademodul (Kurzschlussschutz, Überladeschutz, Überentladeschutz) mit maximal 1A Ladestrom:

![](/assets/img/2979b308-903a-4b5e-846b-ae116e21073b.jpg)

RaspberryPi Zero W mit 32GB Micro-SD-Karte:

![](/assets/img/4da128ee-5874-4751-9ab5-536ecbace6a3.jpg)

![](/assets/img/bcdc1e48-8682-4f34-b95f-7021927b3043.jpg)

PAM8403 Audio Verstärker mit 2 x 3W auf Breakout-Board:

![](/assets/img/27d2e0ce-35ec-42c2-83ed-e83db38b648e.jpg)

Eine Auswahl von Tastern für L- und R-Buttons (die linken 2 wurden am Ende verwendet):

![](/assets/img/4f62fcfd-b89a-432c-a7e1-b8aee6edc935.jpg)

Spannungswandler für RaspberryPi und Audio Verstärker, 2-Kanal-Potentiometer, Headphone-Jack und L-R-Button eingelötet auf Platine zum einkleben:

![](/assets/img/267aa382-c7ac-4131-8ca2-35c020803808.jpg)

## Installation von RetroPie:

Download der Software hier: [RetroPie.org](https://retropie.org.uk/)

Ich empfehle die folgenden Schritte an einem HDMI-Bildschirm mit Tastatur auszuführen.

SSH aktivieren

Dazu in folgendes Verzeichnis gehen und die Datei zum bearbeiten öffnen:

`/boot/config.txt`

Die folgenden Zeilen am Ende der Datei einfügen:

`controllers.gpio.enabled = 1`

`dtoverlay=pwm-2chan, pin=18, func=2, pin2=13, func2=4`

Wenn das Display wie bei mir um 180° gedreht werden soll:

`lcd_rotate = 2` 

Benutzen der GPIO-Pins für die Buttons:

Diese Datei downloaden, um Button über die GPIO-Pins abfragen zu können:

[https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/retrogame.sh](https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/retrogame.sh)

Dann in der Konsole ausführen mit:

`sudo bash retrogame.sh`

Wechsle in dieses Verzeichnis:

`/boot/retrogame.cfg`

Hier selbst verwendeten GPIO-Pins eingeben.

Zum ändern der Schriftgröße:

`/etc/emulationstation/themes/carbon/carbon.xml`

## Hardware:

Ein-/Ausschaltswitch:

![](/assets/img/9de4f8ed-0995-4183-ace8-76933d4d5908.jpg)

Schablone zum Bohren der Löcher für X-Y-Button:

![](/assets/img/e23485e2-e980-49a3-8c5f-cc4d951226f9.jpg)

Bohren der Löcher mit einem Stufenbohrer:

![](/assets/img/3e660c08-caa1-4f50-a38d-81f65fb0b8f2.jpg)

Endergebnis der Ausgebohrten Löcher:

![](/assets/img/a29cf249-47ef-4278-831c-c2434e764008.jpg)

Display mit Heißklebepistole eingeklebt und Button eingesetzt:

![](/assets/img/3280db19-8364-4655-8e27-12a38afe36b1.jpg)

Displayschutz aus dem Displayschutz des KFZ-Gehäuses:

![](/assets/img/41986d45-6bef-46ab-b5b6-d656e0b52901.jpg)

Button-Pads eingesetzt:

![](/assets/img/de95db75-a5c1-4f2f-ae63-322bac53ecc9.jpg)

Button-PCB eingesetzt:

![](/assets/img/c511bb55-c6d4-4347-a009-9b4675e83da1.jpg)

Vorderansicht ohne Displayschutz:

![](/assets/img/d3562cd7-67f7-4133-8b0d-488cb13c57b9.jpg)

Erster Test des Displays und der Buttons:

![](/assets/img/dbdfb90f-4ce4-4b16-ae07-9530cbe6534a.jpg)

Montage der L- und R-Buttons:

![](/assets/img/226df5c9-0c76-4f18-9b33-8b8d8c6e7c84.jpg)

Montage der LiPo-Akkus:

![](/assets/img/05af129b-b30d-4604-8493-4bcaec6e9dc6.jpg)

Ladetest mit Ladeplatine und LEDs:

![](/assets/img/e0951201-3c55-4f05-82e0-4657addfbe2b.jpg)

Erster Test nach dem Zusammenbauen von Vorder- und Rückseite:

![](/assets/img/6e44639a-0021-4714-b72b-14565957ca0a.jpg)

Empfindliche Stellen mit Klebeband überklebt, um einen Kurzschluss zu vermeiden:

![](/assets/img/588c948e-1f37-44e7-90fb-bec979c17f92.jpg)

Der GameBoy beim Aufladen:

![](/assets/img/001dd5b6-03f5-4e9e-9cee-61408498e30f.jpg)

Aufgeladener GameBoy:

![](/assets/img/b6d37a82-97bd-4486-bef8-c58f81199ccd.jpg)

Audio-Schaltung:

![](/assets/img/a7ece063-2e37-4ca5-a74a-78e6404a2c0e.jpg)

Audio-Ausgabe auf dem Oszilloskop:

![](/assets/img/c74d125a-c5a3-47c7-abd4-d776824a9eca.jpg)

USB-Port, Lautsprecher, 2-Channel-Potentiometer und Audioverstärker eingebaut:

![](/assets/img/362b36ad-dfed-4984-981d-70af74017373.jpg)

Das Endergebnis:

![](/assets/img/498b9cd3-4988-495c-aa20-c14e9a7cc934.jpg)
