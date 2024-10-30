from customtkinter import *
from PIL import Image


class janela(CTk):
    ### Cores
    cinza_escuro = "#1E1E1E"
    branco = "#fff"
    cinza_claro = "#2d2d2d"
    cinza_placeholder = "#969696"
    azul = "#006fff"
    azul_claro = "#32ADE6"

    def __init__(self):
        super().__init__()
        self.geometry("900x600")
        self.resizable(False, False)
        self._set_appearance_mode("dark")
        ### Cores
        cinza_escuro = "#1E1E1E"
        branco = "#fff"
        cinza_claro = "#2d2d2d"
        cinza_placeholder = "#969696"
        azul = "#006fff"
        azul_claro = "#32ADE6"

        ### Frame login
        # frame_login = CTkFrame(
        #     self,
        #     height=900,
        #     width=600,
        #     fg_color=cinza_escuro,
        #     bg_color=cinza_escuro)
        # frame_login.place(x=0,y=0)

    class frame_login(CTkFrame(janela)):
        def __init__(self, master, **kwargs):
            super().__init__(master, **kwargs)
            cinza_escuro = "#1E1E1E"
            branco = "#fff"
            cinza_claro = "#2d2d2d"
            cinza_placeholder = "#969696"
            azul = "#006fff"
            azul_claro = "#32ADE6"

            self.configure(
                self,
                height=900,
                width=600,
                fg_color=cinza_escuro,
                bg_color=cinza_escuro
            )
            self.place(x=0, y=0)

            ### Cores
            cinza_escuro = "#1E1E1E"
            branco = "#fff"
            cinza_claro = "#2d2d2d"
            cinza_placeholder = "#969696"
            azul = "#006fff"
            azul_claro = "#32ADE6"

            # Imagem de fundo
            criar_imagem_fundo = CTkImage(
                dark_image=Image.open("assets/login/imagem_fundo.png"),
                light_image=Image.open("assets/login/imagem_fundo.png"),
                size=(900, 600))
            lbl_imagem_fundo = CTkLabel(
                self,
                image=criar_imagem_fundo,
                text="")
            lbl_imagem_fundo.place(x=0, y=0)

            ### Fundo login
            fundo_login = CTkFrame(
                self,
                height=900,
                width=400,
                fg_color=cinza_escuro,
                bg_color=cinza_escuro)
            fundo_login.place(x=500, y=0)

            ### Label inscreva-se
            lbl_inscrevase = CTkLabel(
                self,
                text="Inscreva-se",
                fg_color=cinza_escuro,
                bg_color=cinza_escuro,
                text_color=branco,
                font=("Roboto Bold", 48 * -1, "bold"),
            )
            lbl_inscrevase.place(x=635, y=73)

            ### Entradas
            ent_usuario = CTkEntry(
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
            ent_usuario.place(x=581, y=199)

            ent_senha = CTkEntry(
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
            ent_senha.place(x=581, y=256)

            ent_repsen = CTkEntry(
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
            ent_repsen.place(x=581, y=313)

            ### Botão registrar
            btn_registrar = CTkButton(
                self,
                # command=self.frame.registrar,
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
            btn_registrar.place(x=581, y=408)

            ### Label já tem conta?
            lbl_nconta = CTkLabel(
                self,
                text="Já tem conta?",
                fg_color=cinza_escuro,
                bg_color=cinza_escuro,
                text_color=branco,
                font=("Roboto Bold", 14 * -1, "bold"),
            )
            lbl_nconta.place(x=602, y=474)

            ### Botão voltar
            btn_voltar = CTkButton(
                self,
                # command=self.voltar,
                border_width=0,
                width=74,
                height=16,
                fg_color=cinza_escuro,
                bg_color=cinza_escuro,
                text_color=azul_claro,
                text="Voltar",
                font=("Roboto Bold", 14 * -1, "bold"),
                hover_color=cinza_escuro,
                cursor="hand2",
            )
            btn_voltar.place(x=698, y=477)
        # janela.mainloop()
    ### Funções
    # def registrar(janela):
    #     print("btn_registrar clicked")
    # def voltar(janela):
    #     janela.destroy()
    #
