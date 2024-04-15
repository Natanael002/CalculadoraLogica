# Importação de Bibliotecas
import pandas as pd
import os
from tabulate import tabulate
import re
import itertools


def ValidarExpressao(expressao):
    # Verificar se a expressão está vazia
    if not expressao.strip():
        return False, '\nExpressão vazia'
    else:
        # Verificar se os parênteses estão balanceados
        count_parenteses = 0
        for char in expressao:
            if char == '(':
                count_parenteses += 1
            elif char == ')':
                count_parenteses -= 1
                
        if count_parenteses != 0:
            return False, '\nParenteses desbalanceado'
        else:    
            # Verificar se há operadores sem operandos
            padrao_operadores_sem_operandos = re.compile(r'[∧∨⇒⇔](?!\w|[(])|(?<![\w)])[∧∨⇒⇔]')
            if padrao_operadores_sem_operandos.search(expressao):
                return False, "\nA expressão contém operadores sem operandos"
            else: 
                if "A" in expressao and "B" in expressao and "C" in expressao and "D" in expressao:
                    termos = ["A", "B", "C", "D"]
                    return truth_table(expressao, termos)
                elif "A" in expressao and "B" in expressao and "C" in expressao:
                    termos = ["A", "B", "C"]
                    return truth_table(expressao, termos)
                elif "A" in expressao and "B" in expressao:
                    termos = ["A", "B"]
                    return truth_table(expressao, termos)
                elif "A" in expressao:
                    termos = ["A"]
                    return truth_table(expressao, termos)

def condicional(a, b):
    return (not a) or b

# Definir uma função que representa a expressão equivalente ao operador condicional (⇒)
def conditional_operator(A, B):
    return not A or B

def evaluate_expression(expression, values):
    # Substitua os valores verdadeiros e falsos nas variáveis ​​da expressão
    # Inverter os simbolos para nomes boolean
    
    
    expression = expression.replace('A', 'A ')
    expression = expression.replace('B', 'B ')
    expression = expression.replace('C', 'C ')
    expression = expression.replace('D', 'D ')
    
    for var, value in values.items():
        expression = expression.replace(var, str(value))
        
            
    expression = expression.replace('∨', 'or ')
    expression = expression.replace('∧', 'and ')
    expression = expression.replace('¬', 'not ')
    expression = expression.replace('⇔', '== ')
    # Substituir o operador condicional (⇒) pela chamada à função conditional_operator
    expression = re.sub(r'(\w+)\s*⇒\s*(\w+)', r'conditional_operator(\1, \2)', expression)
    expression = expression.replace('⊕', '^ ')
    expression = expression.replace('⊻', '== ')
    
    # Avalie a expressão e retorne o resultado
    resultado =  eval(expression, {'conditional_operator': conditional_operator}) # {'conditional_operator': conditional_operator}
    
    # Converter o resultado para 0 ou 1, not no eval sempre retorna TRUE ou FALSE
    if resultado:
        return 1
    else:
        return 0

def truth_table(expression, variables):
    # Crie uma lista de todas as combinações possíveis de valores verdadeiros e falsos para as variáveis
    truth_values = list(itertools.product([0, 1], repeat=len(variables)))
    
    # Crie um DataFrame para armazenar a tabela verdade
    truth_table_df = pd.DataFrame(columns=variables + [expression]) #Trocar o result pela expressão pura que vem da calculadora
    
    # Avalie a expressão para cada combinação de valores verdadeiros e falsos
    for values in truth_values:
        values_dict = {variables[i]: values[i] for i in range(len(variables))}
        result = evaluate_expression(expression, values_dict)
        truth_table_df.loc[len(truth_table_df)] = list(values) + [result] # está criando as linhas onde os values seria os [0, 1, 0] da combinação truthv.. e  a ultima result q vem do resultado eval, tabela vem só com as colunas nomeadas 
    
    return True, truth_table_df

