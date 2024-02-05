from os.path import exists
from sqlite3 import connect, Error
from core.Log import Log

class Database:
    """
    A classe Database fornece métodos para gerenciar um banco de dados SQLite.
    """

    db = "Database.db"

    @staticmethod
    def checkFile():
        """
        Verifica se o arquivo do banco de dados existe e o cria se não existir.
        """
        if not exists(Database.db):
            with open(Database.db, 'w', newline='', encoding='utf-8') as file:
                file.write('')
        Database.checkTable()

    @staticmethod
    def create_table(table_name, table_columns):
        """
        Cria uma tabela no banco de dados se ela não existir.

        Args:
            table_name (str): O nome da tabela.
            table_columns (str): As colunas da tabela no formato SQL.

        Exemplo:
            create_table("users", "id INTEGER PRIMARY KEY, name TEXT")
        """
        verify = Database.select(f"SELECT name FROM sqlite_master WHERE type='table'")
        if verify is None or table_name not in (t[0] for t in verify):
            query = f"CREATE TABLE {table_name} ({table_columns})"
            Database.insert(query)
            if table_name == "action":
                query = f"INSERT INTO action (`name`, `function`) VALUES('None', 'None')"
                Database.insert(query)

    @staticmethod
    def checkTable():
        """
        Verifica e cria tabelas essenciais no banco de dados.
        """
        Database.create_table("category", '''
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT CHECK(LENGTH(name) <= 50)
        ''')

        Database.create_table("routes", '''
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            category_id INTEGER,
            start TEXT,
            end TEXT,
            active BOOLEAN,
            FOREIGN KEY (category_id) REFERENCES category (id)
        ''')

        Database.create_table("action", '''
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            function TEXT CHECK(LENGTH(name) <= 50)
        ''')

        Database.create_table("movements", '''
            routes_id INTEGER,
            order_id INTEGER,
            version INTEGER,
            x INTEGER,
            y INTEGER,
            z INTEGER,
            action_id INTEGER,
            PRIMARY KEY (routes_id, order_id, version),
            FOREIGN KEY (routes_id) REFERENCES routes (id),
            FOREIGN KEY (action_id) REFERENCES action (id)
        ''')

    @staticmethod
    def insert(query_string, params=None):
        """
        Executa uma operação de inserção/alteração/exclusão no banco de dados.

        Args:
            query_string (str): A consulta SQL a ser executada.
            params (tuple): Parâmetros para substituir os placeholders na consulta.

        Exemplo:
            insert("INSERT INTO users (name) VALUES (?)", ("John",))
        """
        try:
            connection = connect(Database.db)
            cursor = connection.cursor()
            if params:
                cursor.execute(query_string, params)
            else:
                cursor.execute(query_string)
            connection.commit()
        except Error as e:
            Log(f"Erro ao executar a query: {e}", "Error")
        finally:
            connection.close()
                    
    @staticmethod
    def select(query_string):
        """
        Executa uma operação de seleção no banco de dados.

        Args:
            query_string (str): A consulta SQL a ser executada.

        Returns:
            tuple: A primeira linha do resultado da consulta.
        """
        with connect(Database.db) as connection:
            cursor = connection.cursor()
            cursor.execute(query_string)
            result = cursor.fetchone()
        return result

    @staticmethod
    def select_all(query_string):
        """
        Executa uma operação de seleção no banco de dados, retornando todas as linhas.

        Args:
            query_string (str): A consulta SQL a ser executada.

        Returns:
            list: Lista contendo todas as linhas do resultado da consulta.
        """
        with connect(Database.db) as connection:
            cursor = connection.cursor()
            cursor.execute(query_string)
            result = cursor.fetchall()
        return result

    @staticmethod
    def getAction():
        """
        Obtém todas as entradas da tabela 'action'.

        Returns:
            list: Lista contendo todas as entradas da tabela 'action'.
        """
        return Database.select_all("SELECT * FROM action")

    @staticmethod
    def setAction(name: str, function: str):
        """
        Insere uma nova entrada na tabela 'action'.

        Args:
            name (str): Nome da ação.
            function (str): Função associada à ação.
        """
        string = f"INSERT INTO action(`name`, `function`) VALUES ('{name}', '{function}')"
        Database.insert(string)

    @staticmethod
    def removeAction(id: int):
        """
        Remove uma entrada da tabela 'action' com base no ID.

        Args:
            id (int): ID da entrada a ser removida.
        """
        string = f"DELETE FROM action WHERE id={id};"
        Database.insert(string)

    @staticmethod
    def getCategory():
        """
        Obtém todas as entradas da tabela 'category'.

        Returns:
            list: Lista contendo todas as entradas da tabela 'category'.
        """
        return Database.select_all("SELECT * FROM category")

    # ... (continua para os métodos restantes)

    @staticmethod
    def setRoutes(name: str, category: int, start: tuple, end: tuple):
        """
        Insere uma nova entrada na tabela 'routes'.

        Args:
            name (str): Nome da rota.
            category (int): ID da categoria associada à rota.
            start (tuple): Coordenadas de início da rota.
            end (tuple): Coordenadas de fim da rota.
        """
        start_str = ','.join(map(str, start))
        end_str = ','.join(map(str, end))
        query = "INSERT INTO routes (`name`, `category_id`, `start`, `end`) VALUES (?, ?, ?, ?)"
        params = (name, category, start_str, end_str)
        Database.insert(query, params)

    @staticmethod
    def removeRoutes(id: int):
        """
        Remove uma entrada da tabela 'routes' com base no ID.

        Args:
            id (int): ID da entrada a ser removida.
        """
        string = f"DELETE FROM routes WHERE id={id};"
        Database.insert(string)

    @staticmethod
    def getMovements(router: int, version: int = 1):
        """
        Obtém todas as entradas da tabela 'movements' para um roteador e versão específicos.

        Args:
            router (int): ID do roteador.
            version (int): Número da versão (padrão é 1).

        Returns:
            list: Lista contendo todas as entradas correspondentes.
        """
        return Database.select_all(f"SELECT * FROM movements WHERE routes_Id = {router} and version = {version}")

    @staticmethod
    def setMovements(router: int, version: int, x: int, y: int, z: int, action_id: int = 1):
        """
        Insere uma nova entrada na tabela 'movements'.

        Args:
            router (int): ID do roteador associado ao movimento.
            version (int): Número da versão do movimento.
            x (int): Coordenada x do movimento.
            y (int): Coordenada y do movimento.
            z (int): Coordenada z do movimento.
            action_id (int): ID da ação associada ao movimento (padrão é 1).
        """
        string = f"INSERT INTO movements(routes_id, order_id, version, x, y, z, action_id) VALUES " \
                 f"({router}, {version}, {x}, {y}, {z}, {action_id})"
        Database.insert(string)
    
    @staticmethod
    def removeMovements(id: int, version: int):
        """
        Remove uma entrada da tabela 'movements' com base no ID do roteador e na versão.

        Args:
            id (int): ID do roteador associado ao movimento.
            version (int): Número da versão do movimento.
        """
        string = f"DELETE FROM movements WHERE routes_id={id} and version = {version};"
        Database.insert(string)