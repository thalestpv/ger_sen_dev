from customtkinter import *
from PIL import Image

class Janela(CTk):
    def __init__(self, *args, **kwargs):
        CTk.__init__(self, *args, **kwargs)
        self.geometry("900x600")
        self.resizable(False, False)
        container = CTkFrame(self)
        container.configure(width=900, height=600)
        container._set_appearance_mode("dark")
        container.place(x=0, y=0)
        self.frames = {}
        for F in (FrameLogin, FrameGeren):
            frame = F(container, self)
            self.frames[F] = frame
            frame.place(x=0, y=0)
        self.show_frame(FrameLogin)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()



class FrameLogin(CTkFrame):
    def __init__(self, master, controller):
        CTkFrame.__init__(self, master)
        ### Cores
        cinza_escuro = "#1E1E1E"
        branco = "#fff"
        cinza_claro = "#2d2d2d"
        cinza_placeholder = "#969696"
        azul = "#006fff"
        azul_claro = "#32ADE6"

        self.configure(
            height=600,
            width=900,
            corner_radius=0,
            fg_color=azul,
            bg_color=cinza_escuro,
        )
        # Imagem de fundo
        criar_imagem_fundo = CTkImage(
            dark_image=Image.open("assets/login/imagem_fundo.png"),
            light_image=Image.open("assets/login/imagem_fundo.png"),
            size=(900, 600))
        self.lbl_imagem_fundo = CTkLabel(
            self,
            image=criar_imagem_fundo,
            text="")
        self.lbl_imagem_fundo.place(x=0, y=0)

        container1 = CTkFrame(self)
        container1.configure(width=400, height=600)
        container1._set_appearance_mode("dark")
        container1.place(x=500, y=0)
        self.frames = {}
        for F in (Entrar, Registrar):
            frame = F(container1, self)
            self.frames[F] = frame
            frame.place(x=0, y=0)

        self.show_login(Entrar)

    def show_login(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
class Entrar(CTkFrame):
    def __init__(self, parent, controller):
        CTkFrame.__init__(self, parent)
        cinza_escuro = "#1E1E1E"
        branco = "#fff"
        cinza_claro = "#2d2d2d"
        cinza_placeholder = "#969696"
        azul = "#006fff"
        azul_claro = "#32ADE6"
        self.configure(
        height=600,
        width=400,
        fg_color=cinza_escuro,
        bg_color=cinza_escuro)

        ### Texto entrar
        self.lbl_entrar = CTkLabel(
            self,
            text="Entrar",
            fg_color=cinza_escuro,
            bg_color=cinza_escuro,
            text_color=branco,
            font=("Roboto Bold", 48 * -1, "bold"),
        )
        self.lbl_entrar.place(x=135, y=73)

        ### Entradas
        self.ent_usuario = CTkEntry(
            self,
            bg_color=cinza_escuro,
            fg_color=cinza_claro,
            border_width=0,
            corner_radius=7,
            placeholder_text="Usuário",
            placeholder_text_color=cinza_placeholder,
            text_color=branco,
            width=238,
            height=44,
            font=("Roboto Bold", 16 * -1, "bold"),
        )
        self.ent_usuario.place(x=81, y=199)

        self.ent_senha = CTkEntry(
            self,
            bg_color=cinza_escuro,
            fg_color=cinza_claro,
            border_width=0,
            corner_radius=7,
            placeholder_text="Senha",
            placeholder_text_color=cinza_placeholder,
            text_color=branco,
            width=238,
            height=44,
            show="●",
            font=("Roboto Bold", 16 * -1, "bold"),
        )
        self.ent_senha.place(x=81, y=256)

        self.ent_dois_fat = CTkEntry(
            self,
            bg_color=cinza_escuro,
            fg_color=cinza_claro,
            border_width=0,
            corner_radius=7,
            placeholder_text="Dois fatores",
            placeholder_text_color=cinza_placeholder,
            text_color=branco,
            width=238,
            height=44,
            font=("Roboto Bold", 16 * -1, "bold"),
        )
        self.ent_dois_fat.place(x=81, y=313)

        ### Botão login
        self.btn_login = CTkButton(
            self,
            command=lambda :self.bisa(),
            corner_radius=15,
            border_width=0,
            width=238,
            height=43,
            fg_color=azul,
            bg_color=cinza_escuro,
            text_color=branco,
            text="Login",
            font=("Roboto Bold", 20 * -1, "bold"),
            cursor="hand2",
        )
        self.btn_login.place(x=81, y=408)

        ### Label não tem conta
        self.lbl_nconta = CTkLabel(
            self,
            text="Não tem conta?",
            fg_color=cinza_escuro,
            bg_color=cinza_escuro,
            text_color=branco,
            font=("Roboto Bold", 14 * -1, "bold"),
        )
        self.lbl_nconta.place(x=102, y=474)

        ### Botão inscreva-se
        self.btn_inscrevase = CTkButton(
            self,
            command=lambda :controller.show_login(Registrar),
            border_width=0,
            width=74,
            height=16,
            fg_color=cinza_escuro,
            bg_color=cinza_escuro,
            text_color=azul_claro,
            text="Inscreva-se",
            font=("Roboto Bold", 14 * -1, "bold"),
            hover_color=cinza_escuro,
            cursor="hand2",
        )
        self.btn_inscrevase.place(x=200, y=477)


    def bisa(self):
        self.master.master.master.master.show_frame(FrameGeren)
class Registrar(CTkFrame):
    def __init__(self, parent, controller):
        CTkFrame.__init__(self, parent)
        cinza_escuro = "#1E1E1E"
        branco = "#fff"
        cinza_claro = "#2d2d2d"
        cinza_placeholder = "#969696"
        azul = "#006fff"
        azul_claro = "#32ADE6"
        self.configure(
            height=600,
            width=400,
            fg_color=cinza_escuro,
            bg_color=cinza_escuro)

        ### Label inscreva-se
        self.lbl_inscrevase = CTkLabel(
            self,
            text="Inscreva-se",
            fg_color=cinza_escuro,
            bg_color=cinza_escuro,
            text_color=branco,
            font=("Roboto Bold", 48 * -1, "bold"),
        )
        self.lbl_inscrevase.place(x=74, y=73)

        ### Entradas
        self.ent_usuario = CTkEntry(
            self,
            bg_color=cinza_escuro,
            fg_color=cinza_claro,
            border_width=0,
            corner_radius=7,
            placeholder_text="Usuário",
            placeholder_text_color=cinza_placeholder,
            text_color=branco,
            width=238,
            height=44,
            font=("Roboto Bold", 16 * -1, "bold"),
        )
        self.ent_usuario.place(x=81, y=199)

        self.ent_senha = CTkEntry(
            self,
            bg_color=cinza_escuro,
            fg_color=cinza_claro,
            border_width=0,
            corner_radius=7,
            placeholder_text="Senha",
            placeholder_text_color=cinza_placeholder,
            text_color=branco,
            width=238,
            height=44,
            show="●",
            font=("Roboto Bold", 16 * -1, "bold"),
        )
        self.ent_senha.place(x=81, y=256)

        self.ent_repsen = CTkEntry(
            self,
            bg_color=cinza_escuro,
            fg_color=cinza_claro,
            border_width=0,
            corner_radius=7,
            placeholder_text="Repita a senha",
            placeholder_text_color=cinza_placeholder,
            text_color=branco,
            width=238,
            height=44,
            font=("Roboto Bold", 16 * -1, "bold"),
        )
        self.ent_repsen.place(x=81, y=313)

        ### Botão registrar
        self.btn_registrar = CTkButton(
            self,
            command=lambda : self.btn_registrar,
            corner_radius=15,
            border_width=0,
            width=238,
            height=43,
            fg_color=azul,
            bg_color=cinza_escuro,
            text_color=branco,
            text="Registrar",
            font=("Roboto Bold", 20 * -1, "bold"),
            cursor="hand2",
        )

        self.btn_registrar.place(x=81, y=408)

        ### Label já tem conta?
        self.lbl_nconta = CTkLabel(
            self,
            text="Já tem conta?",
            fg_color=cinza_escuro,
            bg_color=cinza_escuro,
            text_color=branco,
            width=89,
            height=16,
            font=("Roboto Bold", 14 * -1, "bold"),
        )
        self.lbl_nconta.place(x=107, y=474)

        ### Botão voltar
        self.btn_voltar = CTkButton(
            self,
            command=lambda : controller.show_login(Entrar),
            border_width=0,
            width=40,
            height=16,
            fg_color=cinza_escuro,
            bg_color=cinza_escuro,
            text_color=azul_claro,
            text="Voltar",
            font=("Roboto Bold", 14 * -1, "bold"),
            hover_color=cinza_escuro,
            cursor="hand2",
        )
        self.btn_voltar.place(x=200, y=474)


    def btn_registrar(self):
        print("btn_registrar")

class FrameGeren(CTkFrame):
    def __init__(self, parent, controller):
        CTkFrame.__init__(self, parent)
        self.configure(
            height=600,
            width=900,
            corner_radius=0,
            fg_color="#006fff"
        )
        self.lbl_teste = CTkLabel(self, text="tela gerenciador de senhas")
        self.lbl_teste.place(x=20, y=20)
        self.btn_segunda = CTkButton(self, text="voltar", command=lambda: controller.show_frame(FrameLogin))
        self.btn_segunda.place(x=81, y=408)


        container = CTkFrame(self)
        container.configure(width=660, height=600)
        container._set_appearance_mode("dark")
        container.place(x=240, y=0)
        self.frames = {}
        for F in (Pag1, Pag2, Pag3):
            frame = F(container, self)
            self.frames[F] = frame
            frame.place(x=0, y=0)
        self.show_login(Pag1)


        self.btn_pag1 = CTkButton(self, text="Pag1", command=lambda : self.show_login(Pag1))
        self.btn_pag1.place(x=29,y=89)
        self.btn_pag2 = CTkButton(self, text="Pag2", command=lambda : self.show_login(Pag2))
        self.btn_pag2.place(x=29, y=149)
        self.btn_pag3 = CTkButton(self, text="Pag2", command=lambda : self.show_login(Pag3))
        self.btn_pag3.place(x=29, y=209)

    def show_login(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
class Pag1(CTkFrame):
    def __init__(self, parent, controller):
        CTkFrame.__init__(self, parent)
        self.configure(
            height=600,
            width=660,
            corner_radius=0,
            fg_color="#34E5FF"
        )
        self.lbl_teste = CTkLabel(self, text="Pag1")
        self.lbl_teste.place(x=20, y=20)
        self.btn_segunda = CTkButton(self, text="ir para Pag2", command=lambda: controller.show_login(Pag2))
        self.btn_segunda.place(x=81, y=408)
class Pag2(CTkFrame):
    def __init__(self, parent, controller):
        CTkFrame.__init__(self, parent)
        self.configure(
            height=600,
            width=660,
            corner_radius=0,
            fg_color="#E56399"
        )
        self.lbl_teste = CTkLabel(self, text="Pag2")
        self.lbl_teste.place(x=20, y=20)
        self.btn_segunda = CTkButton(self, text="ir para Pag3", command=lambda: controller.show_login(Pag3))
        self.btn_segunda.place(x=81, y=408)
class Pag3(CTkFrame):
    def __init__(self, parent, controller):
        CTkFrame.__init__(self, parent)
        self.configure(
            height=600,
            width=660,
            corner_radius=0,
            fg_color="#7F96FF"
        )
        self.lbl_teste = CTkLabel(self, text="Pag3")
        self.lbl_teste.place(x=20, y=20)
        self.btn_segunda = CTkButton(self, text="ir para Pag1", command=lambda: controller.show_login(Pag1))
        self.btn_segunda.place(x=81, y=408)
app = Janela()


app.mainloop()
