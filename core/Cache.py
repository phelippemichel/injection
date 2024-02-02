import csv

class Cache:

    def create(name:str, type:str = "other",path:str = '/cache/'):
        with open(f"{type}_{name}.csv", 'w', newline='', encoding='utf-8') as arquivo:
            arquivo.write('')



Cache.create('testando')