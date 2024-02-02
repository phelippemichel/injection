from csv import reader
from Log import Log
from os import makedirs, remove
from os.path import exists

class Cache:
    @staticmethod
    def create(name: str, path: str = 'cache', type: str = "csv"):
        """
        Cria um arquivo CSV vazio com o nome especificado.

        Parâmetros:
        - name (str): Nome do arquivo.
        - path (str): Caminho do diretório onde o arquivo será criado.
        - type (str): Extensão do arquivo (padrão é 'csv').
        """
        try:
            with open(f"{path}/{name}.{type}", 'w', newline='', encoding='utf-8') as file:
                file.write('')
        except FileNotFoundError:
            Log(f'O diretório {path} não existe.', "Error")
        except Exception as e:
            Log(f'Ocorreu um erro ao tentar criar o arquivo: {e}', "Error")

    @staticmethod
    def insert(name: str, category: str = "other", array: list = [], path: str = 'cache', type: str = "csv"):
        """
        Insere dados em um arquivo CSV existente ou cria um novo se não existir.

        Parâmetros:
        - name (str): Nome do arquivo.
        - category (str): Categoria para o nome do arquivo (padrão é 'other').
        - array (list): Lista de dados a serem inseridos.
        - path (str): Caminho do diretório onde o arquivo será criado/inserido.
        - type (str): Extensão do arquivo (padrão é 'csv').
        """
        try:
            if not exists(f"./{path}"):
                makedirs(f"./{path}")
            if not exists(f"{path}/{name}.{type}"):
                Cache.create(f"{category}_{name}", path, type)

            with open(f"{path}/{category}_{name}.{type}", 'w', newline='', encoding='utf-8') as file:
                for line in array:
                    file.write(";".join(str(elemento) for elemento in line) + "\n")
        except FileNotFoundError:
            Log(f'O diretório {path} não existe.', "Error")
        except Exception as e:
            Log(f'Ocorreu um erro ao escrever no arquivo: {e}', "Error")

    @staticmethod
    def delete(name: str, path: str = 'cache', type: str = "csv"):
        """
        Deleta um arquivo CSV.

        Parâmetros:
        - name (str): Nome do arquivo.
        - path (str): Caminho do diretório onde o arquivo está localizado.
        - type (str): Extensão do arquivo (padrão é 'csv').
        """
        try:
            if exists(f"./{path}/{name}.{type}"):
                remove(f"./{path}/{name}.{type}")
            else:
                Log(f'O arquivo {name}.{type} não foi encontrado.', "Error")
        except Exception as e:
            Log(f'Ocorreu um erro ao tentar deletar o arquivo {name}.{type}: {e}', "Error")

    @staticmethod
    def load(name: str, path: str = 'cache', type: str = "csv"):
        """
        Carrega um arquivo CSV e retorna os dados como uma lista de listas.

        Parâmetros:
        - name (str): Nome do arquivo.
        - path (str): Caminho do diretório onde o arquivo está localizado.
        - type (str): Extensão do arquivo (padrão é 'csv').

        Retorno:
        - list: Lista de listas contendo os dados do arquivo CSV.
        """
        array = []
        try:
            with open(f"./{path}/{name}.{type}", 'r', newline='', encoding='utf-8') as csv_file:
                reader = reader(csv_file, delimiter=';')
                for linha in reader:
                    array.append(linha)
        except FileNotFoundError:
            Log(f'O arquivo {name}.{type} não foi encontrado.', "Error")
        except Exception as e:
            Log(f'Ocorreu um erro ao tentar carregar o arquivo {name}.{type}: {e}', "Error")

        return array
