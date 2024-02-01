import pymem

def read_coordinates(process, address):
    size = 4
    try:
        data = process.read_bytes(address, size)
        value = int.from_bytes(data, byteorder='little')
        return value
    except pymem.exception.MemoryReadError:
        raise ValueError(f"Failed to read memory at address {address}")

def main():
    process_name = "ravendawn_dx-1706708469.exe"

    try:
        process = pymem.Pymem(process_name)

        x_address = 0x7FF6C301468C
        y_address = 0x7FF6C3014690
        z_address = 0x7FF6C3014694

        x_value = read_coordinates(process, x_address)
        y_value = read_coordinates(process, y_address)
        z_value = read_coordinates(process, z_address)

        print(f"Coordinates: X={x_value}, Y={y_value}, Z={z_value}")

    except pymem.exception.ProcessNotFound:
        print(f"The process {process_name} was not found.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()