import tkinter as tk
from tkinter import messagebox

class JanelaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Janela Principal")
        self.main_frame = MainFrame(self)
        self.main_frame.pack()

    def mostrar_mensagem(self):
        messagebox.showinfo("Mensagem", "Função Mensagem Box Executada!")

class MainFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.subframe = SubFrame(self, master.mostrar_mensagem)
        self.subframe.pack()

class SubFrame(tk.Frame):
    def __init__(self, master, funcao):
        super().__init__(master)
        self.botao = tk.Button(self, text="Executar Função", command=funcao)
        self.botao.pack()

if __name__ == "__main__":
    janela = JanelaPrincipal()
    janela.mainloop()
