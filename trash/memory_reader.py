import pymem

class MemoryReader:
    def __init__(self, process_name):
        self.process_name = process_name
        self.process = None

    def open_process(self):
        try:
            self.process = pymem.Pymem(self.process_name)
        except pymem.exception.ProcessNotFound:
            raise ValueError(f"The process {self.process_name} was not found.")

    def read_coordinates(self, address):
        size = 4
        try:
            data = self.process.read_bytes(address, size)
            value = int.from_bytes(data, byteorder='little')
            return value
        except pymem.exception.MemoryReadError:
            raise ValueError(f"Failed to read memory at address {address}")
