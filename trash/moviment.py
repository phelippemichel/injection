import time
import ctypes
from core.key_codes import *
from key_actions import send_message_keyboard

hwnd = ctypes.windll.user32.FindWindowW(0, 'Ravendawn - Pimpolhosz')

def move_character(start, end):
    current_position = list(start[:2])  # Considerando apenas os eixos X e Y
    target_position = end[:2]

    move_x = 1 if current_position[0] < target_position[0] else -1 if current_position[0] > target_position[0] else 0
    move_y = 1 if current_position[1] < target_position[1] else -1 if current_position[1] > target_position[1] else 0

    if move_x != 0:
        move = "right" if move_x > 0 else "left"
    elif move_y != 0:
        move = "down" if move_y > 0 else "up"
    else:
        print("stop")

    if move in ["up", "down", "left", "right"]:
        send_message_keyboard(hwnd, key_mapping[move])

    time.sleep(0.25) # Jean, menos que isso, ele acaba comendo as posicoes que sao iguais
    print(f"Personagem na posição: {current_position} - {move}")


key_mapping = {"up": VK_W, "down": VK_S, "left": VK_A, "right": VK_D}

# Coordenadas
# TODO: Adicionar chamada ao banco
coordinates_list = [
    (5071, 5108, 6),
    (5072, 5108, 6),
    (5072, 5107, 6),
]

for i in range(len(coordinates_list) - 1):
    move_character(coordinates_list[i], coordinates_list[i + 1])

# Movimento para a última coordenada
move_character(coordinates_list[-1], coordinates_list[0])  # Adicionando movimento de volta para a primeira coordenada
