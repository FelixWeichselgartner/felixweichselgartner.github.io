---
title: My First Website
image: /assets/thumbnails/DjangoWebpageThumbnail.png
---

Alles in diesem Post bezieht sich auf meine erste (nicht diese) Website!

Hier ist die offizielle Website von Django: [DjangoProject.com](https://www.djangoproject.com/)

Django ist ein High-Level Python Web Framework, dass ich bei dieser Website als Backend verwende.

Das Ziel dieser Website war es immer, eine Platform für meine Elektronik- und Softwareprojekte zu bieten. Aus diesem Grund war es für mich wichtig, dass ich eine Art Blog habe, indem ich immer wieder neue Beiträge erstellen kann. 

Dies habe ich mit einem einer Klasse `Post` in der Datei `models.py` geschafft. Diese Klasse erbt von der Klasse `models.Model`, die in Django schon mitgeliefert wird. Hier kann man dann Variablen erstellen für die verschiedenen Attribute die ein (in meinem Fall) Blogeintrag haben soll. Diese kann man später (nach dem registrieren in `admin.py`) leicht über eine vorgefertigte Administratorenseite bearbeiten. Alle meine Blogeinträge werden von Django in einer SQL-Datenbank gespeichert.

Das Schwierigste an diesem Blogeintrag war für mich die Möglichkeit Bilder, Links und Weiteres direkt in den Text einzubinden. Zu erst habe ich in meiner `Post`-Klasse ImageField eingerichtet. Damit konnte ich das erste Mal ein Bild zu einem Blogeintrag speichern. Jedoch konnte ich so diesem Bild keinen speziellen Platz im Text zuweisen. Später habe ich das ImageField dann für das Titelbild verwendet.

Schlussendlich habe ich eine Python-Bibliothek für Django namens [MarkdownX](https://github.com/neutronX/django-markdownx) gefunden. Diese erlaubt es mir statt einem normalen Textfeld ein `MarkdownxField()` zu verwenden. Hier kann man nun mit dem ganz normalen Markdownbefehlen arbeiten. Bilder kann man per Drag-and-Drop in den Text ziehen. Django lädt das Bild automatisch auf einen Ordner auf dem Server hoch und kreiert einen Link im Text.
[MarkdownX]: 

Eine weitere Funktion die ich wollte war, dass ich mein GitHub Repository auf der Website anzeigen kann. Auch hierfür habe ich wieder eine passende Bibliothek gefunden. Mit [PyGithub](https://github.com/PyGithub/PyGithub) habe ich eine GitHub-API-Bibliothek gefunden, die es mir erlaubt mit Python3 Informationen zu allen meinen Repositories zu bekommen. Diese werden dann dem Client angezeigt.

## Was ich bei diesem Projekt gelernt habe:

* Erstellen einer Website mit Hilfe eines Frameworks
* Mardown Language
* Arbeiten mit APIs (in diesem Fall [PyGithub](https://github.com/PyGithub/PyGithub))
* Verwendung von Bootstrap
* Verwendung von Apache2 als Server
* Verwendung von Virtual Environment in Python3
* ssh-Kommunikation mit ssh-Keys
* Websiten für Smartphones anpassen (CSS)