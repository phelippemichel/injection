from memory_reader import MemoryReader
from gui import GUI
import threading

def main():
    memory_reader = MemoryReader("ravendawn_dx-1706708469.exe")
    memory_reader.open_process()

    x_address = 0x7FF6C301468C
    y_address = 0x7FF6C3014690
    z_address = 0x7FF6C3014694

    addresses = [x_address, y_address, z_address]
    size = 4

    gui = GUI(memory_reader)

    def read_memory_thread():
        try:
            while True:
                memory_reader.read_memory(addresses, size)
        except pymem.exception.MemoryReadError:
            print("An error occurred while reading memory. Make sure that the address and process are valid")

    memory_thread = threading.Thread(target=read_memory_thread)
    memory_thread.start()

    gui.start_gui()

if __name__ == "__main__":
    main()