import tkinter as tk

counter = 0

def on_button_click():
    global counter
    counter += 1
    label.config(text=f"Klicks: {counter}")

def on_reset_click():
    global counter
    counter = 0
    label.config(text="Klicks: 0")

# Erstellen des Hauptfensters
root = tk.Tk()
root.title("Mausklick-Counter")
root.geometry("800x400")   # Ändert die Fenstergröße

# Ändert den Hintergrund und die Schriftfarbe
root.configure(bg="black")
root.option_add("*Font", "Helvetica 16")
root.option_add("*Foreground", "black")  # Ändert die Schriftfarbe auf Schwarz

# Erstellen des Labels
label = tk.Label(root, text="Klicks: 0")
label.pack(pady=20)

# Erstellen des Buttons
button = tk.Button(root, text="Klick mich!", command=on_button_click)
button.configure(fg="white", bg="black")  # Ändert die Schriftfarbe auf Weiß und den Hintergrund auf Schwarz
button.pack()

# Erstellen des Reset-Buttons
reset_button = tk.Button(root, text="Reset", command=on_reset_click)
reset_button.configure(fg="white", bg="black")  # Ändert die Schriftfarbe auf Weiß und den Hintergrund auf Schwarz
reset_button.pack(pady=5)

# Starten der Hauptloop
root.mainloop()
