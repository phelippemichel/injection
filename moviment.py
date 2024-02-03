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

    time.sleep(0.25) # Jean, menos que isso, ele acaba comendo as posicoes que sao iguais
    print(f"Personagem na posição: {current_position} - {move}")


key_mapping = {"up": VK_W, "down": VK_S, "left": VK_A, "right": VK_D}

# Coordenadas
coordinates_list = [
    (4953, 4880, 7),
    (4954, 4880, 7),
    (4953, 4880, 7),
    (4952, 4880, 7),
    (4951, 4880, 7),
    (4950, 4880, 7),
    (4949, 4880, 7),
    (4948, 4880, 7),
    (4947, 4880, 7),
    (4946, 4880, 7),
    (4945, 4880, 7),
    (4944, 4880, 7),
    (4943, 4880, 7),
    (4942, 4880, 7),
    (4941, 4880, 7),
    (4941, 4879, 7),
    (4941, 4878, 7),
    (4941, 4877, 7),
    (4942, 4877, 7),
    (4943, 4877, 7),
    (4944, 4877, 7),
    (4944, 4878, 7),
    (4944, 4879, 7),
    (4944, 4880, 7),
    (4945, 4880, 7),
    (4946, 4880, 7),
    (4947, 4880, 7),
    (4948, 4880, 7),
    (4949, 4880, 7),
    (4950, 4880, 7),
    (4951, 4880, 7),
    (4952, 4880, 7),
    (4953, 4880, 7)
]

for i in range(len(coordinates_list) - 1):
    move_character(coordinates_list[i], coordinates_list[i + 1])

# Movimento para a última coordenada
move_character(coordinates_list[-1], coordinates_list[0])  # Adicionando movimento de volta para a primeira coordenada
