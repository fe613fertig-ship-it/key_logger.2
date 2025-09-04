# import socket
# import json
#
# class NetworkWriter(IWriter):
#
from abc import ABC, abstractmethod
import socket
import json

class IWriter(ABC):
    @abstractmethod
    def write(self, data):
        pass

class NetworkWriter(IWriter):
    def __init__(self, host, port):
        self.server_address = (host, port)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(self.server_address)

    def write(self, data):
        # שליחה
        message = json.dumps(data).encode("utf-8")
        self.sock.sendall(message)

        # קבלה (אפשר לקרוא תגובה מהשרת)
        response = self.sock.recv(4096)
        if response:
            try:
                return json.loads(response.decode("utf-8"))
            except json.JSONDecodeError:
                return response.decode("utf-8")
        return None

    def close(self):
        self.sock.close()


def log_event(writer: IWriter, event: str):
    data = {"event": event}
    response = writer.write(data)
    if response:
        print("Server response:", response)


# דוגמה לשימוש
if __name__ == "__main__":
    nw = NetworkWriter("127.0.0.1", 5000)  # צריך שרת מאזין
    log_event(nw, "User login from client")
    log_event(nw, "User sent message")
    nw.close()
