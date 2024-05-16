# Importação de Bibliotecas
import pandas as pd
import re
import itertools
import ttg

# Verificar se a expressão é válida
def ValidarExpressao(expressaoCalculadora):
    # Verifica se a expressão está vazia
    if not expressaoCalculadora.strip():
        return False, '\nExpressão vazia'
    else:
        # Verifica se os parênteses estão balanceados
        count_parenteses = 0
        for char in expressaoCalculadora:
            if char == '(':
                count_parenteses += 1
            elif char == ')':
                count_parenteses -= 1
                
        if count_parenteses != 0:
            return False, '\nparêntesis desbalanceado'
        else:    
            # Verificar se há operadores sem operandos
            padrao_operadores_sem_operandos = re.compile(r'[∧∨→↔+⊻](?!\w|[(])|(?<![\w)])[∧∨→↔+⊻]')
            
            if padrao_operadores_sem_operandos.search(expressaoCalculadora):
                return False, "\nExpressão inválida"
            else: 
                if "A" in expressaoCalculadora and "B" in expressaoCalculadora and "C" in expressaoCalculadora and "D" in expressaoCalculadora:
                    termos = ['A', 'B', 'C', 'D']
                    return tabelaVerdade(termos, expressaoCalculadora)
                elif "A" in expressaoCalculadora and "B" in expressaoCalculadora and "C" in expressaoCalculadora:
                    termos = ['A', 'B', 'C']
                    return tabelaVerdade(termos, expressaoCalculadora)
                elif "A" in expressaoCalculadora and "B" in expressaoCalculadora:
                    termos = ['A', 'B']
                    return tabelaVerdade(termos, expressaoCalculadora)
                elif "B" in expressaoCalculadora and "C" in expressaoCalculadora:
                    termos = ['B', 'C']
                    return tabelaVerdade(termos, expressaoCalculadora)
                elif "C" in expressaoCalculadora and "D" in expressaoCalculadora:
                    termos = ['C', 'D']
                    return tabelaVerdade(termos, expressaoCalculadora)
                elif "A" in expressaoCalculadora:
                    termos = ['A']
                    return tabelaVerdade(termos, expressaoCalculadora)

    
def tranformar_expression(expression):
    # Substitua os operadores lógicos pelos equivalentes aceitos pelo ttg
    expression = expression.replace('∨', ' or ')
    expression = expression.replace('∧', ' and ')
    expression = expression.replace('~', '~')
    expression = expression.replace('→', '=>')
    expression = expression.replace('↔', '=')
    expression = expression.replace('+', ' xor ')
    expression = expression.replace('⊻', ' nand ')

    return expression

# Cria Tabela verdade
def resultado(expression, termos):
    
    expressao = tranformar_expression(expression)
    
    # Cria a Tabela Verdade
    tabela = ttg.Truths(termos, [expressao], ints=True, ascending=True) 
    
    # Transforma em dataframe
    tabela_df = tabela.as_pandas
    
    # Separa a coluna de resultado
    ultima_coluna = tabela_df.iloc[:, -1]
   
    # Verifica qual o tipo da tabela
    tipo = tabela.valuation()
    
    # Traduz os nomes
    if tipo == "Contingency":
        tipo = "Tabela de Contigência"
    elif tipo == "Tautology":
        tipo = "Tabela de Tautologia"
    elif tipo == "Contradiction":
        tipo = "Tabela de Contradição"
    
    return tipo, ultima_coluna

def tabelaVerdade(termos, expression):
    # Crie um DataFrame para armazenar a tabela verdade
    tabelaVerdade_df = pd.DataFrame()
    
    # Cria todas as combinações possíveis de 0 e 1 dependendo da quantidade de termos
    truth_values = list(itertools.product([0, 1], repeat=len(termos)))
    
    # Adicione as combinações como linhas ao DataFrame
    for values in truth_values:
        row_data = dict(zip(termos, values))
        tabelaVerdade_df = pd.concat([tabelaVerdade_df, pd.DataFrame(row_data, index=[0])], ignore_index=True)
    
    tipoTabela, linhas = resultado(expression, termos)
    
    # Cria um dataframe para armazenar tabela de resultado da expressão    
    colunaresult = pd.DataFrame({f'{expression}': linhas})
    
    # Torna os indices da tabela verdade com a da coluna a ser adicional iguais
    colunaresult.index = tabelaVerdade_df.index
    
    # Adicionar os valores na coluna resultado
    colunaresult[f'{expression}'] = linhas
    colunaresult = pd.DataFrame({f'{expression}': linhas})
    colunaresult.index = tabelaVerdade_df.index
    tabelaVerdade_df = pd.concat([tabelaVerdade_df, colunaresult],axis= 1) 

        
    return tipoTabela, tabelaVerdade_df



