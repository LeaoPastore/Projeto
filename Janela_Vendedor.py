from tkinter import *
from tkinter import messagebox
from testeprojeto.Janela_Comprador import Janela_Comprador

# Classe Segunda_Janela
class Janela_Vendedor(Toplevel):
    # Metodo construtor
    def __init__(self, parent):
        # Chamar o init da classe mae
        super().__init__(parent)
        self.geometry('500x250')
        self.title('Cadastro Vendedor')
        self.transient(parent)
        self.grab_set()

        self.btn_close = Button(self, width=10, text='Sair', command=self.destroy)
        self.btn_ok = Button(self, width=10, text='Ok', command=self.cadastro_comprador)#add funcao para salvar
        self.lbl_vendedor = Label(self, width=20, text='Vendedor')
        self.lbl_mat = Label(self, width=20, text='Número de matrícula')
        self.lbl_data = Label(self, width=20, text='Data da venda')
        self.lbl_obs = Label(self, width=20, text= "Observação da venda")
        #self.lbl_obs = Label(self, width=20, text="Observações da venda")
        self.txt_vendedor = Entry(self, width=50)
        self.txt_mat = Entry(self,width=50)
        self.txt_data = Entry(self,width=50)
        self.txt_obs = Entry(self,width=50)
        #self.txt_obs = Entry(self, width=50)

        self.btn_close.place(x=100, y=200)
        self.btn_ok.place(x=300, y=200)
        self.lbl_vendedor.place(x=10, y=30)
        self.lbl_mat.place(x=10, y=70)
        self.lbl_data.place(x=10, y=110)
        self.lbl_obs.place(x=10, y=150)
        #self.lbl_obs.place(x=10, y=190)
        self.txt_vendedor.place(x=150, y=30)
        self.txt_mat.place(x=150, y=70)
        self.txt_data.place(x=150, y=110)
        self.txt_obs.place(x=150, y=150)
        #self.txt_obs.place(x=150, y=190)

        self.dados_vendedor = []


        # Metodo para fechar a janela
    def destroy(self):
        # Janela de confirmacao
        if messagebox.askokcancel('Confirmação', 'Deseja sair, o cadastro não foi finalizado?'):
            super().destroy()

    def cadastro_comprador(self):
        self.dados_vendedor.append([self.txt_vendedor.get(), self.txt_mat.get(), self.txt_data.get(), self.txt_obs.get()])
        f = open('Cadastro_Vendedor', '+a')
        f.write("%s:%s:%s:%s\n"%(self.dados_vendedor[0][0], self.dados_vendedor[0][1],self.dados_vendedor[0][2],self.dados_vendedor[0][3]))
        f.close()

        print('Dados do vendedor:')
        print('Nome:', self.txt_vendedor.get())
        print('Matrícula:', self.txt_mat.get())
        print('Data:',self.txt_data.get())
        print('Observações:',self.txt_obs.get())
        Janela_Comprador(self)
        #print(self.dados_vendedor[0])


    def confirmacao_cadastro(self):
        f = open('Cadastro_Vendedor', 'r')
        f.read()
        f.close()
"""
a=f.read()
a = a.split('\n')

for i in range(0,len(a)):
    i = i.split(:)
"""
