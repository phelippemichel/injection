from datetime import datetime
from os import mkdir
from os.path import exists

class Log:
    @staticmethod
    def __init__(string :str,category:str = 'Log',path:str = 'logs/', type:str = "log") -> None:
        Now = datetime.now()
        data = Now.strftime("%d-%m-%Y")
        if not exists(f"./{path}"):
            mkdir(f"./{path}")
        if not exists(f"{path}/{category}_{data}.{type}"):
            Log.create(f"{category}_{data}",path,type)
        dateTime = Now.strftime("%d-%m-%Y %H:%M:%S")
        with open(f"{path}/{category}_{data}.{type}", 'a', newline='', encoding='utf-8') as file:
            file.write(f"[{category} {dateTime}] {string}\n")
    
    @staticmethod
    def create(name:str,path:str = 'logs', type:str = "log"):
        with open(f"{path}/{name}.{type}", 'w', newline='', encoding='utf-8') as file:
                file.write('')