from customtkinter import *


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
        self.configure(
            height=600,
            width=900,
            corner_radius=0,
            fg_color="#ff0000"
        )
        self.lbl_teste = CTkLabel(self, text="tela login")
        self.lbl_teste.place(x=20, y=20)
        self.btn_segunda = CTkButton(self, text="ir", command=lambda: controller.show_frame(FrameGeren))
        self.btn_segunda.place(x=81, y=408)

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
        self.configure(
            height=600,
            width=400,
            corner_radius=0,
            fg_color="#ffa500"
        )
        self.lbl_teste = CTkLabel(self, text="Entrar")
        self.lbl_teste.place(x=20, y=20)
        self.btn_segunda = CTkButton(self, text="Registar", command=lambda: controller.show_login(Registrar))
        self.btn_segunda.place(x=81, y=408)
        self.btn_terceiro = CTkButton(self, text="Login", command=lambda : self.bisa())
        self.btn_terceiro.place(x=81, y=508)

    def bisa(self):
        self.master.master.master.master.show_frame(FrameGeren)
class Registrar(CTkFrame):
    def __init__(self, parent, controller):
        CTkFrame.__init__(self, parent)
        self.configure(
            height=600,
            width=400,
            corner_radius=0,
            fg_color="#008000"
        )
        self.lbl_teste = CTkLabel(self, text="Registrar")
        self.lbl_teste.place(x=20, y=20)
        self.btn_segunda = CTkButton(self, text="voltar", command=lambda: controller.show_login(Entrar))
        self.btn_segunda.place(x=81, y=408)


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
