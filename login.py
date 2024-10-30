from customtkinter import *
from PIL import Image

### Funções

def login():
    print("btn_login clicked")
def inscrevase():
    print("btn_inscrevase clicked")


### Cores
cinza_escuro = "#1E1E1E"
branco = "#fff"
cinza_claro= "#2d2d2d"
cinza_placeholder = "#969696"
azul = "#006fff"
azul_claro = "#32ADE6"

### Janela
janela = CTk()
janela.geometry("900x600")
janela.resizable(False,False)
janela._set_appearance_mode("dark")

### Imagem de fundo
criar_imagem_fundo = CTkImage(
    dark_image=Image.open("assets/login/imagem_fundo.png"),
    light_image=Image.open("assets/login/imagem_fundo.png"),
    size=(900, 600))
lbl_imagem_fundo = CTkLabel(
    janela,
    image=criar_imagem_fundo,
    text="")
lbl_imagem_fundo.place(x=0,y=0)

### Fundo login
fundo_login = CTkFrame(
    janela,
    height=900,
    width=400,
    fg_color=cinza_escuro,
    bg_color=cinza_escuro)
fundo_login.place(x=500,y=0)

### Texto entrar
lbl_entrar = CTkLabel(
    janela,
    text="Entrar",
    fg_color=cinza_escuro,
    bg_color=cinza_escuro,
    text_color=branco,
    font=("Roboto Bold", 48 * -1, "bold"),
)
lbl_entrar.place(x=635,y=73)

### Entradas
ent_usuario = CTkEntry(
    janela,
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
ent_usuario.place(x=581,y=199)

ent_senha = CTkEntry(
    janela,
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
ent_senha.place(x=581,y=256)

ent_dois_fat = CTkEntry(
    janela,
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
ent_dois_fat.place(x=581,y=313)

### Botão login
btn_login = CTkButton(
    janela,
    command=login,
    corner_radius=15,
    border_width=0,
    width=238,
    height=43,
    fg_color=azul,
    bg_color=cinza_escuro,
    text_color=branco,
    text="Login",
    font = ("Roboto Bold", 20 * -1, "bold"),
    cursor="hand2",
)
btn_login.place(x=581,y=408)

### Label não tem conta
lbl_nconta = CTkLabel(
    janela,
    text="Não tem conta?",
    fg_color=cinza_escuro,
    bg_color=cinza_escuro,
    text_color=branco,
    font=("Roboto Bold", 14 * -1, "bold"),
)
lbl_nconta.place(x=602,y=474)

### Botão inscreva-se
btn_inscrevase = CTkButton(
    janela,
    command=inscrevase,
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
btn_inscrevase.place(x=698,y=477)
janela.mainloop()