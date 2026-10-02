class Cliente:
    def __init__(self, nome, cpf, telefone, email, endereco):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def cadastrar(self, banco):
        """Envia os dados do cliente para a tabela no banco SQLite."""
        query = """
                INSERT INTO clientes (nome, cpf, telefone, email, endereco)
                VALUES (?, ?, ?, ?, ?) \
                """
        parametros = (self.nome, self.cpf, self.telefone, self.email, self.endereco)

        sucesso = banco.executar_comando(query, parametros)

        if sucesso:
            print(f"\n✅ SUCESSO: O hóspede {self.nome} foi cadastrado no sistema!")

    @staticmethod
    def buscar_por_cpf(banco, cpf_busca):
        """Busca um cliente no banco e exibe seus dados de navegação."""
        query = "SELECT nome, telefone, email, endereco FROM clientes WHERE cpf = ?"
        resultado = banco.buscar_dados(query, (cpf_busca,))

        if resultado:
            # Como o CPF é UNIQUE, sabemos que só vai retornar 1 linha
            dados = resultado[0]
            print("\n🔍 --- CLIENTE ENCONTRADO ---")
            print(f"Nome: {dados[0]}")
            print(f"Telefone: {dados[1]}")
            print(f"E-mail: {dados[2]}")
            print(f"Endereço: {dados[3]}")
            print("----------------------------")
            return True
        else:
            print(f"\n❌ Cadastro não encontrado para o CPF: {cpf_busca}")
            return False

    @staticmethod
    def atualizar_dados(banco, cpf_busca, novo_telefone, novo_email):
        """Atualiza o telefone e o e-mail de um cliente existente."""
        query = "UPDATE clientes SET telefone = ?, email = ? WHERE cpf = ?"
        parametros = (novo_telefone, novo_email, cpf_busca)

        sucesso = banco.executar_comando(query, parametros)
        if sucesso:
            print(f"\n✅ SUCESSO: Dados atualizados para o CPF {cpf_busca}.")

    @staticmethod
    def excluir_cadastro(banco, cpf_busca):
        """Remove permanentemente um cliente do banco de dados."""
        query = "DELETE FROM clientes WHERE cpf = ?"

        sucesso = banco.executar_comando(query, (cpf_busca,))
        if sucesso:
            print(f"\n🗑️ AVISO: O cadastro do CPF {cpf_busca} foi excluído do sistema.")