from tkinter import Toplevel

import customtkinter

# # ### Funções
# #
# # def login():
# #     frame_ola.tkraise(aboveThis=frame_login)
# #
# # def inscrevase():
# #     frame_login.tkraise(aboveThis=frame_ola)
# #
# # def teste():
# #     frame_login.tkraise(aboveThis=frame_ola)
#
#
# # ### Cores
# # cinza_escuro = "#1E1E1E"
# # branco = "#fff"
# # cinza_claro= "#2d2d2d"
# # cinza_placeholder = "#969696"
# # azul = "#006fff"
# # azul_claro = "#32ADE6"
#
# ### Janela
#
#
#
#
#
# # ### Imagem de fundo
# # criar_imagem_fundo = CTkImage(
# #     dark_image=Image.open("assets/login/imagem_fundo.png"),
# #     light_image=Image.open("assets/login/imagem_fundo.png"),
# #     size=(900, 600))
# # lbl_imagem_fundo = CTkLabel(
# #     janela,
# #     image=criar_imagem_fundo,
# #     text="")
# # lbl_imagem_fundo.place(x=0,y=0)
#

#
# lbl_teste = CTkLabel(
#     frame_ola,
#     text="isso é um teste",
#     fg_color=cinza_escuro,
#     bg_color=cinza_escuro,
#     text_color=branco,
#     font=("Roboto Bold", 48 * -1, "bold"),
# )
# lbl_teste.pack(padx=20,pady=20)
#
# ### Botão login
# btn_teste = CTkButton(
#     frame_ola,
#     command=teste,
#     corner_radius=15,
#     border_width=0,
#     width=238,
#     height=43,
#     fg_color=azul,
#     bg_color=cinza_escuro,
#     text_color=branco,
#     text="Voltar",
#     font = ("Roboto Bold", 20 * -1, "bold"),
#     cursor="hand2",
# )
# btn_teste.pack(padx=20,pady=20)
#
# ### Fundo login
# frame_login = CTkFrame(
#     janela,
#     height=600,
#     width=400,
#     fg_color=cinza_escuro,
#     bg_color=cinza_escuro)
# frame_login.place(x=500,y=0)
#
# ### Texto entrar
# lbl_entrar = CTkLabel(
#     frame_login,
#     text="Entrar",
#     fg_color=cinza_escuro,
#     bg_color=cinza_escuro,
#     text_color=branco,
#     font=("Roboto Bold", 48 * -1, "bold"),
# )
# lbl_entrar.place(x=135,y=73)
#
# ### Entradas
# ent_usuario = CTkEntry(
#     frame_login,
#     bg_color=cinza_escuro,
#     fg_color=cinza_claro,
#     border_width=0,
#     corner_radius=7,
#     placeholder_text="Usuário",
#     placeholder_text_color=cinza_placeholder,
#     text_color=branco,
#     width=238,
#     height=44,
#     font=("Roboto Bold", 16 * -1, "bold"),
# )
# ent_usuario.place(x=81,y=199)
#
# ent_senha = CTkEntry(
#     frame_login,
#     bg_color=cinza_escuro,
#     fg_color=cinza_claro,
#     border_width=0,
#     corner_radius=7,
#     placeholder_text="Senha",
#     placeholder_text_color=cinza_placeholder,
#     text_color=branco,
#     width=238,
#     height=44,
#     show="●",
#     font=("Roboto Bold", 16 * -1, "bold"),
# )
# ent_senha.place(x=81,y=256)
#
# ent_dois_fat = CTkEntry(
#     frame_login,
#     bg_color=cinza_escuro,
#     fg_color=cinza_claro,
#     border_width=0,
#     corner_radius=7,
#     placeholder_text="Dois fatores",
#     placeholder_text_color=cinza_placeholder,
#     text_color=branco,
#     width=238,
#     height=44,
#     font=("Roboto Bold", 16 * -1, "bold"),
# )
# ent_dois_fat.place(x=81,y=313)
#
# ### Botão login
# btn_login = CTkButton(
#     frame_login,
#     command=login,
#     corner_radius=15,
#     border_width=0,
#     width=238,
#     height=43,
#     fg_color=azul,
#     bg_color=cinza_escuro,
#     text_color=branco,
#     text="Login",
#     font = ("Roboto Bold", 20 * -1, "bold"),
#     cursor="hand2",
# )
# btn_login.place(x=81,y=408)
#
# ### Label não tem conta
# lbl_nconta = CTkLabel(
#     frame_login,
#     text="Não tem conta?",
#     fg_color=cinza_escuro,
#     bg_color=cinza_escuro,
#     text_color=branco,
#     font=("Roboto Bold", 14 * -1, "bold"),
# )
# lbl_nconta.place(x=102,y=474)
#
# ### Botão inscreva-se
# btn_inscrevase = CTkButton(
#     frame_login,
#     command=inscrevase,
#     border_width=0,
#     width=74,
#     height=16,
#     fg_color=cinza_escuro,
#     bg_color=cinza_escuro,
#     text_color=azul_claro,
#     text="Inscreva-se",
#     font=("Roboto Bold", 14 * -1, "bold"),
#     hover_color=cinza_escuro,
#     cursor="hand2",
# )
# btn_inscrevase.place(x=205,y=474)
#
#
#
#
#
#
#
#
#
#


class Frameola(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(
            height=600,
            width=400,
            corner_radius=0,
            fg_color="#006fff")
        self.lbl_teste = customtkinter.CTkLabel(self,text="Esta é a primeira tela")
        self.lbl_teste.place(x=20,y=20)
        self.btn_segunda = customtkinter.CTkButton(self, text="ir", command=self.botao2)
        self.btn_segunda.place(x=81,y=408)

    def botao2(self):
        janela.atv_tchau()


class Frametchau(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(
            height=600,
            width=400,
            corner_radius=0,
            fg_color="#ff0000")
        self.lbl_teste = customtkinter.CTkLabel(self,text="Esta é a segunda tela")
        self.lbl_teste.place(x=20,y=20)
        self.btn_segunda = customtkinter.CTkButton(self, text="Voltar", command=self.botao1)
        self.btn_segunda.place(x=81,y=408)
    def botao1(self):
        janela.atv_ola()


class janela(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("900x600")
        self.resizable(False, False)
        self._set_appearance_mode("dark")
        self.frame_ola = Frameola(self)
        self.frame_ola.place(x=500,y=0)
        self.frame_tchau = Frametchau(self)
        self.frame_tchau.place(x=500,y=0)

    def atv_ola(self):
        self.frame_tchau.place_forget()
        self.frame_ola.place(x=500,y=0)

    def atv_tchau(self):
        self.frame_ola.place_forget()
        self.frame_tchau.place(x=500,y=0)


janela = janela()



janela.mainloop()