# Exemplo de uso
# expression = "A or D and (C and B)"
# variables = ["A", "B", "C", "D"]
# expression = "A ⇒ B"
# variables = ["A", "B"]

# table = truth_table(expression, variables)
# print(eval("not 1 or 1"))

# def testi():
#     print("AAAAAAAAAAA")

# expressao = "testi()"
print(eval('not (1 or 0) or (1 and 1)'))


















################################################################################################################################

# # Função principal, onde ocorre toda a interação com o usúario e funcionamento da Calculadora.
# def Menu():
#     while True:

#         try:
#             print("Calculadora Lógica!\nEscolha a opção desejada:\n\n1- Calculadora Disjunção V\n2- Calculadora Conjunção ∧\n3- Calculadora Condicional →\n4- Calculadora Bicondicional ↔\n5- Calculadora Negação ¬\n6- Gerador de Tabela Verdade\n7- Encerrar calculadora\n")
#             opcao = int(input("Digite a Opção Desejada: "))

#             if 1 <= opcao <= 6:
#                 os.system("cls")
#                 conectivo(opcao)
#                 input("\nPrecione enter para continuar e retornar ao menu principal ")
#                 os.system("cls")
#             elif opcao == 7:
#                 print("Fim da execução\nTenha um bom dia!")
#                 break
#             elif opcao == 8:
#                 expressao()
#             else:
#                 input("Escolha uma opção válida!\nPrecione enter para continuar ")
#                 os.system("cls")
#         except ValueError: # Se for inserido algo diferente de um número
#             input("Informe apenas valores numéricos...\nPrecione enter para continuar ")
#             os.system("cls")

# # Função para Verificação da seleção do meu e chamar as funções da calculadora
# def conectivo(opcao):
#     match opcao:
        
#         case 1:
#             CalculadoraDisjuncao()
#         case 2:
#             CalculadoraConjuncao()
#         case 3:
#             CalculadoraCondicional()
#         case 4:
#             CalculadoraBicondicional()
#         case 5:
#             CalculadoraNegacao()
#         case 6:
#             while True:

#                 try:
#                     print("Escolha uma tabela verdade das seguintes lógicas\n1- Disjunção V\n2- Conjunção ∧\n3- Condicional →\n4- Bicondicional ↔\n5- Negação ¬\n")
#                     opcaoTabela = int(input("Digite a Tabela Desejada: "))

#                     if 1 <= opcaoTabela <= 5:
#                         os.system("cls")
#                         if opcaoTabela == 1:
#                             print("Tabela Verdade Disjunção\n")
#                             CriaTabela("V", 2)
#                             break
#                         elif opcaoTabela == 2:
#                             print("Tabela Verdade Conjunção\n")
#                             CriaTabela("∧", 2)
#                             break
#                         elif opcaoTabela == 3:
#                             print("Tabela Verdade Condicional\n")
#                             CriaTabela("⭢", 2)
#                             break
#                         elif opcaoTabela == 4:
#                             print("Tabela Verdade Bicondicional\n")
#                             CriaTabela("↔", 2)
#                             break
#                         elif opcaoTabela == 5:
#                             print("Tabela Verdade Negação\n")
#                             CriaTabela("¬", 1)
#                             break
                        
#                     else:
#                         input("Escolha uma opção válida!\nPrecione enter para continuar ")
#                         os.system("cls")
#                 except ValueError: # Se for inserido algo diferente de um número
#                     input("Informe apenas valores numéricos...\nPrecione enter para continuar ")
#                     os.system("cls")
                    
# # Funcão para digitar expressão
# def expressao():
#     while True:
#         try:
#             print("use 'and' para ∧, 'or' para V, 'not' para ¬, '->' para → e '<->' para ↔")
#             expressao = input() #not P and Q or R
#         except ValueError: # Se for inserido algo diferente de um número
#             input("Informe apenas valores numéricos...\nPrecione enter para continuar ")
#             os.system("cls")
                    
