import time
import pymem
from dotenv import load_dotenv
import os

load_dotenv()

def read_coordinates(process, address):
    size = 4
    try:
        data = process.read_bytes(address, size)
        value = int.from_bytes(data, byteorder='little')
        return value
    except pymem.exception.MemoryReadError:
        raise ValueError(f"Failed to read memory at address {address}")

def main():
    process_name = os.getenv("PROCESS_NAME")

    try:
        process = pymem.Pymem(process_name)

        x_address = 0x7FF7B87A468C
        y_address = 0x7FF7B87A4690
        z_address = 0x7FF7B87A4694

        previous_coordinates = None

        while True:
            x_value = read_coordinates(process, x_address)
            y_value = read_coordinates(process, y_address)
            z_value = read_coordinates(process, z_address)

            current_coordinates = (x_value, y_value, z_value)

            if current_coordinates != previous_coordinates:
                print(f"Coordinates: X={x_value}, Y={y_value}, Z={z_value}")
                previous_coordinates = current_coordinates

            time.sleep(1)

    except pymem.exception.ProcessNotFound:
        print(f"The process {process_name} was not found.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
