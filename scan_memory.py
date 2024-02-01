import pymem
import time

process_name = "ravendawn_dx-1706708469.exe"

try:
    process = pymem.Pymem(process_name)
    
    Haddress = 0x7FF6C301468C
    # Vaddress = 0x7FF6C3014690
    
    size = 4 

    while True:
       
        data = process.read_bytes(Haddress, size)
        
        value = int.from_bytes(data, byteorder='little')  

        print(f"Dados lidos na memória: {data}")
        print(f"Valor convertido: {value}")

        
        time.sleep(1)  

except pymem.exception.ProcessNotFound:
    print(f"O processo {process_name} não foi encontrado.")

except pymem.exception.MemoryReadError:
    print("Erro ao ler a memória. Certifique-se de que o endereço e o processo são válidos.")
