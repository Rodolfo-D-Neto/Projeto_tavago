# Projeto Tavago 🏨

Sistema de gestão hoteleira/motel desenvolvido em Python. O projeto utiliza uma arquitetura modularizada para separar a interface gráfica, as regras de negócio e a persistência de dados utilizando SQLite.

## 📁 Arquitetura do Projeto

O código foi dividido em vários módulos (ficheiros `.py`) para facilitar a manutenção e a legibilidade:

*   **`main.py`**: O ficheiro principal do projeto. É o ponto de entrada (bootstrapping) onde a aplicação é iniciada.
*   **`database.py`**: O "Porteiro" do sistema. Gere a conexão direta com a base de dados SQLite (`ta_vago.db`), executando as queries de inserção, leitura, atualização e eliminação.
*   **`interface.py`**: A "Janela" da aplicação. Responsável por desenhar os menus, formulários e toda a interação visual com o utilizador.
*   **`login.py`**: Gere a autenticação e o controlo de acesso dos utilizadores ao sistema.
*   **`cliente.py`**: Contém a classe e as regras de negócio relacionadas com o registo e gestão dos clientes.
*   **`quarto.py`**: Gere as entidades dos quartos, incluindo a sua disponibilidade, categorias e preços.
*   **`reserva.py`**: Responsável por processar a lógica das reservas, interligando clientes aos quartos disponíveis.

## 🛠️ Tecnologias Utilizadas

*   **Linguagem:** Python 3.x
*   **Base de Dados:** SQLite3 (embutido)
*   **Interface Gráfica:** (Ex: Tkinter / CustomTkinter / PyQt - *ajuste conforme a biblioteca que utilizou*)

## 🚀 Como Executar o Projeto

1.  Clone este repositório para a sua máquina local:
    ```bash
    git clone [https://github.com/Rodolfo-D-Neto/Projeto_tavago.git](https://github.com/Rodolfo-D-Neto/Projeto_tavago.git)
    ```
2.  Navegue até à pasta do projeto:
    ```bash
    cd Projeto_tavago
    ```
3.  Execute o ficheiro principal:
    ```bash
    python main.py
    ```

> **Nota:** A base de dados (`ta_vago.db`) é gerada automaticamente na primeira execução e está configurada para ser ignorada pelo `.gitignore`, garantindo que não são expostos dados locais no repositório.
