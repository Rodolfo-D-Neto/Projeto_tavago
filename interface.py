import customtkinter as ctk
from tkinter import messagebox
from database import ConexaoSQLite
from cliente import Cliente
from quarto import Quarto

# Configuração visual global
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class PainelPrincipal(ctk.CTk):
    def __init__(self, nivel_acesso):
        super().__init__()

        self.title("Sistema Tá Vago - Dashboard")
        self.geometry("1000x650")  # Janela um pouco maior para acomodar tudo
        self.nivel_acesso = nivel_acesso

        # Configurando o Grid da janela (1 linha, 2 colunas)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # ==========================================
        # FRAME DO MENU LATERAL (Esquerda com Rolagem)
        # ==========================================
        # Trocamos CTkFrame por CTkScrollableFrame para caber os 11 botões
        self.frame_menu = ctk.CTkScrollableFrame(self, width=260, corner_radius=0)
        self.frame_menu.grid(row=0, column=0, sticky="nsew")

        # Cabeçalho do Menu
        ctk.CTkLabel(self.frame_menu, text="TÁ VAGO", font=("Segoe UI", 20, "bold")).pack(pady=(10, 0))
        ctk.CTkLabel(self.frame_menu, text=f"Perfil: {self.nivel_acesso.upper()}", font=("Segoe UI", 11)).pack(
            pady=(0, 20))

        # --- REPLICANDO O MENU DO TERMINAL ---

        ctk.CTkButton(self.frame_menu, text="1 - Cadastrar Novo Hóspede", anchor="w",
                      command=lambda: self.mostrar_tela("Cadastrar Novo Hóspede")).pack(pady=5, padx=10, fill="x")

        ctk.CTkButton(self.frame_menu, text="2 - Cadastrar Novo Quarto", anchor="w",
                      command=lambda: self.mostrar_tela("Cadastrar Novo Quarto")).pack(pady=5, padx=10, fill="x")

        ctk.CTkButton(self.frame_menu, text="3 - Check-in de Hóspede", anchor="w",
                      command=lambda: self.mostrar_tela("Check-in de Hóspede")).pack(pady=5, padx=10, fill="x")

        ctk.CTkButton(self.frame_menu, text="4 - Check-out de Hóspede", anchor="w",
                      command=lambda: self.mostrar_tela("Check-out de Hóspede")).pack(pady=5, padx=10, fill="x")

        ctk.CTkButton(self.frame_menu, text="5 - Consultar Quartos Disponíveis", anchor="w",
                      command=lambda: self.mostrar_tela("Consultar Quartos Disponíveis")).pack(pady=5, padx=10,
                                                                                               fill="x")

        ctk.CTkButton(self.frame_menu, text="6 - Consultar Reserva", anchor="w",
                      command=lambda: self.mostrar_tela("Consultar Reserva")).pack(pady=5, padx=10, fill="x")

        # Botões de Exclusão (Destacados em vermelho suave)
        ctk.CTkButton(self.frame_menu, text="7 - Excluir Cadastro de Hóspede", anchor="w", fg_color="#A82020",
                      hover_color="#8B0000",
                      command=lambda: self.mostrar_tela("Excluir Cadastro de Hóspede")).pack(pady=5, padx=10, fill="x")

        ctk.CTkButton(self.frame_menu, text="8 - Excluir Quarto Cadastrado", anchor="w", fg_color="#A82020",
                      hover_color="#8B0000",
                      command=lambda: self.mostrar_tela("Excluir Quarto Cadastrado")).pack(pady=5, padx=10, fill="x")

        ctk.CTkButton(self.frame_menu, text="9 - Pesquisar Cliente", anchor="w",
                      command=lambda: self.mostrar_tela("Pesquisar Cliente")).pack(pady=5, padx=10, fill="x")

        ctk.CTkButton(self.frame_menu, text="10 - Reservar Quarto", anchor="w",
                      command=lambda: self.mostrar_tela("Reservar Quarto")).pack(pady=5, padx=10, fill="x")

        # Botão 11 (Sair)
        ctk.CTkButton(self.frame_menu, text="11 - Sair do Sistema", fg_color="transparent", border_width=1,
                      command=self.destroy).pack(pady=(20, 10), padx=10, fill="x")

        # ==========================================
        # FRAME DE CONTEÚDO (Direita)
        # ==========================================
        self.frame_conteudo = ctk.CTkFrame(self, corner_radius=10)
        self.frame_conteudo.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        # Inicia mostrando a tela principal (Visão Geral)
        self.mostrar_home()

    # --- FUNÇÕES DE CONTROLE DA INTERFACE ---

    def limpar_conteudo(self):
        """Remove os widgets anteriores da tela da direita."""
        for widget in self.frame_conteudo.winfo_children():
            widget.destroy()

    def mostrar_home(self):
        self.limpar_conteudo()
        ctk.CTkLabel(self.frame_conteudo, text="Bem-vindo ao Sistema Hoteleiro", font=("Segoe UI", 24, "bold")).pack(
            pady=50)
        ctk.CTkLabel(self.frame_conteudo, text="Selecione uma opção no menu lateral para iniciar.").pack()

    def mostrar_tela(self, titulo_modulo):
        """Roteador: Decide qual formulário desenhar na tela da direita."""
        self.limpar_conteudo()

        # Título padrão no topo
        ctk.CTkLabel(self.frame_conteudo, text=titulo_modulo, font=("Segoe UI", 22, "bold")).pack(pady=(20, 30))

        # Roteamento baseado no nome do botão clicado
        if titulo_modulo == "Cadastrar Novo Hóspede":
            self.desenhar_form_cadastro_hospede()

        elif titulo_modulo == "Cadastrar Novo Quarto":
            self.desenhar_form_cadastro_quarto()

        elif titulo_modulo == "Pesquisar Cliente":
            self.desenhar_form_pesquisa_cliente()

        else:
            # Tela padrão para funcionalidades ainda não implementadas
            ctk.CTkLabel(self.frame_conteudo, text="Formulário em construção...", text_color="gray").pack(pady=10)

    # ==========================================
    # CONSTRUTORES DE FORMULÁRIOS
    # ==========================================

    def desenhar_form_cadastro_hospede(self):
        """Desenha os campos e conecta a classe Cliente ao Banco de Dados com rastreio de erros."""
        form_frame = ctk.CTkFrame(self.frame_conteudo, fg_color="transparent")
        form_frame.pack(pady=10)

        entry_nome = ctk.CTkEntry(form_frame, placeholder_text="Nome Completo", width=300)
        entry_nome.pack(pady=8)

        entry_cpf = ctk.CTkEntry(form_frame, placeholder_text="CPF (Apenas números)", width=300)
        entry_cpf.pack(pady=8)

        entry_telefone = ctk.CTkEntry(form_frame, placeholder_text="Telefone", width=300)
        entry_telefone.pack(pady=8)

        entry_email = ctk.CTkEntry(form_frame, placeholder_text="E-mail", width=300)
        entry_email.pack(pady=8)

        entry_endereco = ctk.CTkEntry(form_frame, placeholder_text="Endereço", width=300)
        entry_endereco.pack(pady=8)

        def acao_salvar():
            try:
                print("DEBUG: Botão clicado, capturando dados...")
                nome = entry_nome.get()
                cpf = entry_cpf.get()
                telefone = entry_telefone.get()
                email = entry_email.get()
                endereco = entry_endereco.get()

                if not nome or not cpf:
                    messagebox.showwarning("Aviso", "Nome e CPF são campos obrigatórios!")
                    return

                print(f"DEBUG: Instanciando banco e classe para: {nome}")
                banco = ConexaoSQLite("ta_vago.db")
                novo_cliente = Cliente(nome, cpf, telefone, email, endereco)

                print("DEBUG: Executando método cadastrar...")
                sucesso = novo_cliente.cadastrar(banco)
                print(f"DEBUG: Retorno do cadastro foi: {sucesso}")

                if sucesso:
                    messagebox.showinfo("Sucesso", f"O hóspede {nome} foi cadastrado!")
                    entry_nome.delete(0, 'end')
                    entry_cpf.delete(0, 'end')
                    entry_telefone.delete(0, 'end')
                    entry_email.delete(0, 'end')
                    entry_endereco.delete(0, 'end')
                else:
                    messagebox.showerror("Erro", "Não foi possível cadastrar no banco.")

            except Exception as e:
                print(f"ERRO CRÍTICO CAPTURADO: {e}")
                messagebox.showerror("Erro de Execução", f"Ocorreu um erro:\n{e}")

        ctk.CTkButton(form_frame, text="Salvar Hóspede no Sistema", fg_color="green", hover_color="darkgreen",
                      command=acao_salvar, width=300).pack(pady=20)

    def desenhar_form_pesquisa_cliente(self):
        """Desenha o campo de busca e a área de resultados."""
        form_frame = ctk.CTkFrame(self.frame_conteudo, fg_color="transparent")
        form_frame.pack(pady=10)

        entry_cpf_busca = ctk.CTkEntry(form_frame, placeholder_text="Digite o CPF do cliente", width=300)
        entry_cpf_busca.pack(pady=10)

        # Label vazia onde o resultado vai aparecer depois de clicar no botão
        lbl_resultado = ctk.CTkLabel(form_frame, text="", font=("Segoe UI", 14), justify="left")
        lbl_resultado.pack(pady=20)

        def acao_buscar():
            cpf = entry_cpf_busca.get()

            # Aqui os alunos chamarão: resultado = Cliente.buscar_por_cpf(banco, cpf)
            if cpf == "123":  # Simulação estática para teste
                texto_banco = "Nome: João da Silva\nCPF: 123\nTelefone: (47) 9999-9999\nE-mail: joao@email.com"
                lbl_resultado.configure(text=texto_banco, text_color="white")
            else:
                lbl_resultado.configure(text="Cliente não encontrado no sistema.", text_color="#FF5555")

        ctk.CTkButton(form_frame, text="Buscar Cliente", command=acao_buscar, width=300).pack(pady=10)

    def desenhar_form_cadastro_quarto(self):
        """Desenha os campos para o cadastro de novos quartos e conecta à classe Quarto."""
        form_frame = ctk.CTkFrame(self.frame_conteudo, fg_color="transparent")
        form_frame.pack(pady=10)

        # Entradas de Texto (Entries) específicas para Quarto
        entry_numero = ctk.CTkEntry(form_frame, placeholder_text="Número do Quarto (Ex: 101)", width=300)
        entry_numero.pack(pady=8)

        entry_tipo = ctk.CTkEntry(form_frame, placeholder_text="Categoria (Ex: Luxo, Casal, Solteiro)", width=300)
        entry_tipo.pack(pady=8)

        entry_preco = ctk.CTkEntry(form_frame, placeholder_text="Valor da Diária (Ex: 150.00)", width=300)
        entry_preco.pack(pady=8)

        def acao_salvar_quarto():
            try:
                numero = entry_numero.get()
                tipo = entry_tipo.get()
                preco_texto = entry_preco.get().replace(",", ".")  # Garante compatibilidade com ponto flutuante

                if not numero or not preco_texto:
                    messagebox.showwarning("Aviso", "Número e Preço são campos obrigatórios!")
                    return

                preco = float(preco_texto)

                # Conexão e Inclusão via Classe
                banco = ConexaoSQLite("ta_vago.db")
                novo_quarto = Quarto(numero, tipo, preco)

                # Executa o método de cadastro do quarto
                sucesso = novo_quarto.cadastrar_quarto(banco)

                if sucesso is not False:  # Trata caso o método não retorne booleano explícito
                    messagebox.showinfo("Sucesso", f"O quarto {numero} foi cadastrado com sucesso!")
                    entry_numero.delete(0, 'end')
                    entry_tipo.delete(0, 'end')
                    entry_preco.delete(0, 'end')
                else:
                    messagebox.showerror("Erro",
                                         "Não foi possível cadastrar o quarto. Verifique se o número já existe.")

            except ValueError:
                messagebox.showerror("Erro de Formato", "O campo Preço deve conter apenas números válidos.")
            except Exception as e:
                messagebox.showerror("Erro Crítico", f"Ocorreu um erro:\n{e}")

        # Botão de Ação
        ctk.CTkButton(form_frame, text="Salvar Quarto no Sistema", fg_color="green", hover_color="darkgreen",
                      command=acao_salvar_quarto, width=300).pack(pady=20)


# Para rodar e testar a interface isoladamente
if __name__ == "__main__":
    app = PainelPrincipal(nivel_acesso="admin")
    app.mainloop()