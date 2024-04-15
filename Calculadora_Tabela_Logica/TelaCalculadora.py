 
import Blackbox as bc
import tkinter as tk
from tkinter import *
from pandastable import Table
import pandas as pd


# # Estrutura da Janela
# calculadora = Tk()
# calculadora.title('Calculadora Lógica')
# calculadora.resizable(False, False)  # Impede redimensionamento horizontal e vertical
# window_width = 475
# window_height = 500
# screen_width = calculadora.winfo_screenwidth()
# screen_height = calculadora.winfo_screenheight()
# x_coordinate = (screen_width/2) - (window_width/2)
# y_coordinate = (screen_height/2) - (window_height/2)
# calculadora.geometry('%dx%d+%d+%d' % (window_width, window_height, x_coordinate, y_coordinate))
# calculadora.config(bg='#121d4f') 


# # Função que insere os símbolos lógicos no campo de texto
# def btSimbolos(simbolo):
#     campoNumeros.insert(END, simbolo)

# # Função para limpar o campo de texto
# def limpaCampo():
#     campoNumeros.delete('1.0', END)

# # Função para calcular o resultado da expressão lógica
# def igual():
#     expressao = campoNumeros.get('1.0', END)
#     result, mensagem = bc.ValidarExpressao(expressao)
    
#     if result == False:
#         campoNumeros.insert(END, mensagem)
#     else:
#         # campoNumeros.insert(END, mensagem) 
#         root = tk.Tk()
#         root.title('PandasTable Example')

#         frame = tk.Frame(root)
#         frame.pack(fill='both', expand=True)
        
#         # Crie um DataFrame Pandas a partir da mensagem
#         df = pd.DataFrame(mensagem)

#         pt = Table(frame, dataframe=df, index=False)
#         pt.show()

#         root.mainloop()  
        
#     # try:
#     #     resultado = eval(expressao)
#     #     limpaCampo()
#     #     campoNumeros.insert(END, resultado)
#     # except Exception as e:
#     #     limpaCampo()
#     #     campoNumeros.insert(END, 'Erro')
        
#     # Teste de funcionamento de uma tabela verdade sendo gerada
#     #bc.tabela()
        
# # Função para impedir a inserção de texto via mouse
# def bloquearInsercao(event):
#     return "break"

# # Entry
# campoNumeros = Text(calculadora, width=30, height=3, font=('Arial', 14))
# campoNumeros.place(x=70, y=25)
# campoNumeros.config(highlightbackground="black", highlightthickness=3)

# # Vincula a função bloquearInsercao ao evento de clique do botão esquerdo do mouse
# campoNumeros.bind('<Button-1>', bloquearInsercao)

# # Botões de símbolos lógicos
# BtA = Button(calculadora, text='A', relief=FLAT, width=10, height=3, command=lambda: btSimbolos('A'))
# BtA.place(x=50, y=120)
# # configurar_boton(BtA)

# BtB = Button(calculadora, text='B', relief=FLAT, width=10, height=3, command=lambda: btSimbolos('B'))
# BtB.place(x=140, y=120)

# BtC = Button(calculadora, text='C', relief=FLAT, width=10, height=3, command=lambda: btSimbolos('C'))
# BtC.place(x=230, y=120)

# BtD = Button(calculadora, text='D', relief=FLAT, width=10, height=3, command=lambda: btSimbolos('D'))
# BtD.place(x=320, y=120)

# BtAnd = Button(calculadora, text='∧', relief=FLAT, width=10, height=3, command=lambda: btSimbolos('∧'))
# BtAnd.place(x=50, y=190)

# BtOr = Button(calculadora, text='∨', relief=FLAT, width=10, height=3, command=lambda: btSimbolos('∨'))
# BtOr.place(x=140, y=190)

# BtNot = Button(calculadora, text='¬', relief=FLAT, width=10, height=3, command=lambda: btSimbolos('¬'))
# BtNot.place(x=230, y=190)

# BtIfThen = Button(calculadora, text='⇒', relief=FLAT, width=10, height=3, command=lambda: btSimbolos('⇒')) # →
# BtIfThen.place(x=320, y=190)

# BtIfOnlyIf = Button(calculadora, text='⇔', relief=FLAT, width=10, height=3, command=lambda: btSimbolos('⇔'))
# BtIfOnlyIf.place(x=50, y=265)

