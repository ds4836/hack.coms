import tkinter as tk
from src.color_selection import rgb_to_hex

def display_colors(colors):
    root = tk.Tk()
    canvas_width = 400
    canvas_height = 100
    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
    canvas.pack()

    radius = 15
    y = canvas_height//2

    for index, color in enumerate(colors):
        x = 20 + (index * 30)
        canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=rgb_to_hex(color), outline='')


    root.mainloop()