# # Função para Calcular Operação de Disjunção
# def CalculadoraDisjuncao():
#     Colunas = pd.DataFrame({'A': [], 'B': []}) 
#     valorA = []
#     valorB = []
#     i = 0
#     while i < 4 : 
#         try:
#             A = int(input(f"Insira um valor entre 0 e 1 para o {i+1}° A: "))
#             B = int(input(f"Insira um valor entre 0 e 1 para o {i+1}° B: "))
#             i = i + 1
#             if (0 <= A <= 1) and (0 <= B <= 1) :
#                 valorA.insert(i, A)
#                 valorB.insert(i, B)
#             else:
#                 print("Digitos inválidos\n")
#                 i = i - 1
#         except ValueError:
#             print("Por favor, digite apenas entre 1 e 0\n")
    
#     Colunas['A'] = valorA
#     Colunas['B'] = valorB
    
#     print("\nTabela Verdade Disjunção\n")
#     CriaTabelaDin(Colunas, "V", 2)

# # Função para Calcular Operação de Conjunção
# def CalculadoraConjuncao(): 
#     Colunas = pd.DataFrame({'A': [], 'B': []}) 
#     valorA = []
#     valorB = []
#     i = 0
#     while i < 4 : 
#         try:
#             A = int(input(f"Insira um valor entre 0 e 1 para o {i+1}° A: "))
#             B = int(input(f"Insira um valor entre 0 e 1 para o {i+1}° B: "))
#             i = i + 1
#             if (0 <= A <= 1) and (0 <= B <= 1) :
#                 valorA.insert(i, A)
#                 valorB.insert(i, B)
#             else:
#                 print("Digitos inválidos\n")
#                 i = i - 1
#         except ValueError:
#             print("Por favor, digite apenas entre 1 e 0")
            
#     Colunas['A'] = valorA
#     Colunas['B'] = valorB
    
#     print("\nTabela Verdade Conjunção\n")
#     CriaTabelaDin(Colunas, "∧", 2)

# # Função para Calcular Operação Condicional    
# def CalculadoraCondicional():
#     Colunas = pd.DataFrame({'A': [], 'B': []}) 
#     valorA = []
#     valorB = []
#     i = 0
#     while i < 4 : 
#         try:
#             A = int(input(f"Insira um valor entre 0 e 1 para o {i+1}° A: "))
#             B = int(input(f"Insira um valor entre 0 e 1 para o {i+1}° B: "))
#             i = i + 1
#             if (0 <= A <= 1) and (0 <= B <= 1) :
#                 valorA.insert(i, A)
#                 valorB.insert(i, B)
#             else:
#                 print("Digitos inválidos\n")
#                 i = i - 1
#         except ValueError:
#             print("Por favor, digite apenas entre 1 e 0")
            
#     Colunas['A'] = valorA
#     Colunas['B'] = valorB
    
#     print("\nTabela Verdade Condicional\n")
#     CriaTabelaDin(Colunas, "⭢", 2)

# # Função para Calcular Operação Bicondicional    
# def CalculadoraBicondicional():
#     Colunas = pd.DataFrame({'A': [], 'B': []}) 
#     valorA = []
#     valorB = []
#     i = 0
#     while i < 4 : 
#         try:
#             A = int(input(f"Insira um valor entre 0 e 1 para o {i+1}° A: "))
#             B = int(input(f"Insira um valor entre 0 e 1 para o {i+1}° B: "))
#             i = i + 1
#             if (0 <= A <= 1) and (0 <= B <= 1) :
#                 valorA.insert(i, A)
#                 valorB.insert(i, B)
#             else:
#                 print("Digitos inválidos\n")
#                 i = i - 1
#         except ValueError:
#             print("Por favor, digite apenas entre 1 e 0")
            
#     Colunas['A'] = valorA
#     Colunas['B'] = valorB
    
#     print("\nTabela Verdade Bicondicional\n")
#     CriaTabelaDin(Colunas, "↔", 2)

