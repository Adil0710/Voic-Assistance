import subprocess
import threading
from tkinter import *
from PIL import Image, ImageTk
from tkinter import PhotoImage
from urllib.parse import urlencode


process = None  # Declare the process variable as a global variable
micstart_img = None  # Global variable to hold the 'micstart' image
micstop_img = None  # Global variable to hold the 'micstop' image

class TransparentText(Text):
    def __init__(self, *args, **kwargs):
        from urllib.parse import urlencode

        super().__init__(*args, **kwargs)
        from urllib.parse import urlencode

        self.configure(
            bd=0,
            highlightthickness=0,
            relief="flat",
            insertbackground="#F2F4F4",  # Set the cursor color to white for better visibility
            highlightbackground="#F2F4F4"  # Set the highlight background color to match the window's background color
        )

def read_output():
    global process, button

    while True:
        output = process.stdout.readline().strip()
        if not output:
            break
        entry0.config(state="normal")
        entry0.insert(END, output + '\n')
        entry0.config(state="disabled")
        entry0.see(END)  # Scroll to the end of the text area
        window.update_idletasks()  # Update the GUI to show the new text

    # Process completed
    process = None

    # Update the button text and image
    button.config(
        text="Tap to Speak",
        font=("Roboto", 10, "bold"),
        image=micstart_img  # Change the button's image to "micstart"
    )

def run_script():
    global process
    process = subprocess.Popen(
        ["python", "-u", "main.py"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True,
        creationflags=subprocess.CREATE_NO_WINDOW
    )

    # Start a separate thread to read the output
    output_thread = threading.Thread(target=read_output)
    output_thread.start()

    # Wait for the process to complete
    process.wait()
    output_thread.join()  # Wait for the output thread to finish

    process = None  # Set process to None when the execution is complete


# Define a flag variable to track the button state
is_listening = False

def btn_clicked():
    global process, button, entry0, micstart_img, micstop_img, is_listening

    if process is None or process.poll() is not None:
        # Start the script in a separate thread
        threading.Thread(target=run_script, daemon=True).start()

        is_listening = not is_listening

    else:
        # Stop the script
        process.terminate()
        process.wait()  # Wait for the process to complete
        process = None

        is_listening = not is_listening

    # Toggle between text and image based on the button state
    if is_listening:
        button.config(text="Stop Listening")
    else:
        button.config(text="Tap to Speak")

    # Toggle between images based on the button state
    if is_listening:
        button.config(image=micstop_img)
    else:
        button.config(image=micstart_img)

    # Clear the contents of the text area
    entry0.config(state="normal")  # Enable the text area for clearing
    entry0.delete(1.0, END)  # Clear the contents of the text area
    entry0.config(state="disabled")  # Disable the text area to prevent user input


       

def on_closing():
    global process

    if process is not None and process.poll() is None:
        # Stop the script before closing the window
        process.terminate()

    window.destroy()

window = Tk()
window.geometry("1000x700")
window.title("Voice Assistant")
window.wm_iconbitmap("images/voice-control.ico")
window.configure(bg="#ffffff")

window.wm_protocol("WM_DELETE_WINDOW", on_closing)

canvas = Canvas(
    window,
    bg="#ffffff",
    height=700,
    width=1000,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

background_img_path = "images/background.png"
background_img = Image.open(background_img_path)
background_img = background_img.resize((1000, 700), Image.LANCZOS)
background_tk = ImageTk.PhotoImage(background_img)

background = canvas.create_image(
    500.0, 350.0,
    image=background_tk
)

entry0 = TransparentText(
    window,
    font=("Inter", 11),  # Set the font as desired
    wrap=WORD,
    width=40,
    height=10,
    bg="#F2F4F4",  # Set the background color to transparent
    highlightthickness=0,
    bd=0,
    relief="flat",
    state="disabled",
    fg="#797D7F"
)
entry0.place(
    x=658, y=170,
    width=285,
    height=367
)

def on_button_enter(event):
    button.config(bg='#8E44AD', fg='#FFFFFF')


def on_button_leave(event):
    button.config(bg='#6C3483', fg='#D9D9D9')


# Add the image to the button
micstart_img = PhotoImage(file="images/micstart.png")
micstop_img = PhotoImage(file="images/micstop.png")
button = Button(
    window,
    text="Tap to Speak",
    font=("Roboto", 10, "bold"),
    command=btn_clicked,
    image=micstart_img,  # Set the button's image to "micstart"
    compound="left",  # Display the image to the left of the text
    bg='#6C3483',
    fg='#D9D9D9',
    bd=0,
    relief="flat",
    highlightthickness=0
)
button.pack()
button.place(x=160, y=500, height=40, width=140)

window.bind('<Return>', lambda event: button.invoke())

button.bind("<Enter>", on_button_enter)
button.bind("<Leave>", on_button_leave)

window.resizable(False, False)
window.mainloop()
