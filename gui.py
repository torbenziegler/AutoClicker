import tkinter as tk
from tkinter import ttk
import customtkinter as ctk

class AutoClickerGUI(ctk.CTk):
    def __init__(self, autoclicker):
        super().__init__()
        self.autoclicker = autoclicker
        self.root = ctk.CTk()
        self.root.title("AutoClicker")
        self.root.geometry("400x300")
        self.set_appearance_mode("system")
        self.create_widgets()
        self.update_saved_position_label()
        self.update_click_count_label()
        self.root.protocol("WM_DELETE_WINDOW", self.quit)
        self.root.bind('<s>', lambda event: self.save_position())
        self.root.bind('<m>', lambda event: self.move_to_saved_position())
        self.root.bind('<r>', lambda event: self.toggle_pause())
        self.root.bind('<q>', lambda event: self.quit())

    def set_appearance_mode(self, mode):
        ctk.set_appearance_mode(mode)

    def create_widgets(self):
        # Saved position
        self.position_label = ctk.CTkLabel(self.root, text="Saved position: ")
        self.position_label.pack(pady=5)

        # Click count
        self.click_count_label = ctk.CTkLabel(self.root, text="Click count: ")
        self.click_count_label.pack(pady=5)

        # Interval frame
        self.interval_frame = ctk.CTkFrame(self.root)
        self.interval_frame.pack(pady=5)
        self.interval_label = ctk.CTkLabel(self.interval_frame, text="Click interval (s):")
        self.interval_label.pack(side=tk.LEFT, padx=5)
        self.interval_var = ctk.StringVar(value="1")
        self.interval_dropdown = ctk.CTkOptionMenu(self.interval_frame, variable=self.interval_var, values=["0.1", "0.5", "1", "5", "10", "30", "60"], command=self.update_interval)
        self.update_interval(self.interval_var.get())
        self.interval_dropdown.pack(side=tk.LEFT)

        # Start button
        self.start_button = ctk.CTkButton(self.root, text="Start AutoClicker (R)", command=self.toggle_pause, fg_color="#2bbf02", hover_color="green")
        self.start_button.pack(pady=5)

        # Move button
        self.move_button = ctk.CTkButton(self.root, text="Move to saved position (M)", command=self.move_to_saved_position)
        self.move_button.pack(pady=5)

        # Logging
        self.logging_checkbox = ctk.CTkCheckBox(self.root, text="Logging enabled", command=self.toggle_logging)
        self.logging_checkbox.pack()

        # Appearance
        self.appearance_frame = ctk.CTkFrame(self.root)
        self.appearance_frame.pack(pady=5)
        self.appearance_label = ctk.CTkLabel(self.appearance_frame, text="Appearance:")
        self.appearance_label.pack(side=tk.LEFT, padx=5)
        self.appearance_dropdown = ctk.CTkOptionMenu(self.appearance_frame, values=["System", "Light", "Dark"], command=self.set_appearance_mode)
        self.appearance_dropdown.pack(side=tk.LEFT)

    def update_saved_position_label(self):
        position_str = "Saved position: ({}, {}) (S)".format(self.autoclicker.saved_position[0], self.autoclicker.saved_position[1])
        self.position_label.configure(text=position_str)
        self.root.after(100, self.update_saved_position_label)

    def update_click_count_label(self):
        click_count_str = "Click count: {}".format(self.autoclicker.click_count)
        self.click_count_label.configure(text=click_count_str)
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
            self.start_button.configure(text="Stop AutoClicker (R)", command=self.toggle_pause, fg_color="#FF0000", hover_color="#BA0000")
        else:
            self.start_button.configure(text="Start AutoClicker (R)", command=self.toggle_pause, fg_color="#2bbf02", hover_color="green")


    def toggle_logging(self):
        self.autoclicker.toggle_logging()

    def quit(self):
        self.autoclicker.quit()
        self.root.destroy()

    def run(self):
        self.root.mainloop()