# # Função para Calcular Operação de Negação
# def CalculadoraNegacao():
#     Colunas = pd.DataFrame({'A': []}) 
#     valorA = []
#     i = 0
#     while i < 2 : 
#         try:
#             A = int(input(f"Insira um valor entre 0 e 1 para o {i+1}° A: "))
#             i = i + 1
#             if (0 <= A <= 1):
#                 valorA.insert(i, A)
#             else:
#                 print("Digitos inválidos\n")
#                 i = i - 1
#         except ValueError:
#             print("Por favor, digite apenas entre 1 e 0")
            
#     Colunas['A'] = valorA
    
#     print("\nTabela Verdade Negação\n")
#     CriaTabelaDin(Colunas, "¬", 1)
    
# # Função para criação da tabela
# def CriaTabela(nome_tabela, col = 0): 
#     nome_table = nome_tabela
    
#     if col == 2: 
#         df = pd.DataFrame({'A': [], 'B': []}) # Cria uma tabela com coluna A B
#         InserirValores(df, nome_table, col = 2) 
#         Tabela = InserirValores(df, nome_table, col = 2) # Passa a tabela e um parametro com o valor lógico desejado e recebe uma tabela pronta
#         print(tabulate(Tabela, headers='keys', tablefmt= 'rounded_grid', showindex= False)) # rounded_grid double_grid
#     elif col == 1:
#         df = pd.DataFrame({'A': []}) # Cria uma tabela com coluna A
#         InserirValores(df, nome_table, col = 1) # Passa a tabela e um parametro com o valor lógico desejado
#         Tabela = InserirValores(df, nome_table, col = 1) # Passa a tabela e um parametro com o valor lógico desejado e recebe uma tabela pronta
#         print(tabulate(Tabela, headers='keys', tablefmt='rounded_grid', showindex= False))

# # Função para criação da tabela dinâmica       
# def CriaTabelaDin(nome_tabela, operacao ,col = 0): 
#     if col == 2: 
#         Tabela = InserirValoresDin(nome_tabela, operacao, col = 2) # Passa a tabela e um parametro com o valor lógico desejado e recebe uma tabela pronta
#         print(tabulate(Tabela, headers='keys', tablefmt= 'rounded_grid', showindex= False)) # rounded_grid double_grid
#     elif col == 1:
#         Tabela = InserirValoresDin(nome_tabela, operacao, col = 1) # Passa a tabela e um parametro com o valor lógico desejado e recebe uma tabela pronta
#         print(tabulate(Tabela, headers='keys', tablefmt='rounded_grid', showindex= False))
        
# # Função para inserir valores em uma tabela    
# def InserirValores(tabela, operacao, col = 0):
#     if col == 2:
        
#         resultado = pd.concat([Col2, tabela], axis= 0) # Cria uma tabela juntando a tabela passada por parametro e a tabela com valores pré definidos de padrões de operações lógicas com 1 e 0
#         cont = len(resultado)
        
#         if operacao == 'V':
#             valor = []
#             for i in range(cont) : # Realiza verificação dos indices da tabela e realiza a operação guardando o resultado 
#                 indA = resultado.at[i, 'A']
#                 indB = resultado.at[i, 'B']
#                 if (indA == 0 and indB == 0):
#                     valor.insert(i, 0)
#                 else:
#                     valor.insert(i, 1)
        
#             # Cria um Dic com chaves e valores recebidos do loop
#             ResultOperacao = {'A V B' : []}
#             ResultOperacao['A V B'] = valor
            
#             # Adiciona a coluna de resultado na tabela formada nesta função e retorna a tabela completa com operações e resultados        
#             ColResul = pd.DataFrame(ResultOperacao)
#             TabelaFinal = pd.concat([resultado, ColResul], axis= 1) 
#             TabelaFormatada = TabelaFinal.astype(int)
#             return TabelaFormatada 
            
#         elif operacao == '∧':
#             valor = []
#             for i in range(cont):
#                 indA = resultado.at[i, 'A']
#                 indB = resultado.at[i, 'B']
#                 if (indA == 1 and indB == 1):
#                     valor.insert(i, 1)
#                 else:
#                     valor.insert(i, 0)
            
