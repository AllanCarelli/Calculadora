import customtkinter as ctk

class calculadora:
    def __init__(self):
        self.valor1 = '';self.conta = '';self.valor2 = '';self.resultados = f'{self.valor1}{self.conta}{self.valor2}'
        self.janela = ctk.CTk();self.janela.geometry('84x100');self.janela.resizable(False, False)
        self.txt = ctk.CTkLabel(self.janela, text=f'{self.resultados}', font=('Arial', 15))
        for k in range(0,4):
            self.botao_num_gerador(k,(k-1)*17, 40)
        for l in range(3,7):
            self.botao_num_gerador(l,(l-4)*17, 60)
        for m in range(6,10):
            self.botao_num_gerador(m,(m-7)*17, 80)
        self.botao_num_gerador(0,51,40)
        for x in (43,45,42,47):
            if x == 43:
                self.botao_num_gerador(chr(x),51,60)
            elif x == 45:
                self.botao_num_gerador(chr(x),51,80)
            elif x == 42:
                self.botao_num_gerador(chr(x),68,40)
            else:
                self.botao_num_gerador(chr(x),68,60)
       
        bi = ctk.CTkButton(self.janela, text='=', command=self.resultado, width=10, height=10).place(x=68,y=80)
        self.janela.mainloop()
    def adicionar_numero_na_conta(self, numero):
        if self.conta == '':
            self.valor1 += f'{numero}'
            self.update_label(True)
        else:
            self.valor2 += f'{numero}'
            self.update_label(True)
    def adicionar_operacao(self, operacao):
        self.conta = operacao
        self.update_label(True)
    def resultado(self):
        self.resultados = eval(self.resultados)
        self.update_label(False)
        self.valor1 = ''; self.conta = ''; self.valor2 = ''
    def update_label(self, mudar_resultados):
        if mudar_resultados == True:
            self.resultados = f'{self.valor1}{self.conta}{self.valor2}'
        self.txt.destroy()
        self.txt = ctk.CTkLabel(self.janela, text=f'{self.resultados}', font=('Arial', 15))
        self.txt.place(x=0, y=0)
    def botao_num_gerador(self, obj, xs, ys):
        try:
            if obj == int(obj):
                ctk.CTkButton(self.janela, text=f'{obj}', command=lambda: self.adicionar_numero_na_conta(obj), width=10, height=10).place(x=xs,y=ys)  #se eu criar uma função "local"  com lambda, eu crio ela sem parâmetros, o que faz ela só ser executada com o clique.
        except ValueError:
            if obj == '-':
                ctk.CTkButton(self.janela, text=obj, command=lambda: self.adicionar_operacao(obj), width=20, height=10).place(x=xs,y=ys) 
            else:
                ctk.CTkButton(self.janela, text=obj, command=lambda: self.adicionar_operacao(obj), width=10, height=10).place(x=xs,y=ys) 
        

calculadora()
