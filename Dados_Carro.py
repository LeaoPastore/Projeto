from tkinter import *
from tkinter import messagebox
#from testeprojeto.Janela_Vendedor import Janela_Vendedor
# Classe Segunda_Janela
class Dados_Carro(Toplevel):
    # Metodo construtor
    def __init__(self, parent):

        super().__init__(parent)
        self.geometry('500x250')
        self.title('Cadastro Carro Vendido')
        self.transient(parent)
        self.grab_set()

        self.btn_close = Button(self, width=10, text='Sair', command=self.destroy)
        self.btn_ok = Button(self, width=10, text='Ok', command=self.dados_carro)

        self.lbl_modelo = Label(self, width=20, text='Modelo')
        self.lbl_cor = Label(self, width=20, text='Cor')
        self.lbl_valor = Label(self, width=20, text='Valor da venda')
        self.lbl_chassi = Label(self, width=20, text= "Chassi")


        self.txt_modelo = Entry(self, width=50)
        self.txt_cor = Entry(self,width=50)
        self.txt_valor = Entry(self,width=50)
        self.txt_chassi = Entry(self,width=50)


        self.btn_close.place(x=100, y=200)
        self.btn_ok.place(x=300, y=200)

        self.lbl_modelo.place(x=10, y=30)
        self.lbl_cor.place(x=10, y=70)
        self.lbl_valor.place(x=10, y=110)
        self.lbl_chassi.place(x=10, y=150)

        self.txt_modelo.place(x=150, y=30)
        self.txt_cor.place(x=150, y=70)
        self.txt_valor.place(x=150, y=110)
        self.txt_chassi.place(x=150, y=150)

        self.info_carro = []

    def dados_carro(self):
        self.info_carro.append([self.txt_modelo.get(), self.txt_cor.get(), self.txt_valor.get(), self.txt_chassi.get()])
        f = open('Cadastro_Carro', '+a')
        f.write("%s:%s:%s:%s\n" % (self.info_carro[0][0], self.info_carro[0][1], self.info_carro[0][2],self.info_carro[0][3]))
        f.close()

        print('Dados do carro:')
        print('Modelo:', self.txt_modelo.get())
        print('Cor:', self.txt_cor.get())
        print('Valor: R$', self.txt_valor.get())
        print('Nº do Chassi:', self.txt_chassi.get())
        #print(self.dados_vendedor)
        if messagebox.askokcancel('Finalização de cadastro', 'Cadastro Realizado com sucesso'):
            super().destroy()

    def destroy(self):
        if messagebox.askokcancel('Confirmação', 'Deseja sair, o cadastro não foi finalizado?'):
            super().destroy()