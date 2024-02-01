import pymem
import time
import pickle

class MemoryReader:
    def __init__(self, process_name):
        self.process_name = process_name
        self.process = None

    def open_process(self):
        try:
            self.process = pymem.Pymem(self.process_name)
        except pymem.exception.ProcessNotFound:
            print(f"The process {self.process_name} not found.")

    def read_memory(self, addresses, size):
        save_values = []

        while True:
            actual_values = []
            for i, address in enumerate(addresses):
                data = self.process.read_bytes(address, size)
                value = int.from_bytes(data, byteorder='little')
                actual_values.append(value)

            if actual_values != save_values:
                print(f"Data read from memory: {actual_values}")
                save_values = actual_values.copy()

                with open("save_values.pkl", "wb") as file:
                    pickle.dump(save_values, file)

            time.sleep(0.2)

    def get_saved_values(self):
        try:
            with open("save_values.pkl", "rb") as file:
                saved_values = pickle.load(file)
            return saved_values
        except FileNotFoundError:
            return []