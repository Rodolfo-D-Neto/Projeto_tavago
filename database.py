import sqlite3

class ConexaoSQLite:
    def __init__(self, nome_banco="ta_vago.db"):
        self.nome_banco = nome_banco
        self.conexao = None

    def conectar(self):
        self.conexao = sqlite3.connect(self.nome_banco)

    def desconectar(self):
        if self.conexao:
            self.conexao.close()

    def executar_comando(self, query, parametros=None):
        self.conectar()
        try:
            cursor = self.conexao.cursor()
            if parametros:
                cursor.execute(query, parametros)
            else:
                cursor.execute(query)
            self.conexao.commit()
            return True
        except sqlite3.Error as e:
            print(f"Erro no banco: {e}")
            return False
        finally:
            self.desconectar()

    def buscar_dados(self, query, parametros=None):
        self.conectar()
        try:
            cursor = self.conexao.cursor()
            if parametros:
                cursor.execute(query, parametros)
            else:
                cursor.execute(query)
            return cursor.fetchall()
        finally:
            self.desconectar()

    def criar_tabelas(self):
        """Cria as tabelas caso elas não existam."""
        self.executar_comando("""
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                cpf TEXT UNIQUE,
                telefone TEXT,
                email TEXT,
                endereco TEXT
            )
        """)
        self.executar_comando("""
            CREATE TABLE IF NOT EXISTS quartos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                numero TEXT UNIQUE,
                tipo TEXT,
                preco REAL
            )
        """)
        print("Tabelas verificadas/criadas com sucesso!")

    def inicializar_admin(self):
        # Opcional para garantir o admin inicial
        pass