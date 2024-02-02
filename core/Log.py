from datetime import datetime
from os import mkdir
from os.path import exists

class Log:
    _instance = None  # Armazena a instância única da classe

     def __new__(cls, *args, **kwargs):
        """
        Método especial para criar uma instância única da classe Log (singleton).

        Este método garante que apenas uma instância da classe seja criada e reutilizada.
        Se a instância ainda não existe, cria uma nova. Se já existe, retorna a instância existente.

        Parâmetros:
        - cls: A própria classe (Log).
        - *args: Argumentos posicionais não nomeados.
        - **kwargs: Argumentos nomeados.

        Retorna:
        - Instância única da classe Log.
        """
        if not cls._instance:
            cls._instance = super(Log, cls).__new__(cls)
            cls._instance.__initialized = False
        return cls._instance

    def __init__(self, string: str, category: str = 'Log', path: str = 'logs/', type: str = "log") -> None:
        """
        Inicializa a classe Log e adiciona uma entrada no arquivo de log.

        Parâmetros:
        - string (str): Mensagem a ser registrada no log.
        - category (str): Categoria para o nome do arquivo (padrão é 'Log').
        - path (str): Caminho do diretório onde o arquivo será criado/inserido (padrão é 'logs/').
        - type (str): Extensão do arquivo (padrão é 'log').
        """
        if not self.__initialized:
            Now = datetime.now()
            data = Now.strftime("%d-%m-%Y")

            # Verifica se o diretório existe, se não, cria-o
            if not exists(f"./{path}"):
                mkdir(f"./{path}")

            # Verifica se o arquivo do dia já existe, se não, cria-o
            if not exists(f"{path}/{category}_{data}.{type}"):
                self.create(f"{category}_{data}", path, type)

            # Obtém a data e hora atual para inclusão no log
            dateTime = Now.strftime("%d-%m-%Y %H:%M:%S")

            # Adiciona a entrada no arquivo de log
            with open(f"{path}/{category}_{data}.{type}", 'a', newline='', encoding='utf-8') as file:
                file.write(f"[{category} {dateTime}] {string}\n")

            self.__initialized = True

    @staticmethod
    def create(name: str, path: str = 'logs', type: str = "log"):
        """
        Cria um arquivo de log vazio com o nome especificado.

        Parâmetros:
        - name (str): Nome do arquivo de log.
        - path (str): Caminho do diretório onde o arquivo será criado.
        - type (str): Extensão do arquivo (padrão é 'log').
        """
        with open(f"{path}/{name}.{type}", 'w', newline='', encoding='utf-8') as file:
            file.write('')

# Exemplo de uso
Log("Mensagem de log")
