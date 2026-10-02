import tkinter as tk
from tkinter import messagebox
import sqlite3
from interface import abrir_interface_principal


def validar_login(usuario, senha):
    conn = sqlite3.connect("ta_vago.db")
    cursor = conn.cursor()
    cursor.execute("SELECT nivel_acesso FROM usuarios WHERE nome_usuario = ? AND senha = ?", (usuario, senha))
    resultado = cursor.fetchone()
    conn.close()
    return resultado[0] if resultado else None


def salvar_novo_usuario(user, senha, janela):
    if not user or not senha:
        messagebox.showwarning("Aviso", "Preencha todos os campos!")
        return

    conn = sqlite3.connect("ta_vago.db")
    cursor = conn.cursor()
    try:
        # Por padrão, novos usuários entram como 'recepcao'
        cursor.execute("INSERT INTO usuarios (nome_usuario, senha, nivel_acesso) VALUES (?, ?, ?)",
                       (user, senha, 'recepcao'))
        conn.commit()
        messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
        janela.destroy()
    except sqlite3.IntegrityError:
        messagebox.showerror("Erro", "Este nome de usuário já existe.")
    finally:
        conn.close()


def abrir_janela_cadastro():
    janela_cad = tk.Toplevel()
    janela_cad.title("Cadastro de Usuário")
    janela_cad.geometry("250x200")

    tk.Label(janela_cad, text="Usuário:").pack(pady=5)
    entry_user = tk.Entry(janela_cad)
    entry_user.pack()

    tk.Label(janela_cad, text="Senha:").pack(pady=5)
    entry_pass = tk.Entry(janela_cad, show="*")
    entry_pass.pack()

    tk.Button(janela_cad, text="Salvar",
              command=lambda: salvar_novo_usuario(entry_user.get(), entry_pass.get(), janela_cad)).pack(pady=20)


def tela_login():
    root = tk.Tk()
    root.title("Login - Sistema Tá Vago")
    root.geometry("300x250")

    tk.Label(root, text="Usuário:").pack(pady=5)
    entry_usuario = tk.Entry(root)
    entry_usuario.pack()

    tk.Label(root, text="Senha:").pack(pady=5)
    entry_senha = tk.Entry(root, show="*")
    entry_senha.pack()

    def tentar_logar():
        nivel = validar_login(entry_usuario.get(), entry_senha.get())
        if nivel:
            root.destroy()  # Fecha a janela de login
            abrir_interface_principal(nivel)  # Abre a interface com o menu
        else:
            messagebox.showerror("Erro", "Credenciais inválidas!")

    tk.Button(root, text="Entrar", command=tentar_logar).pack(pady=10)
    tk.Button(root, text="Cadastrar Novo Usuário", command=abrir_janela_cadastro).pack()
    root.mainloop()


if __name__ == "__main__":
    tela_login()