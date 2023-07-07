import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter import *
from PIL import Image, ImageTk
import subprocess
import threading

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("A.I. Voice Assistance")
        self.geometry("1000x700")
        self.iconbitmap("voice-control.ico")

        # Add background image
        self.background_image = Image.open("background.png")  # Replace with your background image file name
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        self.background_label = ttk.Label(self, image=self.background_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.background_label.image = self.background_photo  # Store a reference to avoid garbage collection

        # Create GUI elements
        self.text_font = font.Font(family="Space Grotesk", size=10, weight="bold")

        self.microphone_start_image = Image.open("microphone_start.png")  # Replace with your microphone start image file name
        self.microphone_start_image = self.microphone_start_image.resize((30, 30))  # Resize the image if necessary
        self.microphone_start_photo = ImageTk.PhotoImage(self.microphone_start_image)

        self.microphone_stop_image = Image.open("microphone_stop.png")  # Replace with your microphone stop image file name
        self.microphone_stop_image = self.microphone_stop_image.resize((30, 30))  # Resize the image if necessary
        self.microphone_stop_photo = ImageTk.PhotoImage(self.microphone_stop_image)

        self.button_frame = ttk.Frame(self)
        self.button_frame.place(x=10, y=60)
        self.button_style = ttk.Style()
        self.button_style.configure("Custom.TButton",
                                     background="white",  # Set the background color of the button
                                     relief="flat",  # Make the button flat
                                     font=self.text_font,
                                     foreground="black")  # Set the foreground (text) color of the button
        self.button = ttk.Button(self.button_frame, text="Tap to Speak", image=self.microphone_start_photo,
                                 compound=tk.LEFT, command=self.toggle_script, style="Custom.TButton")
        self.button.pack(side=tk.LEFT)
        self.text_area = tk.Text(self, height=25, width=35, font=self.text_font)
        self.text_area.place(x=10, y=110)

        self.configure(background="#3d6466")

        self.process = None
        self.running = False

    def toggle_script(self):
        if not self.running:
            self.start_script()
            self.button.config(image=self.microphone_stop_photo, text="Stop Listening",
                               style="Custom.TButton.Active")  # Change button style when active
        else:
            self.stop_script()
            self.button.config(image=self.microphone_start_photo, text="Tap to Speak",
                               style="Custom.TButton")  # Change button style when inactive

    # Rest of the code...


    def start_script(self):
        self.running = True
        self.button.config(image=self.microphone_stop_photo, text="Stop Listening")
        self.text_area.delete(1.0, tk.END)  # Clear the output area
        self.process = subprocess.Popen(["python", "-u", "main.py"], stdout=subprocess.PIPE,
                                        stderr=subprocess.STDOUT, universal_newlines=True)
        self.start_output_thread()

    def stop_script(self):
        if self.running:
            self.process.terminate()
            self.process = None
            self.running = False
            self.button.config(image=self.microphone_start_photo, text="Tap to Speak")

    def start_output_thread(self):
        thread = threading.Thread(target=self.update_output)
        thread.daemon = True
        thread.start()

    def update_output(self):
        for line in iter(self.process.stdout.readline, ''):
            if line:
                self.text_area.insert(tk.END, line)
                self.text_area.see(tk.END)

        self.stop_script()

if __name__ == '__main__':
    app = Application()
    app.mainloop()
