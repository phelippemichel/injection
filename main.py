from memory_reader import MemoryReader
from gui import GUI

if __name__ == "__main__":
    process_name = "ravendawn_dx-1706708469.exe"
    memory_reader = MemoryReader(process_name)
    gui = GUI(memory_reader)
    gui.mainloop()