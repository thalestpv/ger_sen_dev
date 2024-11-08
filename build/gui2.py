
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/home/thales/PycharmProjects/ger_sen_dev/build/assets/frame2")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("900x600")
window.configure(bg = "#1E1E1E")


canvas = Canvas(
    window,
    bg = "#1E1E1E",
    height = 600,
    width = 900,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    900.0,
    600.0,
    fill="#28282B",
    outline="")

canvas.create_rectangle(
    0.0,
    0.0,
    240.0,
    600.0,
    fill="#1E1E1E",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    603.0,
    555.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("atualizar.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=826.0,
    y=541.0,
    width=28.0,
    height=28.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("copiar.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=780.0,
    y=541.0,
    width=28.0,
    height=28.0
)

canvas.create_text(
    357.0,
    543.0,
    anchor="nw",
    text="fcwsufi3j45490723849208yr2-8y1hi",
    fill="#FFFFFF",
    font=("Roboto Medium", 20 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    586.0,
    202.0,
    image=image_image_2
)

canvas.create_text(
    419.0,
    179.0,
    anchor="nw",
    text="Tela com as senha",
    fill="#FFFFFF",
    font=("Roboto Bold", 40 * -1)
)

canvas.create_text(
    67.0,
    33.0,
    anchor="nw",
    text="Adicionar",
    fill="#FFFFFF",
    font=("Roboto Medium", 20 * -1)
)

image_image_3 = PhotoImage(
    file=relative_to_assets("mais.png"))
image_3 = canvas.create_image(
    43.0,
    44.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("remover.png"))
image_4 = canvas.create_image(
    43.0,
    101.0,
    image=image_image_4
)

canvas.create_text(
    67.0,
    90.0,
    anchor="nw",
    text="Remover",
    fill="#FFFFFF",
    font=("Roboto Medium", 20 * -1)
)

canvas.create_text(
    67.0,
    549.0,
    anchor="nw",
    text="Sair",
    fill="#FFFFFF",
    font=("Roboto Medium", 20 * -1)
)

image_image_5 = PhotoImage(
    file=relative_to_assets("sair.png"))
image_5 = canvas.create_image(
    40.0,
    559.0,
    image=image_image_5
)
window.resizable(False, False)
window.mainloop()