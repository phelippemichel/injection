# # import pymem

# # def ler_valor_na_memoria(pid, module_name, offsets):
# #     try:
# #         process = pymem.Pymem(pid)
# #         modules = process.list_modules()
# #         target_module = next((module for module in modules if module.name.lower() == module_name.lower()), None)

# #         if target_module:
# #             module_base = target_module.lpBaseOfDll
# #             final_address = module_base

# #             for offset in offsets:
# #                 offset_hex = hex(offset)[2:]
# #                 offset_int = int(offset_hex, 16)
# #                 final_address += offset_int

# #             # Lê o valor na memória considerando a ordem dos bytes little-endian
# #             value_bytes = process.read_bytes(final_address, 4)
# #             value = int.from_bytes(value_bytes, byteorder='little', signed=False)

# #             return value

# #         else:
# #             print(f"Módulo {module_name} não encontrado.")
# #             return None

# #     except Exception as e:
# #         print(f"Ocorreu uma exceção: {e}")
# #         return None

# # # Informações
# # pid = 8720
# # module_name = "ravendawn_dx-1706997596.exe"

# # # Tente ler o valor esperado com offsets 0 e 1
# # offsets_teste1 = [0x27C46BC] # Horizontal
# # offsets_teste2 = [0x1C15398] # Vertical
# # offsets_teste3 = [0x27C46C4] # Level

# # valor_lido_teste = ler_valor_na_memoria(pid, module_name, offsets_teste1)

# # # Imprime o valor lido
# # print(f"Valor lido: {valor_lido_teste}")
# # valor_lido_teste = ler_valor_na_memoria(pid, module_name, offsets_teste2)

# # # Imprime o valor lido
# # print(f"Valor lido: {valor_lido_teste}")
# # valor_lido_teste = ler_valor_na_memoria(pid, module_name, offsets_teste3)

# # # Imprime o valor lido
# # print(f"Valor lido: {valor_lido_teste}")


# # #_----------------------------------------------------------------------

# import pymem

# def encontrar_offset_por_valor(pid, module_name, target_value):
#     try:
#         process = pymem.Pymem(pid)
#         modules = process.list_modules()
#         target_module = next((module for module in modules if module.name.lower() == module_name.lower()), None)

#         if target_module:
#             module_base = target_module.lpBaseOfDll
#             module_end = module_base + target_module.SizeOfImage

#             # Loop através do espaço de endereço do módulo
#             current_address = module_base
#             excludeoffset = []
#             while current_address < module_end:
#                 # Lê um valor de 4 bytes na memória
#                 value_bytes = process.read_bytes(current_address, 4)
#                 current_value = int.from_bytes(value_bytes, byteorder='little', signed=False)

#                 # Verifica se o valor lido corresponde ao valor desejado
#                 # print(f"Valor encontrado no endereço: 0x{current_address:X}")
#                 # if current_value == target_value and f"{current_value:X}" == "0x206F425AEF4":
#                 # print(f"Procurando 0x{current_address:X}")
#                 if current_value == target_value:
#                     # Calcula o offset
#                     offset = current_address - module_base
#                     # if(f"0x{current_address:X}" == "0x7FF6484E46C4"):
#                     print(f"Valor encontrado no endereço: 0x{current_address:X}")
#                     print(f"Offset correspondente: 0x{offset:X}")
#                     # offset_string = f"0x{offset:X}"

# # Convertendo a string hexadecimal para um valor inteiro
#                     # offset_int = int(offset_string, 16)
#                     # excludeoffset.append(offset_int)
#                     # excludeoffset = [0x175A08,0xB924,0xFE7C,0x188]
#                     # if f"0x{offset:X}" in excludeoffset:
#                     #     print("dentro")
#                     #     return offset
#                     # print(excludeoffset)

#                 # Move para o próximo endereço
#                 current_address += 4  # Avança 4 bytes
#             print(f"Valor {target_value} não encontrado no módulo {module_name}.")
#             return excludeoffset

#         else:
#             print(f"Módulo {module_name} não encontrado.")

#     except Exception as e:
#         print(f"Ocorreu uma exceção: {e}")

# # Informações
# pid = 8720
# module_name = "ravendawn_dx-1706997596.exe"

# # Realiza a análise dinâmica para encontrar o offset
# target_value = 5132  # Substitua pelo valor desejado
# offset_encontrado = encontrar_offset_por_valor(pid, module_name, target_value)
# # print(offset_encontrado)
# temp = input("aperte qualquer coisa")
import psutil
import ctypes

def obter_hwnd_por_pid(pid):
    hwnd = None
    try:
        processo = psutil.Process(pid)
        # Obtenha a lista de janelas associadas ao processo
        janelas = processo.window_handles()
        if janelas:
            # Retorne a primeira janela associada ao processo (pode haver mais de uma)
            return janelas[0]
        else:
            print(f"O processo com PID {pid} não tem uma janela associada.")
    except psutil.NoSuchProcess:
        print(f"Não existe processo com o PID {pid}.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Substitua 'SEU_PID_AQUI' pelo PID do processo desejado
pid_desejado = 8720
hwnd_resultado = obter_hwnd_por_pid(pid_desejado)

if hwnd_resultado is not None:
    print(f"O HWND associado ao PID {pid_desejado} é: {hwnd_resultado}")
