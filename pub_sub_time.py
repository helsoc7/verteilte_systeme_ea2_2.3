import multiprocessing
import zmq
import time


def server():
    context = zmq.Context()
    socket = context.socket(zmq.PUB)  # Publisher-Socket
    socket.bind("tcp://*:12345")  # Bind to TCP Port 12345
    print("Server läuft und veröffentlicht die Zeit...")

    while True:
        time.sleep(5)  # Alle 5 Sekunden
        t = "TIME " + time.asctime()
        socket.send(t.encode())  # Zeitnachricht veröffentlichen
        print(f"Veröffentlicht: {t}")


def client(name):
    context = zmq.Context()
    socket = context.socket(zmq.SUB)  # Subscriber-Socket
    socket.connect("tcp://localhost:12345")  # Mit Server verbinden
    socket.setsockopt(zmq.SUBSCRIBE, b"TIME")  # Nachrichten mit "TIME" abonnieren
    print(f"Client {name} ist mit dem Server verbunden und wartet auf Nachrichten...")

    while True:
        message = socket.recv()  # Empfangene Nachricht
        print(f"Client {name} empfing: {message.decode()}")


if __name__ == "__main__":
    # Server-Prozess starten
    server_process = multiprocessing.Process(target=server)
    server_process.start()

    # Mehrere Client-Prozesse starten
    client_processes = []
    for i in range(3):  # Drei Subscriber, hier können wir natürlich mehr machen bei Bedarf
        client_process = multiprocessing.Process(target=client, args=(f"Client-{i+1}",))
        client_process.start()
        client_processes.append(client_process)

    # Server und Clients stoppen (optional nach Testlauf)
    try:
        server_process.join()
        for client_process in client_processes:
            client_process.join()
    except KeyboardInterrupt:
        print("Beenden...")
        server_process.terminate()
        for client_process in client_processes:
            client_process.terminate()
