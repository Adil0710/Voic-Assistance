import tkinter as tk
import customtkinter as ctk

def create_gradient(canvas, width, height, color1, color2):
    # Create a vertical gradient background on the canvas
    for i in range(height):
        r = int(color1[0] + (color2[0] - color1[0]) * i / height)
        g = int(color1[1] + (color2[1] - color1[1]) * i / height)
        b = int(color1[2] + (color2[2] - color1[2]) * i / height)
        color = "#%02x%02x%02x" % (r, g, b)
        canvas.create_rectangle(0, i, width, i+1, fill=color, outline="")

root = tk.Tk()
root.geometry("400x300")

# Create a canvas to hold the gradient background
canvas = ctk.CTkCanvas(root, width=400, height=300)
canvas.pack(fill="both", expand=True)

# Define the start and end colors for the gradient
color1 = (255, 255, 255)  # White
color2 = (0, 0, 255)      # Blue

# Create the gradient background on the canvas
create_gradient(canvas, 400, 300, color1, color2)

# Create a transparent label
label = ctk.CTkLabel(root, text="Transparent Label", font=("Arial", 16))
label.configure(highlightthickness=0)
label.place(relx=0.5, rely=0.4, anchor="center")

# Create a transparent button
button = ctk.CTkButton(root, text="Transparent Button")
button.configure(highlightthickness=0)
button.place(relx=0.5, rely=0.6, anchor="center")

root.mainloop()
