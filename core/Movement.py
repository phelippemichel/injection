import pymem
from core.Database import Database
from core.Load import Load
from core.Offset import Horizontal,Vertical,Layer
from core.key_codes import *
from time import sleep
import ctypes


class Movement:
    @staticmethod   
    def getPosition(module_name,pid):
        process = pymem.Pymem(pid)
        modules = process.list_modules()
        target_module = next((module for module in modules if module.name.lower() == module_name.lower()), None)

        if target_module:
            
            module_base = target_module.lpBaseOfDll
            final_address = module_base

            position_x = process.read_bytes(final_address + int(hex(Horizontal)[2:], 16), 4)
            position_y = process.read_bytes(final_address + int(hex(Vertical)[2:], 16), 4)
            position_z = process.read_bytes(final_address + int(hex(Layer)[2:], 16), 4)

            result_x = int.from_bytes(position_x, byteorder='little', signed=False)
            result_y = int.from_bytes(position_y, byteorder='little', signed=False)
            result_z = int.from_bytes(position_z, byteorder='little', signed=False)

            return (result_x,result_y,result_z)

        else:

            return None
    @staticmethod   
    def createRouter(module_name,pid):
        Position = Movement.getPosition(module_name,pid)
        Start = Position
        Moving = []
        while len(Moving) < 5:
            Verify = Movement.getPosition(module_name,pid)
            if not Position == Verify:
                Moving.append(tuple(a - b for a, b in zip(Verify,Position)))
                
                Position = Verify
            sleep(0.1)
        End = Position
        
        input("Go?")
        Movement.Walk(Start,End,Moving,module_name,pid)
    

    def send_message_keyboard(key_code):
        hwnd = ctypes.windll.user32.FindWindowW(0, 'Ravendawn - Jepart')
        ctypes.windll.user32.PostMessageW(hwnd, WM_KEYDOWN, key_code, 0)
        sleep(0.1)
        ctypes.windll.user32.PostMessageW(hwnd, WM_KEYUP, key_code, 0)
    
    @staticmethod
    def getKey(tuple):
        if tuple[0] == 1:
            return VK_D
        if tuple[0] == -1:
            return VK_A
        if tuple[1] == 1:
            return VK_S
        if tuple[1] == -1:
            return VK_W
    
    @staticmethod    
    def Walk(start,end,positions,module_name,pid):
        Position = Movement.getPosition(module_name,pid)
        while Position != start:
            print(Position)
            Position = Movement.getPosition(module_name,pid)
            sleep(1)
        Count = start
        for move in positions:
            PositionStart = Movement.getPosition(module_name,pid)
            Movement.send_message_keyboard(Movement.getKey(move))
            Verify = Movement.getPosition(module_name,pid)
            while Verify != tuple(a + b for a, b in zip(PositionStart, move)):
                Movement.send_message_keyboard(Movement.getKey(move))
                Verify = Movement.getPosition(module_name,pid)
        