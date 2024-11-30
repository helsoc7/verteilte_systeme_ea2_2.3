
# Publish/Subscribe Time Server in Python

Dieses Projekt implementiert ein einfaches **Publish/Subscribe-System** mit Python und ZeroMQ. Der Server (Publisher) veröffentlicht alle 5 Sekunden die aktuelle Zeit, und mehrere Clients (Subscriber) können diese Nachrichten empfangen.

## Features
- **Publisher (Server):** Sendet die aktuelle Uhrzeit an alle verbundenen Clients.
- **Subscriber (Clients):** Empfangen und zeigen die veröffentlichten Zeitnachrichten an.
- **Multithreading:** Der Server und die Clients laufen in separaten Prozessen, sodass mehrere Subscriber gleichzeitig getestet werden können.

## Anforderungen
- Python 3.x
- ZeroMQ-Bibliothek (pyzmq)

## Setup
Starte das Projekt, indem du die requirements.txt. Datei installierst:
```bash
pip install -r requirements.txt
```
(optimal in einer venv)


## Verwendung
### 1. Skript ausführen
Speichere das Skript als `pub_sub_time.py` und starte es:
```bash
python pub_sub_time.py
```

### 2. Funktionsweise
- Der Server sendet alle 5 Sekunden eine Zeitnachricht.
- Die Clients (Subscriber) empfangen die Nachrichten und geben sie auf der Konsole aus.
- Das Skript startet automatisch mehrere Subscriber-Prozesse.

### 3. Beispielausgabe
#### Server:
```text
Server läuft und veröffentlicht die Zeit...
Veröffentlicht: TIME Sun Nov 30 12:00:00 2024
Veröffentlicht: TIME Sun Nov 30 12:00:05 2024
```

#### Clients:
```text
Client Client-1 ist mit dem Server verbunden und wartet auf Nachrichten...
Client Client-1 empfing: TIME Sun Nov 30 12:00:00 2024
Client Client-1 empfing: TIME Sun Nov 30 12:00:05 2024
```
```text
Client Client-2 ist mit dem Server verbunden und wartet auf Nachrichten...
Client Client-2 empfing: TIME Sun Nov 30 12:00:00 2024
Client Client-2 empfing: TIME Sun Nov 30 12:00:05 2024
```

### 4. Stoppen des Programms
Drücke `CTRL+C`, um das Programm zu beenden. Alle Prozesse (Server und Clients) werden automatisch beendet.

## Anpassungen
- Die Anzahl der Clients kann durch Ändern der Zeile `for i in range(3)` im Skript erhöht oder verringert werden.
- Der Zeitintervall für die Nachrichten kann in der Zeile `time.sleep(5)` angepasst werden.

## Hintergrund
Dieses Projekt illustriert das **Publish/Subscribe-Muster**:
- Der **Publisher** veröffentlicht Nachrichten, die mit einem Tag versehen sind (z. B. `"TIME"`).
- Der **Subscriber** filtert Nachrichten basierend auf dem abonnierten Tag und empfängt nur relevante Informationen.

## Autor
Dieses Projekt wurde basierend auf einer Aufgabe aus dem Buch *Distributed Systems, 4th Edition, 2024* entwickelt.
