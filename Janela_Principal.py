# Importando as bibliotecas
from tkinter import *
from tkinter import messagebox
from testeprojeto.Segunda_Janela import Segunda_Janela
from testeprojeto.Janela_Patio import Janela_Patio

class Janela_Principal(Tk):

    def __init__(self, controle):

        self.controle = controle
        super().__init__()
        self.geometry('400x400')
        self.title('Concessionária')

        self.btn_close = Button(self, width=10, text='Sair', command=self.destroy)
        self.btn_uno = Button(self, width=20, text='Uno', command = self.criar_terceira_janela)
        #self.btn_ok = Button(self, width=10, text='Ok', command=self.btn_ok_click)
        #self.lbl_ok = Label(self, text='Teste')
        #self.txt_ok = Entry(self)

        self.btn_close.place(x=10, y=250)
        self.btn_uno.place(x=10, y= 50)
        #self.btn_ok.place(x=140, y=250)
        #self.lbl_ok.place(x=140, y=200)
        #self.txt_ok.place(x=140, y=150)

        self.menu = Menu(self)
        #Criando um item de menu e subtitens
        self.menu_principal = Menu(self.menu, tearoff=0)
        self.menu_principal.add_command(label='Compradores', command=self.criar_segunda_janela)
        self.menu_principal.add_command(label='Vendedores', command=self.menu_click)
        #Criar terceira janela
        self.menu_principal.add_command(label='Carros Vendidos', command=self.menu_click)
        #Criar quarta janela
        self.menu_principal.add_separator()
        self.menu_principal.add_command(label='Sair', command=self.destroy)
        self.menu.add_cascade(label='Menu', menu=self.menu_principal)
        # Mostrando o menu
        self.config(menu=self.menu)


    def destroy(self):
        if messagebox.askokcancel('Confirmação', 'Deseja sair?'):
            super().destroy()

    # Metodo para o btn_ok
    #def btn_ok_click(self):
        # Recuperar a lista de compra
     #   lista_compra = self.controle.get_lista_compra()
        # Percorrer a lista
      #  for item in lista_compra:
       #     messagebox.showinfo('Item', item.to_string())

    def menu_click(self):
       messagebox.showinfo('Menu', 'Clicou no item de menu!')


    def criar_segunda_janela(self):
        Segunda_Janela(self)

    def criar_terceira_janela(self):
        Janela_Patio(self)


