import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class AutoClickerGUI:
    def __init__(self, autoclicker):
        self.autoclicker = autoclicker
        self.root = tk.Tk()
        self.root.title("AutoClicker")
        self.root.geometry("400x300")
        self.create_widgets()
        self.update_saved_position_label()
        self.update_click_count_label()
        self.root.bind('<s>', lambda event: self.save_position())
        self.root.bind('<m>', lambda event: self.move_to_saved_position())
        self.root.bind('<r>', lambda event: self.toggle_pause())
        self.root.bind('<q>', lambda event: self.root.destroy())

    def create_widgets(self):
        self.position_label = ttk.Label(self.root, text="Saved position: ")
        self.position_label.pack(pady=5)
        self.click_count_label = ttk.Label(self.root, text="Click count: ")
        self.click_count_label.pack(pady=5)
        self.interval_frame = ttk.Frame(self.root)
        self.interval_frame.pack(pady=5)
        self.interval_label = ttk.Label(self.interval_frame, text="Click interval (s):")
        self.interval_label.pack(side=tk.LEFT, padx=5)
        self.interval_var = tk.StringVar(value="1")
        self.interval_dropdown = ttk.OptionMenu(self.interval_frame, self.interval_var, "1", "0.1", "0.5", "1", "5", "10", "30", "60", command=self.update_interval)
        self.update_interval(self.interval_var.get())
        self.interval_dropdown.pack(side=tk.LEFT)
        self.start_button = ttk.Button(self.root, text="Start AutoClicker (R)", command=self.toggle_pause)
        self.start_button.pack(pady=5)
        self.move_button = ttk.Button(self.root, text="Move to saved position (M)", command=self.move_to_saved_position)
        self.move_button.pack(pady=5)
        self.logging_checkbox = tk.Checkbutton(self.root, text="Logging enabled", command=self.toggle_logging)
        self.logging_checkbox.pack()

    def update_saved_position_label(self):
        position_str = "Saved position: ({}, {}) (S)".format(self.autoclicker.saved_position[0], self.autoclicker.saved_position[1])
        self.position_label.config(text=position_str)
        self.root.after(100, self.update_saved_position_label)

    def update_click_count_label(self):
        click_count_str = "Click count: {}".format(self.autoclicker.click_count)
        self.click_count_label.config(text=click_count_str)
        self.root.after(100, self.update_click_count_label)

    def update_interval(self, value):
        self.autoclicker.set_interval(float(value))

    def save_position(self):
        self.autoclicker.save_position()
        self.update_saved_position_label()

    def move_to_saved_position(self):
        self.autoclicker.move_to_saved_position()

    def toggle_pause(self):
        self.autoclicker.toggle_pause()
        if self.autoclicker.get_clicking():
            self.start_button.config(text="Stop AutoClicker (R)", command=self.toggle_pause)
        else:
            self.start_button.config(text="Start AutoClicker (R)", command=self.toggle_pause)


    def toggle_logging(self):
        self.autoclicker.toggle_logging()

    def run(self):
        self.root.mainloop()