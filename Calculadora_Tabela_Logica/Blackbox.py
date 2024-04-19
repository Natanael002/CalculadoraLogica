# Importação de Bibliotecas
import pandas as pd
import re
import itertools
import ttg

# Verificar se a expressão é válida
def ValidarExpressao(expressaoCalculadora):
    # Verificar se a expressão está vazia
    if not expressaoCalculadora.strip():
        return False, '\nExpressão vazia'
    else:
        # Verificar se os parênteses estão balanceados
        count_parenteses = 0
        for char in expressaoCalculadora:
            if char == '(':
                count_parenteses += 1
            elif char == ')':
                count_parenteses -= 1
                
        if count_parenteses != 0:
            return False, '\nParenteses desbalanceado'
        else:    
            # Verificar se há operadores sem operandos
            padrao_operadores_sem_operandos = re.compile(r'[∧∨⇒⇔](?!\w|[(])|(?<![\w)])[∧∨⇒⇔]')
            if padrao_operadores_sem_operandos.search(expressaoCalculadora):
                return False, "\nA expressão contém operadores sem operandos"
            else: 
                if "A" in expressaoCalculadora and "B" in expressaoCalculadora and "C" in expressaoCalculadora and "D" in expressaoCalculadora:
                    termos = ['A', 'B', 'C', 'D']
                    return truth_table(termos, expressaoCalculadora)
                elif "A" in expressaoCalculadora and "B" in expressaoCalculadora and "C" in expressaoCalculadora:
                    termos = ['A', 'B', 'C']
                    return truth_table(termos, expressaoCalculadora)
                elif "A" in expressaoCalculadora and "B" in expressaoCalculadora:
                    termos = ['A', 'B']
                    return truth_table(termos, expressaoCalculadora)
                elif "A" in expressaoCalculadora:
                    termos = ['A']
                    return truth_table(termos, expressaoCalculadora)

    
def tranformar_expression(expression):
    # Substitua os operadores lógicos pelos equivalentes aceitos pelo ttg
    expression = expression.replace('∨', ' or ')
    expression = expression.replace('∧', ' and ')
    expression = expression.replace('¬', '~')
    expression = expression.replace('⇒', '=>')
    expression = expression.replace('⇔', '=')
    expression = expression.replace('⊕', 'xor')
    expression = expression.replace('⊻', 'nand')

    # Adicione parênteses extras para garantir a ordem correta de avaliação
    # expression = "(" + expression + ")"

    return expression

# Cria Tabela verdade
def resultado(expression, termos):
    
    expressao = tranformar_expression(expression)
    print(f"antes: {expression}")
    print(f"Depois: {expressao}")
    # Cria a Tabela Verdade
    tabela = ttg.Truths(termos, [expressao], ints=True, ascending=True) 
    
    # Transforma em dataframe
    tabela_df = tabela.as_pandas
    
    # Separa a coluna de resultado
    ultima_coluna = tabela_df.iloc[:, -1]
   
    # Verifica qual o tipo da tabela
    tipo = tabela.valuation()
    
    return ultima_coluna

def truth_table(variables, expression):
    # Crie um DataFrame para armazenar a tabela verdade
    # truth_table_df = pd.DataFrame(columns=variables + [expression]) #Trocar o result pela expressão pura que vem da calculadora 
    truth_table_df = pd.DataFrame()
    
    truth_values = list(itertools.product([0, 1], repeat=len(variables)))
    # Adicione as combinações como linhas ao DataFrame
    for values in truth_values:
        row_data = dict(zip(variables, values))
        truth_table_df = pd.concat([truth_table_df, pd.DataFrame(row_data, index=[0])], ignore_index=True)
    
    linhas = resultado(expression, variables)
    
    # Cria um dataframe para armazenar tabela de resultado da expressão    
    colunaresult = pd.DataFrame({f'{expression}': linhas})
    colunaresult.index = truth_table_df.index
    
    # Adicionar os valores na coluna resultado
    colunaresult[f'{expression}'] = linhas
    colunaresult = pd.DataFrame({f'{expression}': linhas})
    colunaresult.index = truth_table_df.index
    truth_table_df = pd.concat([truth_table_df, colunaresult],axis= 1) 

        
    return True, truth_table_df


# termos = 'A', 'B', 'C', 'D'
# exp = 'A or B and C => D'
# print(ttg.Truths(['A', 'B', 'C', 'D'], [exp], ints=True, ascending=True)) # Colunas ao contrário 0 0 0 
