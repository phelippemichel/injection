import ctypes

# Abre o processo com base no ID do processo
process_id = 25272  # Substitua pelo ID do processo desejado
process_handle = ctypes.windll.kernel32.OpenProcess(0x1F0FFF, False, process_id)

if process_handle:
    # Endereço de memória onde a quantidade de dinheiro está armazenada
    money_address = 0x00112233  # Substitua pelo endereço real

    # Novo valor para o dinheiro (substitua pelo valor desejado)
    new_money_value = 9999

    # Escreve o novo valor na memória do processo
    ctypes.windll.kernel32.WriteProcessMemory(process_handle, money_address, ctypes.byref(ctypes.c_int(new_money_value)), 4)

    # Fecha o handle do processo
    ctypes.windll.kernel32.CloseHandle(process_handle)
else:
    print("Não foi possível abrir o processo.")
