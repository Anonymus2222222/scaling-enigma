import tkinter as tk
import random
import time

root = tk.Tk()
root.geometry('300x200')  # Taille de la fenêtre

# Liste de couleurs pour le prank
colors = ['red', 'green', 'blue', 'yellow', 'purple', 'orange']

def change_color():
    color = random.choice(colors)
    root.configure(bg=color)
    root.after(500, change_color)  # Change la couleur toutes les 500 ms

change_color()
root.mainloop()
