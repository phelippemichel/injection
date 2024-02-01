import tkinter as tk
from tkinter import messagebox

# Exemplo da classe MemoryReader (substitua isso pela sua implementação real)
class MemoryReader:
    def __init__(self, process_name):
        pass  # Adicione a inicialização necessária para ler a memória

    def read_coordinates(self):
        # Exemplo de leitura de coordenadas fictícias
        x_value = 50
        y_value = 80
        z_value = 25
        return x_value, y_value, z_value

class CavebotFrame(tk.Frame):
    def __init__(self, master=None, back_callback=None, memory_reader=None, **kwargs):
        super().__init__(master, **kwargs)
        self.back_callback = back_callback
        self.memory_reader = memory_reader
        self.create_widgets()

    def create_widgets(self):
        label = tk.Label(self, text="Cavebot Section")
        label.pack(pady=10)

        # Canvas para exibir as coordenadas
        self.canvas = tk.Canvas(self, width=200, height=200, bg="white")
        self.canvas.pack(pady=10)

    def draw_coordinates_rectangle(self, x, y, z):
        # Fatores de escala para ajustar as coordenadas para caber no Canvas
        scale_factor_x = 5
        scale_factor_y = 5

        # Converte as coordenadas para as dimensões do Canvas
        canvas_x = x * scale_factor_x
        canvas_y = y * scale_factor_y
        canvas_width = 20  # Largura do retângulo no Canvas
        canvas_height = 20  # Altura do retângulo no Canvas

        self.canvas.delete("coordinates_rectangle")  # Limpa retângulos anteriores
        self.canvas.create_rectangle(
            canvas_x, canvas_y, canvas_x + canvas_width, canvas_y + canvas_height,
            outline="black", fill="blue", tags="coordinates_rectangle"
        )

class GUI(tk.Tk):
    def __init__(self, process_name):
        super().__init__()
        self.memory_reader = MemoryReader(process_name)
        self.title("Memory Reader GUI")

        self.cavebot_frame = CavebotFrame(self, back_callback=self.show_main_frame, memory_reader=self.memory_reader)

        self.cavebot_button = tk.Button(self, text="Cavebot", command=self.show_cavebot_frame)
        self.farm_button = tk.Button(self, text="Farm", command=self.show_farm_frame)
        self.tradepack_button = tk.Button(self, text="Tradepack", command=self.show_tradepack_frame)
        self.back_button = tk.Button(self, text="Voltar", command=self.show_main_frame)

        self.cavebot_button.pack(side=tk.LEFT, anchor=tk.N)
        self.farm_button.pack(side=tk.LEFT, anchor=tk.N)
        self.tradepack_button.pack(side=tk.LEFT, anchor=tk.N)

        self.cavebot_frame.pack_forget()

        # Configurações para tornar a janela não redimensionável e com tamanho fixo
        self.resizable(False, False)
        self.geometry("400x300")

    def show_cavebot_frame(self):
        self.farm_button.pack_forget()
        self.tradepack_button.pack_forget()
        self.back_button.pack(side=tk.LEFT, anchor=tk.N)
        self.cavebot_frame.pack()

        # Exemplo de como usar o método para desenhar um retângulo com tamanho específico (100x50)
        x, y, z = self.memory_reader.read_coordinates()
        self.cavebot_frame.draw_coordinates_rectangle(x, y, z)

    def show_main_frame(self):
        self.cavebot_frame.pack_forget()
        self.farm_button.pack(side=tk.LEFT, anchor=tk.N)
        self.tradepack_button.pack(side=tk.LEFT, anchor=tk.N)
        self.back_button.pack_forget()

    def show_farm_frame(self):
        # Adicione aqui a lógica para iniciar o Farm
        messagebox.showinfo("Farm", "Starting Farm.")

    def show_tradepack_frame(self):
        # Adicione aqui a lógica para iniciar o Tradepack
        messagebox.showinfo("Tradepack", "Starting Tradepack.")

if __name__ == "__main__":
    process_name = "ravendawn_dx-1706708469.exe"
    gui = GUI(process_name)
    gui.mainloop()
