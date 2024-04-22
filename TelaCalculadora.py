 
import calculadoraLogica as bc
import tkinter as tk
from tkinter import *
from pandastable import Table
import pandas as pd


class VentanaCalculadora(tk.Tk): 
    
    def __init__(self):
        super(VentanaCalculadora, self).__init__()
        self.title("Calculadora Logica")
        self.iconbitmap("C:/Users/natanael.silva/Documents/projeto_forca/projeto_forca/Curso_python/Calculadora_Tabela_Logica/calc_calculator_10824.ico")
        self.geometry('300x450')
        self.config(bd=20)
        self.config(background="#05021b")
        self.resizable(False, False)
        self.entrada = tk.StringVar() 
        
        self.pantalla = tk.Entry(
                            self, 
                            font=("Courier",12), 
                            background="#84a9ac",##84a9ac
                            fg='#000000', 
                            borderwidth=10, 
                            width=24,
                            textvariable=self.entrada
                        )
        self.pantalla.grid(row=0, column=0, columnspan=4, pady=25)
        
        # Botões de símbolos lógicos
        BtA = Button(self, text='A', command=lambda: self.btSimbolos('A'))
        self.configurar_boton(BtA)
        BtA.grid(row=2, column=0, pady=5)

        BtB = Button(self, text='B', command=lambda: self.btSimbolos('B'))
        self.configurar_boton(BtB)
        BtB.grid(row=2, column=1)
        
        BtC = Button(self, text='C', command=lambda: self.btSimbolos('C'))
        self.configurar_boton(BtC)
        BtC.grid(row=2, column=2)

        BtD = Button(self, text='D', command=lambda: self.btSimbolos('D'))
        self.configurar_boton(BtD)
        BtD.grid(row=2, column=3)

        BtAnd = Button(self, text='∧', command=lambda: self.btSimbolos('∧'))
        self.configurar_boton(BtAnd)
        BtAnd.grid(row=3, column=0, pady=5)

        BtOr = Button(self, text='∨', command=lambda: self.btSimbolos('∨'))
        self.configurar_boton(BtOr)
        BtOr.grid(row=3, column=1)

        BtNot = Button(self, text='~', command=lambda: self.btSimbolos('~'))
        self.configurar_boton(BtNot)
        BtNot.grid(row=3,column=2)

        BtIfThen = Button(self, text='⇒', command=lambda: self.btSimbolos('⇒')) # →
        self.configurar_boton(BtIfThen)
        BtIfThen.grid(row= 3, column=3)

        BtIfOnlyIf = Button(self, text='⇔', command=lambda: self.btSimbolos('⇔'))
        self.configurar_boton(BtIfOnlyIf)
        BtIfOnlyIf.grid(row=4, column=0, pady=5)

        BtIfXOR = Button(self, text='+', command=lambda: self.btSimbolos('+'))
        self.configurar_boton(BtIfXOR)
        BtIfXOR.grid(row=4, column=1)
        
        BtIfXAND = Button(self, text='⊻', command=lambda: self.btSimbolos('⊻'))
        self.configurar_boton(BtIfXAND)
        BtIfXAND.grid(row=4, column=2)

        BtParenthesis = Button(self, text='(', command=lambda: self.btSimbolos('('))
        self.configurar_boton(BtParenthesis)
        BtParenthesis.grid(row=4, column=3)

        BtParenthesis2 = Button(self, text=')', command=lambda: self.btSimbolos(')'))
        self.configurar_boton(BtParenthesis2)
        BtParenthesis2.grid(row=5, column=0, pady=5)

        BtClear = Button(self, text='AC', command=self.limpaCampo)
        self.configurar_boton(BtClear) 
        BtClear.config(bg="#7F261C")
        BtClear.grid(row=5, column=1)

        BtEqual = Button(self, text='=',height=3, command=self.igual)
        self.configurar_boton(BtEqual)
        BtEqual.config(bg="#38B5D4")
        BtEqual.grid(row=5, column=2)
        
        # Vincula a função bloquearInsercao ao evento de clique do botão esquerdo do mouse
        self.pantalla.bind('<Button-1>', self.bloquearInsercao)
        
        # Legendas dos botões
        legendas_esquerda = [
            "Termos A, B, C, D",
            "Conjunção ∧",
            "Disjunção ∨",
            "Negação ~"
        ]
        
        legendas_direita = [
            "Implicação ⇒",
            "Bicondicional ⇔",
            "XOR +",
            "XAND ⊻"
        ]
        
        # Organiza as legendas por meio de loop
        for i, (leg_esq, leg_dir) in enumerate(zip(legendas_esquerda, legendas_direita)):
            label_esq = Label(self, text=leg_esq, bg="#05021b", fg="#cae8d5")
            label_dir = Label(self, text=leg_dir, bg="#05021b", fg="#cae8d5")
            label_esq.place(x=6, y=310 + i * 30)
            label_dir.place(x=130, y=310 + i * 30)
            label_esq.config(font=("Georgia", 9))
            label_dir.config(font=("Georgia", 9))
        
        self.mainloop()

    # Função para o layout dos botões
    def configurar_boton(self, boton):
        boton.config(
            font= ('Courier',13),
            bg='#204051', 
            width=3, 
            height=1, 
            fg='#cae8d5',
            padx=7,
            pady=4
    )
    
    # Função para inserir simbolo no campo de texto        
    def btSimbolos(self, simbolo):
        self.pantalla.insert(self.pantalla.index(tk.INSERT),simbolo)
        self.pantalla
        
   # Função para limpar o campo de texto
    def limpaCampo(self):
        self.pantalla.delete(0, END)

    # Função para calcular o resultado da expressão lógica
    def igual(self):
        expressao = self.entrada.get()
        result, mensagem = bc.ValidarExpressao(expressao)
        
        if result == False:
            self.pantalla.delete(0, END)
            self.pantalla.insert(self.pantalla.index(tk.INSERT), mensagem)
        else: 
            # Criar Janela para mostrar tabela verdade da expressão
            tipo = result
            tabela = mensagem
            root = tk.Tk()
            root.title(tipo)

            frame = tk.Frame(root)
            frame.pack(fill='both', expand=True)
            
            # Crie um DataFrame Pandas a partir da mensagem retornada
            df = pd.DataFrame(tabela)

            # Janela Tabela
            pt = Table(frame, dataframe=df, index=False)
            pt.show()

            root.mainloop()  
        
    # Função para impedir a inserção de texto via mouse
    def bloquearInsercao(self, event):
        return "break"

            
main = VentanaCalculadora() 