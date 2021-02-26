---
title: Customer Messaging Software
image: assets/img/CustomerMessageSoftware_1.png
---

This is a software I wrote for the company of a relative of mine. It is used to notify customers when their contract expires. This means they will get an e-mail and/or a WhatsApp-Message with the price of the new contract and the experiation date of the old contract. Obviously the e-mail functionality wasn't very hard to program, on the other hand the WhatsApp was quite tricky. I ended up using [Selenium](https://www.selenium.dev/) for this. The complete program is purely written in [Python3](https://www.python.org/).

![QtUI](/assets/img/CustomerMessageSoftware_1.png)

For better useability for non-programmers, I created a graphical user interface with Qt5. Here I could reuse my knowledge I gained from [TetrisQt](http://127.0.0.1:4000/2020/05/08/TetrisQt.html), which I programmed with a couple of friends earlier.

![SQLite3Db](/assets/img/CustomerMessageSoftware_2_database.png)

Generally, the data can either be loaded from a local database (like SQLite3 in this example with [SQLiteStudio](https://sqlitestudio.pl/)) or from [SevDesk](https://sevdesk.de/) (this is a web-based accounting software for germans), via their API. As of today, the software is saving a lot of time, since customers don't have to be contacted individually.

