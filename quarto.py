class Quarto:
    def __init__(self, numero, categoria, valor):
        self.numero = numero
        self.categoria = categoria
        self.valor = valor

    def cadastrar_quarto(self, banco):
        query = "INSERT INTO quartos (numero_quarto, categoria, valor_diaria) VALUES (?, ?, ?)"
        sucesso = banco.executar_comando(query, (self.numero, self.categoria, self.valor))
        if sucesso:
            print(f"\n✅ Quarto {self.numero} ({self.categoria}) cadastrado com sucesso!")

    @staticmethod
    def listar_quartos_disponiveis(banco):
        query = "SELECT numero_quarto, categoria, valor_diaria FROM quartos WHERE status = 'Disponível'"
        resultados = banco.buscar_dados(query)

        print("\n--- QUARTOS DISPONÍVEIS ---")
        for q in resultados:
            print(f"Quarto: {q[0]} | Categoria: {q[1]} | Valor: R$ {q[2]:.2f}")
        print("---------------------------")

    @staticmethod
    def excluir_quarto(banco, numero_quarto):
        query = "DELETE FROM quartos WHERE numero_quarto = ?"
        sucesso = banco.executar_comando(query, (numero_quarto,))
        if sucesso:
            print(f"\n✅ Quarto {numero_quarto} excluído com sucesso!")
        else:
            print("\n❌ Erro ao excluir o quarto.")