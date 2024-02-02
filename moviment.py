import time
import random

def move_character(start, end):
    current_position = list(start)
    move_x,move_y = current_position[0] - end[0],current_position[1] - end[1]
    while current_position != list(end):
        if move_x != 0 and move_y != 0 :
            move_random = random.randrange(2)
        elif move_x != 0:
            move_random = 0
        elif move_y != 0:
            move_random = 1            
        else:
            print("stop")
        if move_random == 0:
            move_x_go = 1 if move_x < 0 else -1
            current_position[0] += move_x_go
            move = "up" if move_x_go < 0 else "down"
        else:
            move_y_go = 1 if move_y < 0 else -1
            current_position[1]+= move_y_go
            move = "left" if move_y_go < 0 else "right"
        print(f"Personagem na posição: {current_position} - {move}")
        time.sleep(0.1)  # Apenas para simular o movimento. Remova isso em uma implementação real
        move_x,move_y = current_position[0] - end[0],current_position[1] - end[1]
    print(f"Chegou ao destino! Posição final: {end}")

# Coordenadas iniciais e finais
start_coordinate = (4141, 5251, 6)
end_coordinate = (4144, 5242, 6)

# Movendo o bonecor
move_character(start_coordinate, end_coordinate)