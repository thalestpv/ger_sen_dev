
#imports necessários
import customtkinter as ctk
import random
import string
from customtkinter import *
from PIL import Image, ImageTk
import pyotp
import qrcode
import sqlite3
from hashlib import sha256
import string as st
import numpy as np
from tkinter import messagebox, ttk
#from ger_sen_dev.login import ent_senha
import hashlib
import tkinter

#CRIA UMA TABELA PARA OS DADOS DO CADASTRO
def cadastro_db(self):
    cursor = self.conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS cadastro (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        chave_2fa TEXT NOT NULL,
        usuario TEXT NOT NULL,
        senha TEXT NOT NULL,
    )
    ''')
    self.conn.commit()

#CADASTRA OS DADOS DAS ENTRADAS E CRIA O QRCODE COM A CHAVE 2FA
def cadastro_db(self):
    # Validações básicas
    usuario = self.ent_usuario.get().strip()
    senha = self.ent_senha.get()
    senha_repetida = self.ent_repsen.get()

    # Verificar se todos os campos foram preenchidos
    if not usuario or not senha or not senha_repetida:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos!")
        return False

    # Verificar se as senhas coincidem
    if senha != senha_repetida:
        messagebox.showerror("Erro", "As senhas não coincidem!")
        return False

    # Verificar se o usuário já existe
    cursor = self.conn.cursor()
    cursor.execute('SELECT usuario FROM cadastro WHERE usuario = ?', (usuario,))
    if cursor.fetchone():
        messagebox.showerror("Erro", "Este usuário já está cadastrado!")
        return False

    try:
        # Gerar chave 2FA
        chave_2fa = pyotp.random_base32()

        # Criar URI para o QR Code
        totp = pyotp.TOTP(chave_2fa)
        uri = totp.provisioning_uri(usuario, issuer_name="SeuApp")

        # Gerar QR Code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(uri)
        qr.make(fit=True)

        # Criar imagem do QR Code
        qr_image = qr.make_image(fill_color="black", back_color="white")

        # Converter para formato PhotoImage do Tkinter
        qr_image = qr_image.resize((200, 200))  # Redimensionar para um tamanho adequado
        qr_photo = ImageTk.PhotoImage(qr_image)

        # Criar uma nova janela para mostrar o QR Code
        qr_window = CTkToplevel(self)
        qr_window.title("Configure 2FA")
        qr_window.geometry("400x500")

        # Adicionar QR Code e instruções na janela
        CTkLabel(qr_window, text="Configure a Autenticação de Dois Fatores",
                 font=("Roboto Bold", 16)).pack(pady=10)

        qr_label = tkinter.Label(qr_window, image=qr_photo)
        qr_label.image = qr_photo  # Manter referência
        qr_label.pack(pady=10)

        CTkLabel(qr_window, text="1. Abra seu aplicativo de autenticação\n" +
                                 "2. Escaneie o QR Code acima\n" +
                                 "3. Guarde sua chave de backup:",
                 font=("Roboto", 12)).pack(pady=10)

        # Mostrar a chave em texto para backup
        chave_entry = CTkEntry(qr_window, width=300)
        chave_entry.insert(0, chave_2fa)
        chave_entry.configure(state="readonly")
        chave_entry.pack(pady=10)

        # Hash da senha para segurança
        senha_hash = hashlib.sha256(senha.encode()).hexdigest()

        # Inserir novo usuário
        cursor.execute('''
            INSERT INTO cadastro (usuario, senha, chave_2fa)
            VALUES (?, ?, ?)
        ''', (usuario, senha_hash, chave_2fa))

        self.conn.commit()
        messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")

        # Limpar os campos após cadastro
        self.ent_usuario.delete(0, 'end')
        self.ent_senha.delete(0, 'end')
        self.ent_repsen.delete(0, 'end')

        return True

    except sqlite3.Error as e:
        messagebox.showerror("Erro", f"Erro ao cadastrar: {str(e)}")
        self.conn.rollback()
        return False

    finally:
        cursor.close()

#VALIDA OS DADOS ENVIADOS NO LOGIN
def validar_login(self):
    # Obter valores das entradas
    usuario = self.ent_usuario.get().strip()
    senha = self.ent_senha.get()
    codigo_2fa = self.ent_dois_fat.get().strip()

    # Verificar se todos os campos foram preenchidos
    if not usuario or not senha or not codigo_2fa:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos!")
        return False

    try:
        cursor = self.conn.cursor()

        # Criar hash da senha para comparação
        senha_hash = hashlib.sha256(senha.encode()).hexdigest()

        # Buscar usuário no banco
        cursor.execute('''
            SELECT usuario, senha, chave_2fa 
            FROM cadastro 
            WHERE usuario = ? AND senha = ?
        ''', (usuario, senha_hash))

        resultado = cursor.fetchone()

        if not resultado:
            messagebox.showerror("Erro", "Usuário ou senha inválidos!")
            return False

        # Verificar código 2FA
        chave_2fa = resultado[2]  # Índice 2 corresponde à coluna chave_2fa
        totp = pyotp.TOTP(chave_2fa)

        if not totp.verify(codigo_2fa):
            messagebox.showerror("Erro", "Código de autenticação inválido!")
            return False

        # Se chegou aqui, login foi bem-sucedido
        messagebox.showinfo("Sucesso", "Login realizado com sucesso!")

        # Limpar campos
        self.ent_usuario.delete(0, 'end')
        self.ent_senha.delete(0, 'end')
        self.ent_dois_fat.delete(0, 'end')

        return True

    except sqlite3.Error as e:
        messagebox.showerror("Erro", f"Erro ao validar login: {str(e)}")
        return False

    finally:
        cursor.close()




#CRIA AS PÁGINAS 3 E 4 (BANCO DE SENHAS E ALTERAÇÕES)
    def show_db(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
#cria a página do banco de senhas e modificações
class GerenciadorSenhas(CTkFrame):
    def __init__(self, master, controller):
        CTkFrame.__init__(self, master)
        # Inicializar o banco de dados
        self.inicializar_banco()

        # Configuração da janela principal
        self.janela = ctk.CTk()
        self.janela.title("Gerenciador de Senhas")
        self.janela.geometry("800x600")

        # Frame para os botões superiores
        self.frame_botoes = ctk.CTkFrame(self.janela)
        self.frame_botoes.pack(fill="x", padx=10, pady=5)

        # Botões superiores
        self.btn_adicionar = ctk.CTkButton(self.frame_botoes, text="Adicionar", command=self.adicionar)
        self.btn_adicionar.pack(side="left", padx=5)

        self.btn_remover = ctk.CTkButton(self.frame_botoes, text="Remover", command=self.remover)
        self.btn_remover.pack(side="left", padx=5)

        self.btn_alterar = ctk.CTkButton(self.frame_botoes, text="Alterar", command=self.alterar)
        self.btn_alterar.pack(side="left", padx=5)

        self.btn_atualizar = ctk.CTkButton(self.frame_botoes, text="Atualizar Tabela", command=self.atualizar_tabela)
        self.btn_atualizar.pack(side="left", padx=5)

        # Frame para as entradas
        self.frame_entradas = ctk.CTkFrame(self.janela)
        self.frame_entradas.pack(fill="x", padx=10, pady=5)

        # Labels e entradas
        ctk.CTkLabel(self.frame_entradas, text="Site:").pack(side="left", padx=5)
        self.entrada_site = ctk.CTkEntry(self.frame_entradas, width=200)
        self.entrada_site.pack(side="left", padx=5)

        ctk.CTkLabel(self.frame_entradas, text="Usuário:").pack(side="left", padx=5)
        self.entrada_usuario = ctk.CTkEntry(self.frame_entradas, width=200)
        self.entrada_usuario.pack(side="left", padx=5)

        ctk.CTkLabel(self.frame_entradas, text="Senha:").pack(side="left", padx=5)
        self.entrada_senha = ctk.CTkEntry(self.frame_entradas, width=200)  # Removido show="*"
        self.entrada_senha.pack(side="left", padx=5)

        # Frame para a tabela
        self.frame_tabela = ctk.CTkFrame(self.janela)
        self.frame_tabela.pack(fill="both", expand=True, padx=10, pady=5)

        # Criar Treeview para mostrar os dados
        self.tree = ttk.Treeview(self.frame_tabela, columns=("Site", "Usuário", "Senha"), show="headings")
        self.tree.heading("Site", text="Site")
        self.tree.heading("Usuário", text="Usuário")
        self.tree.heading("Senha", text="Senha")

        # Ajustar largura das colunas
        self.tree.column("Site", width=200)
        self.tree.column("Usuário", width=200)
        self.tree.column("Senha", width=200)

        # Adicionar scrollbar
        scrollbar = ttk.Scrollbar(self.frame_tabela, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Posicionar tree e scrollbar
        scrollbar.pack(side="right", fill="y")
        self.tree.pack(fill="both", expand=True)

        # Adicionar evento de clique na tabela
        self.tree.bind("<ButtonRelease-1>", self.selecionar_item)

        # Frame para o gerador de senha
        self.frame_gerador = ctk.CTkFrame(self.janela)
        self.frame_gerador.pack(fill="x", padx=10, pady=5)

        # Gerador de senha
        self.btn_gerar = ctk.CTkButton(self.frame_gerador, text="Gerar Senha", command=self.gerar_senha)
        self.btn_gerar.pack(pady=5)

        # Botão de sair (canto inferior esquerdo)
        self.btn_sair = ctk.CTkButton(self.janela, text="Sair", command=self.janela.destroy)
        self.btn_sair.pack(side="left", padx=10, pady=10)

        # Carregar dados iniciais
        self.atualizar_tabela()

    def inicializar_banco(self):
        self.banco = sqlite3.connect('../lab2/bancosenhas.db')
        self.cursor = self.banco.cursor()

        # Criar tabela se não existir
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS registros (
                site TEXT,
                usuario TEXT,
                senha TEXT
            )
        ''')
        self.banco.commit()

    def atualizar_tabela(self):
        # Limpar tabela atual
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Buscar dados do banco
        self.cursor.execute('SELECT * FROM registros')
        for registro in self.cursor.fetchall():
            # Mostrar a senha sem máscara
            self.tree.insert('', 'end', values=registro)

    def selecionar_item(self, event):
        # Obter item selecionado
        item_selecionado = self.tree.selection()
        if item_selecionado:
            # Obter valores do item
            valores = self.tree.item(item_selecionado)['values']

            # Limpar campos
            self.limpar_campos()

            # Preencher campos com valores selecionados
            self.entrada_site.insert(0, valores[0])
            self.entrada_usuario.insert(0, valores[1])
            self.entrada_senha.insert(0, valores[2])

    def limpar_campos(self):
        self.entrada_site.delete(0, 'end')
        self.entrada_usuario.delete(0, 'end')
        self.entrada_senha.delete(0, 'end')

    def adicionar(self):
        site = self.entrada_site.get()
        usuario = self.entrada_usuario.get()
        senha = self.entrada_senha.get()

        if site and usuario and senha:
            try:
                self.cursor.execute('INSERT INTO registros VALUES (?, ?, ?)',
                                    (site, usuario, senha))
                self.banco.commit()
                messagebox.showinfo("Sucesso", "Registro adicionado com sucesso!")
                self.limpar_campos()
                self.atualizar_tabela()
            except sqlite3.Error as erro:
                messagebox.showerror("Erro", f"Erro ao adicionar registro: {erro}")
        else:
            messagebox.showwarning("Aviso", "Por favor, preencha todos os campos!")

    def remover(self):
        site = self.entrada_site.get()
        usuario = self.entrada_usuario.get()

        if site and usuario:
            try:
                self.cursor.execute('DELETE FROM registros WHERE site = ? AND usuario = ?',
                                    (site, usuario))
                self.banco.commit()

                if self.cursor.rowcount > 0:
                    messagebox.showinfo("Sucesso", "Registro removido com sucesso!")
                    self.limpar_campos()
                    self.atualizar_tabela()
                else:
                    messagebox.showwarning("Aviso", "Registro não encontrado!")
            except sqlite3.Error as erro:
                messagebox.showerror("Erro", f"Erro ao remover registro: {erro}")
        else:
            messagebox.showwarning("Aviso", "Por favor, preencha site e usuário!")

    def alterar(self):
        site = self.entrada_site.get()
        usuario = self.entrada_usuario.get()
        nova_senha = self.entrada_senha.get()

        if site and usuario and nova_senha:
            try:
                self.cursor.execute('''
                    UPDATE registros 
                    SET senha = ? 
                    WHERE site = ? AND usuario = ?
                ''', (nova_senha, site, usuario))
                self.banco.commit()

                if self.cursor.rowcount > 0:
                    messagebox.showinfo("Sucesso", "Senha alterada com sucesso!")
                    self.limpar_campos()
                    self.atualizar_tabela()
                else:
                    messagebox.showwarning("Aviso", "Registro não encontrado!")
            except sqlite3.Error as erro:
                messagebox.showerror("Erro", f"Erro ao alterar senha: {erro}")
        else:
            messagebox.showwarning("Aviso", "Por favor, preencha todos os campos!")

    def gerar_senha(self):
        # Gera uma senha aleatória de 12 caracteres
        caracteres = string.ascii_letters + string.digits + string.punctuation
        senha = ''.join(random.choice(caracteres) for _ in range(12))
        self.entrada_senha.delete(0, 'end')
        self.entrada_senha.insert(0, senha)

    def iniciar(self):
        self.janela.mainloop()

    def __del__(self):
        # Garantir que a conexão com o banco seja fechada
        try:
            self.banco.close()
        except:
            pass