# BtIfXOR = Button(calculadora, text='⊕', relief=FLAT, width=10, height=3, command=lambda: btSimbolos('⊕'))
# BtIfXOR.place(x=140, y=265)

# BtIfXAND = Button(calculadora, text='⊻', relief=FLAT, width=10, height=3, command=lambda: btSimbolos('⊻'))
# BtIfXAND.place(x=230, y=265)

# BtParenthesis = Button(calculadora, text='(', relief=FLAT, width=10, height=3, command=lambda: btSimbolos('('))
# BtParenthesis.place(x=320, y=265)

# BtParenthesis2 = Button(calculadora, text=')', relief=FLAT, width=10, height=3, command=lambda: btSimbolos(')'))
# BtParenthesis2.place(x=50, y=340)

# BtEqual = Button(calculadora, text='=', relief=FLAT, width=20, height=3, command=igual)
# BtEqual.place(x=230, y=340)

# BtClear = Button(calculadora, text='CE', relief=FLAT, width=10, height=3, command=limpaCampo)
# BtClear.place(x=140, y=340)

# feitoPor = Label(calculadora, text='Desenvolvido por Natan')
# feitoPor.pack(side='bottom')

# calculadora.mainloop()

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
        
        # btnP = tk.Button(self, text='p', command = lambda: self.escribir('p'))
        # self.configurar_boton(btnP)
        # btnP.grid(row=2, column=0, pady=5)
        
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

        BtNot = Button(self, text='¬', command=lambda: self.btSimbolos('¬'))
        self.configurar_boton(BtNot)
        BtNot.grid(row=3,column=2)

        BtIfThen = Button(self, text='⇒', command=lambda: self.btSimbolos('⇒')) # →
        self.configurar_boton(BtIfThen)
        BtIfThen.grid(row= 3, column=3)

        BtIfOnlyIf = Button(self, text='⇔', command=lambda: self.btSimbolos('⇔'))
        self.configurar_boton(BtIfOnlyIf)
        BtIfOnlyIf.grid(row=4, column=0, pady=5)

        BtIfXOR = Button(self, text='⊕', command=lambda: self.btSimbolos('⊕'))
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

        BtEqual = Button(self, text='=',height=3, command=self.igual)
        self.configurar_boton(BtEqual)
        BtEqual.grid(row=5, column=1)

        BtClear = Button(self, text='AC', command=self.limpaCampo)
        self.configurar_boton(BtClear)
        BtClear.grid(row=5, column=2)
        
        feitoPor = Label(self, text='Desenvolvido por Natan')
        feitoPor.grid(row=7, column= 3)
        # feitoPor.pack(side='bottom')
        
        # Vincula a função bloquearInsercao ao evento de clique do botão esquerdo do mouse
        self.pantalla.bind('<Button-1>', self.bloquearInsercao)
        
        self.mainloop()

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
            
    def btSimbolos(self, simbolo):
        self.pantalla.insert(self.pantalla.index(tk.INSERT),simbolo)
        # os.system('cls')
        self.pantalla
        
   # Função para limpar o campo de texto
    def limpaCampo(self):
        self.pantalla.delete(0, END)

    # Função para calcular o resultado da expressão lógica
    def igual(self):
        expressao = self.entrada.get()
        result, mensagem = bc.ValidarExpressao(expressao)
        
        if result == False:
            self.pantalla.insert(self.pantalla.index(tk.INSERT), mensagem)
        else:
            # campoNumeros.insert(END, mensagem) 
            root = tk.Tk()
            root.title('PandasTable Example')

            frame = tk.Frame(root)
            frame.pack(fill='both', expand=True)
            
            # Crie um DataFrame Pandas a partir da mensagem
            df = pd.DataFrame(mensagem)

            pt = Table(frame, dataframe=df, index=False)
            pt.show()

            root.mainloop()  
            
        # try:
        #     resultado = eval(expressao)
        #     limpaCampo()
        #     campoNumeros.insert(END, resultado)
        # except Exception as e:
        #     limpaCampo()
        #     campoNumeros.insert(END, 'Erro')
            
        # Teste de funcionamento de uma tabela verdade sendo gerada
        #bc.tabela()
        
    # Função para impedir a inserção de texto via mouse
    def bloquearInsercao(self, event):
        return "break"

            
main = VentanaCalculadora() 