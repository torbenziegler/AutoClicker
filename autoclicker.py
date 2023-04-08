import pyautogui
import time
import threading


class AutoClicker:
    def __init__(self):
        self.saved_position = (500, 500)
        self.position = None
        self.interval = None
        self.click_count = 0
        self.clicking = False
        self.is_logging_enabled = False
        self.thread = None

    def set_position(self):
        self.position = pyautogui.position()
        print("Current cursor position: {}".format(self.position))

    def save_position(self):
        self.saved_position = pyautogui.position()
        print("Saved position: {}".format(self.saved_position))

    def get_clicking(self):
        return self.clicking

    def set_interval(self, interval):
        self.interval = interval

    def toggle_pause(self):
        # set clicking to opposite of current value
        self.clicking = not self.clicking
        if self.clicking:
            print("Start AutoClicker")
            self.move_to_saved_position()
            self.start_autoclicker()
        else:
            print("Stop AutoClicker")
            self.stop_autoclicker()

    def toggle_logging(self):
        self.is_logging_enabled = not self.is_logging_enabled
        print("Logging is {}".format("enabled" if self.is_logging_enabled else "disabled"))

    def move_to_saved_position(self):
        pyautogui.moveTo(self.saved_position)

    def start_autoclicker(self):
        self.thread = threading.Thread(target=self._autoclicker_loop)
        self.thread.start()

    def stop_autoclicker(self):
        self.clicking = False

    def _autoclicker_loop(self):
        while self.clicking:
            self.set_position()
            # check if position is same as saved position
            if self.position == self.saved_position:
                pyautogui.click(self.saved_position)
                print("Clicked at {}".format(self.saved_position))
                self.increment_clicks()
                if self.is_logging_enabled:
                    self.log()
            time.sleep(self.interval)
        self.thread = None

    def increment_clicks(self):
        self.click_count += 1

    def log(self):
        with open("clicks.log", "a") as f:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"Timestamp: {timestamp}, Position: {self.position}\n")
