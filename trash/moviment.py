import time
import ctypes
from key_codes import *
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

    time.sleep(0.18) # Jean, menos que isso, ele acaba comendo as posicoes que sao iguais
    print(f"Personagem na posição: {current_position} - {move}")


key_mapping = {"up": VK_W, "down": VK_S, "left": VK_A, "right": VK_D}

# Coordenadas
coordinates_list = [
    (5071, 5108, 6),
    (5072, 5108, 6),
    (5073, 5108, 6),
    (5074, 5108, 6),
    (5075, 5108, 6),
    (5075, 5109, 6),
    (5075, 5110, 6),
    (5075, 5111, 6),
    (5075, 5112, 6),
    (5075, 5113, 6),
    (5075, 5114, 6),
    (5075, 5115, 6),
    (5076, 5115, 6),
    (5077, 5115, 6),
    (5078, 5115, 6),
    (5079, 5115, 6),
    (5080, 5115, 6),
    (5081, 5115, 6),
    (5082, 5115, 6),
    (5083, 5115, 6),
    (5084, 5115, 6),
    (5085, 5115, 6),
    (5086, 5115, 6),
    (5087, 5115, 6),
    (5088, 5115, 6),
    (5089, 5115, 6),
    (5090, 5115, 6),
    (5091, 5115, 6),
    (5092, 5115, 6),
    (5093, 5115, 6),
    (5094, 5115, 6),
    (5094, 5116, 6),
    (5094, 5117, 6),
    (5094, 5118, 6),
    (5094, 5119, 6),
    (5094, 5120, 6),
    (5095, 5120, 6),
    (5096, 5120, 6),
    (5097, 5120, 6),
    (5098, 5120, 6),
    (5099, 5120, 6),
    (5100, 5120, 6),
    (5101, 5120, 6),
    (5102, 5120, 6),
    (5103, 5120, 6),
    (5104, 5120, 6),
    (5105, 5120, 6),
    (5106, 5120, 6),
    (5107, 5120, 6),
    (5108, 5120, 6),
    (5109, 5120, 6),
    (5110, 5120, 6),
    (5111, 5120, 6),
    (5112, 5120, 6),
    (5113, 5120, 6),
    (5114, 5120, 6),
    (5115, 5120, 6),
    (5116, 5120, 6),
    (5117, 5120, 6),
    (5118, 5120, 6),
    (5119, 5120, 6),
    (5120, 5120, 6),
    (5121, 5120, 6),
    (5122, 5120, 6),
    (5123, 5120, 6),
    (5124, 5120, 6),
    (5125, 5120, 6),
    (5125, 5119, 6),
    (5125, 5118, 6),
    (5125, 5117, 6),
    (5125, 5116, 6)
]

for i in range(len(coordinates_list) - 1):
    move_character(coordinates_list[i], coordinates_list[i + 1])

# Movimento para a última coordenada
move_character(coordinates_list[-1], coordinates_list[0])  # Adicionando movimento de volta para a primeira coordenada
