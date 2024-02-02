import csv
from Log import Log
import os
from os import mkdir,remove
from os.path import exists

class Cache:
    @staticmethod
    def create(name:str,path:str = 'cache', type:str = "csv"):
        try:
            with open(f"{path}/{name}.{type}", 'w', newline='', encoding='utf-8') as file:
                file.write('')
        except Exception as e:
            Log(f'Ocorreu um erro ao tentar criar o arquivo: {e}',"Error")

    @staticmethod
    def insert(name:str,category:str = "other",array:list = [],path:str = 'cache', type:str = "csv"):
        try:
            if not exists(f"./{path}"):
                mkdir(f"./{path}")
            if not exists(f"{path}/{name}.{type}"):
                Cache.create(f"{category}_{name}",path,type)
            
            with open(f"{path}/{category}_{name}.{type}", 'w', newline='', encoding='utf-8') as file:
                for line in array:
                    file.write(";".join(str(elemento) for elemento in line)+"\n")
        except Exception as e:
            Log(f'Ocorreu um erro ao tentar criar o arquivo: {e}',"Error")
            
    @staticmethod
    def delete(name:str,path:str = 'cache',type:str = "csv"):
        if exists(f"./{path}/{name}.{type}"):
            remove(f"./{path}/{name}.{type}")
        else:
            Log(f'Ocorreu um erro ao tentar deletar o arquivo {name}.{type}',"Error")
