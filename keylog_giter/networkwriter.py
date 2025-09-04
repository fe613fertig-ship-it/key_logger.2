# import socket
# import json
#
# class NetworkWriter(IWriter):
#
from abc import ABC, abstractmethod


class IWriter(ABC):
    @abstractmethod
    def write(self, data):
        pass
import socket
import json

class NetworkWriter(IWriter):
    def __init__(self, host, port):
        self.server_address = (host, port)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(self.server_address)

    def write(self, data):
        massage = json.dumps(data).encode("utf-8")
        self.sock.sendall(massage)

    def close(self):
        self.sock.close()

def log_event(writer: IWriter, event: str):
        data = {"event": event}
        writer.write(data)



# כתיבה לרשת
nw = NetworkWriter("127.0.0.1", 5000)  # צריך להריץ שרת מאזין
log_event(nw, "User login from client")
log_event(nw, "User sent message")
nw.close()