#             # Cria um Dic com chaves e valores recebidos do loop
#             ResultOperacao = {'A ∧ B' : []}
#             ResultOperacao['A ∧ B'] = valor
                    
#             # Adiciona a coluna de resultado na tabela formada nesta função e retorna a tabela completa com operações e resultados        
#             ColResul = pd.DataFrame(ResultOperacao)
#             TabelaFinal = pd.concat([resultado, ColResul], axis= 1) 
#             TabelaFormatada = TabelaFinal.astype(int) 
#             return TabelaFormatada 
        
#         elif operacao == '⭢':
#             valor = []
#             for i in range(cont):
#                 indA = resultado.at[i, 'A']
#                 indB = resultado.at[i, 'B']
#                 if (indA == 1 and indB == 0):
#                     valor.insert(i, 0)
#                 else:
#                     valor.insert(i, 1)
            
#             # Cria um Dic com chaves e valores recebidos do loop
#             ResultOperacao = {'A ⭢ B' : []}
#             ResultOperacao['A ⭢ B'] = valor
                    
#             # Adiciona a coluna de resultado na tabela formada nesta função e retorna a tabela completa com operações e resultados        
#             ColResul = pd.DataFrame(ResultOperacao)
#             TabelaFinal = pd.concat([resultado, ColResul], axis= 1) 
#             TabelaFormatada = TabelaFinal.astype(int) 
#             return TabelaFormatada
        
#         elif operacao == '↔':
#             valor = []
#             for i in range(cont):
#                 indA = resultado.at[i, 'A']
#                 indB = resultado.at[i, 'B']
#                 if (indA == indB):
#                     valor.insert(i, 1)
#                 else:
#                     valor.insert(i, 0)
            
#             # Cria um Dic com chaves e valores recebidos do loop
#             ResultOperacao = {'A ↔ B' : []}
#             ResultOperacao['A ↔ B'] = valor
                    
#             # Adiciona a coluna de resultado na tabela formada nesta função e retorna a tabela completa com operações e resultados        
#             ColResul = pd.DataFrame(ResultOperacao)
#             TabelaFinal = pd.concat([resultado, ColResul], axis= 1) 
#             TabelaFormatada = TabelaFinal.astype(int) 
#             return TabelaFormatada
        
#     elif col == 1:
        
#         resultado = pd.concat([Col1, tabela], axis= 0) # Cria uma tabela juntando a tabela passada por parametro e a tabela com valores pré definidos de padrões de operações lógicas com 1 e 0
#         cont = len(resultado)  
#         if operacao == '¬':
#             valor = []
#             for i in range(cont):
#                 indA = resultado.at[i, 'A']
#                 if indA == 1:
#                     valor.insert(i, 0)
#                 else:
#                     valor.insert(i, 1)
                    
#             # Cria um Dic com chaves e valores recebidos do loop
#             ResultOperacao = {'¬ A' : []}
#             ResultOperacao['¬ A'] = valor
                    
#             # Adiciona a coluna de resultado na tabela formada nesta função e retorna a tabela completa com operações e resultados        
#             ColResul = pd.DataFrame(ResultOperacao)
#             TabelaFinal = pd.concat([resultado, ColResul], axis= 1) 
#             TabelaFormatada = TabelaFinal.astype(int) 
#             return TabelaFormatada 
    
#     else:
#         return print("Nenhuma tabela foi fornecida!")             

# # Função para inserir valores em uma tabela dinâmica    
# def InserirValoresDin(tabela, operacao, col = 0):
#     if col == 2:
        
#         if operacao == 'V':
#             cont = len(tabela)
#             valor = []
#             for i in range(cont) : # Realiza verificação dos indices da tabela e realiza a operação guardando o resultado 
#                 indA = tabela.at[i, 'A']
#                 indB = tabela.at[i, 'B']
#                 if (indA == 0 and indB == 0):
#                     valor.insert(i, 0)
#                 else:
#                     valor.insert(i, 1)
                    
