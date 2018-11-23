from tkinter import *
from tkinter import messagebox
from testeprojeto.Janela_Vendedor import Janela_Vendedor

class Janela_Patio(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.geometry('300x300')
        self.title('No pátio')
        self.transient(parent)
        self.grab_set()

        self.btn_close = Button(self, width=10, text='Sair', command=self.destroy)
        self.btn_placa = Button(self, width=15, text='LOL-2018', command=self.fazer_cadastro)

        self.btn_close.place(x=10, y=250)
        self.btn_placa.place(x=10, y=50)

    def destroy(self):
        if messagebox.askokcancel('Confirmação', 'Deseja sair?'):
            super().destroy()

    def fazer_cadastro(self):
        Janela_Vendedor(self)