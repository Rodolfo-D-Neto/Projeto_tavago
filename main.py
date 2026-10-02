from database import ConexaoSQLite
from interface import PainelPrincipal


def main():
    print("Iniciando a infraestrutura do Sistema Tá Vago...")

    # Apontando direto para o arquivo na raiz do projeto
    banco_motel = ConexaoSQLite("ta_vago.db")
    banco_motel.criar_tabelas()  # Agora o método existe e vai funcionar!

    print("Banco de dados pronto! Abrindo a interface gráfica...")

    app = PainelPrincipal(nivel_acesso="admin")
    app.mainloop()

    print("\nSistema encerrado.")


if __name__ == "__main__":
    main()