#         # Cria um Dic com chaves e valores recebidos do loop
#             ResultOperacao = {'A V B' : []}
#             ResultOperacao['A V B'] = valor
            
#             # Adiciona a coluna de resultado na tabela formada nesta função e retorna a tabela completa com operações e resultados        
#             ColResul = pd.DataFrame(ResultOperacao)
#             TabelaFinal = pd.concat([tabela, ColResul], axis= 1) 
#             return TabelaFinal 
        
#         if operacao == '∧':
#                 cont = len(tabela)
#                 valor = []
#                 for i in range(cont) :  
#                     indA = tabela.at[i, 'A']
#                     indB = tabela.at[i, 'B']
#                     if (indA == 1 and indB == 1):
#                         valor.insert(i, 1)
#                     else:
#                         valor.insert(i, 0)
                        
#             # Cria um Dic com chaves e valores recebidos do loop
#                 ResultOperacao = {'A ∧ B' : []}
#                 ResultOperacao['A ∧ B'] = valor
                
#                 # Adiciona a coluna de resultado na tabela formada nesta função e retorna a tabela completa com operações e resultados        
#                 ColResul = pd.DataFrame(ResultOperacao)
#                 TabelaFinal = pd.concat([tabela, ColResul], axis= 1) 
#                 return TabelaFinal 
            
#         elif operacao == '⭢':
#             cont = len(tabela)
#             valor = []
#             for i in range(cont):
#                 indA = tabela.at[i, 'A']
#                 indB = tabela.at[i, 'B']
#                 if (indA == 1 and indB == 0):
#                     valor.insert(i, 0)
#                 else:
#                     valor.insert(i, 1)
            
#             # Cria um Dic com chaves e valores recebidos do loop
#             ResultOperacao = {'A ⭢ B' : []}
#             ResultOperacao['A ⭢ B'] = valor
                    
#             # Adiciona a coluna de resultado na tabela formada nesta função e retorna a tabela completa com operações e resultados        
#             ColResul = pd.DataFrame(ResultOperacao)
#             TabelaFinal = pd.concat([tabela, ColResul], axis= 1) 
#             return TabelaFinal
        
#         elif operacao == '↔':
#             cont = len(tabela)
#             valor = []
#             for i in range(cont):
#                 indA = tabela.at[i, 'A']
#                 indB = tabela.at[i, 'B']
#                 if (indA == indB):
#                     valor.insert(i, 1)
#                 else:
#                     valor.insert(i, 0)
            
#             # Cria um Dic com chaves e valores recebidos do loop
#             ResultOperacao = {'A ↔ B' : []}
#             ResultOperacao['A ↔ B'] = valor
                    
#             # Adiciona a coluna de resultado na tabela formada nesta função e retorna a tabela completa com operações e resultados        
#             ColResul = pd.DataFrame(ResultOperacao)
#             TabelaFinal = pd.concat([tabela, ColResul], axis= 1) 
#             return TabelaFinal    
    
#     elif col == 1:
#         if operacao == '¬':
#             cont = len(tabela)
#             valor = []
#             for i in range(cont):
#                 indA = tabela.at[i, 'A']
#                 if indA == 1:
#                     valor.insert(i, 0)
#                 else:
#                     valor.insert(i, 1)
                    
#             # Cria um Dic com chaves e valores recebidos do loop
#             ResultOperacao = {'¬A' : []}
#             ResultOperacao['¬A'] = valor
                    
#             # Adiciona a coluna de resultado na tabela formada nesta função e retorna a tabela completa com operações e resultados        
#             ColResul = pd.DataFrame(ResultOperacao)
#             TabelaFinal = pd.concat([tabela, ColResul], axis= 1) 
#             return TabelaFinal    
        
#     else:
#         return print("Nenhuma tabela foi fornecida!")

# # Execução do código
# Menu() 
