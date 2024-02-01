import tkinter as tk
from tkinter import Label, Button, messagebox

class GUI(tk.Tk):
    def __init__(self, memory_reader):
        super().__init__()
        self.title("Memory Reader")
        self.geometry("300x100")

        self.label = Label(self, text="Data read from memory: ")
        self.label.pack()

        self.memory_reader = memory_reader

        # Botão para exibir as coordenadas salvas
        self.show_saved_button = Button(self, text="Show Saved Coordinates", command=self.show_saved_coordinates)
        self.show_saved_button.pack()

    def update_label(self, data):
        self.label.config(text=f"Data read from memory: {data}")

    def start_gui(self):
        self.after(0, self.update_gui)
        self.mainloop()

    def update_gui(self):
        data = self.memory_reader.get_saved_values()
        self.update_label(data)
        self.after(100, self.update_gui)

    def show_saved_coordinates(self):
        saved_values = self.memory_reader.get_saved_values()
        if saved_values:
            coordinates_str = ""

            for entry in saved_values:
                if isinstance(entry, int):
                    coordinates_str += str(entry) + "\n"
                else:
                    coordinates_str += f"({', '.join(map(str, entry))})\n"

            messagebox.showinfo("Saved Coordinates", f"Saved Coordinates:\n{coordinates_str}")
        else:
            messagebox.showinfo("Saved Coordinates", "No coordinates saved yet.")
