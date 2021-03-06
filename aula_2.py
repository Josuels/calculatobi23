#1. Você tem uma lista de número: [6,7,4,7,8,4,2,5,7,'hum','dois']. A ideia do 
#exercício é tirar a média de todos os valores contidos na lista, porém para 
#fazer o cálculo precisa remover as strings.

soma = 0
contador = 0
lista_numeros = [6,7,4,7,8,4,2,5,7,'hum','dois']
for i in lista_numeros:
    indice = lista_numeros.index(i)
    if(indice != 9 and indice != 10):
        soma = soma + i
        contador = contador + 1

    media = soma / contador
print('A média é: ', media)

#2.crie um método que receba duas matrizes, some os valores total de cada matriz e
# depois multiple o resultado delas e retorne o valor.

matriz_1 = [1,2,3,4,5]
matriz_2 = [6,7,8,9,10]

def calculo(m1, m2):
    soma1 = 0
    soma2 = 0

    for i in m1:
        soma1 = soma1 + i

    for j in m2:
        soma2 = soma2 + j
        
    print('A soma da matriz_1 é: ', soma1)
    print('A soma da matriz_2 é: ', soma2)
    print('A soma das 2 matrizes é: ', soma1 + soma2)
    print('A multiplicação das matrizes é: ', soma1 * soma2)

calculo(matriz_1, matriz_2)

#3.Criar uma matriz nxm (n = 5, m =7)

import numpy as np

matriz = np.array([[1,2,3,4,5,6,7], [2,3,5,4,6,8,9], [9,5,4,6,1,3,2], [5,7,1,9,6,3,4], [9,7,8,4,1,3,5]])

#a.faça a matriz transposta desta matriz
matriz_t = np.array(matriz).T
print('A impressão da matriz transposta é: \n', matriz_t)

#b.somar toda matrix
soma_matriz = np.sum(matriz)
print('A soma total da matriz é: ', soma_matriz)

#c.somar todas as colunas
soma_coluna = np.sum(matriz, 0)
print('A soma de cada coluna é: ', soma_coluna)

#d.somar todas as linhas.
soma_linha = np.sum(matriz, 1)
print('A soma de cada linha é: ', soma_linha)

#e.retorne o maior valor
maior_valor = np.max(matriz)
print('O maior valor da matriz é: ', maior_valor)

#f.retorne o menor valor.
menor_valor = np.min(matriz)
print('O menor valor da matriz é: ', menor_valor)

#4.Crie uma matriz nxn (n=5). Agora some essa matriz com a matriz do exercício 3.

matriz_nxn = np.array([[1,2,3,5,7], [4,5,3,7,8], [9,8,4,2,3], [4,6,2,7,1], [6,4,3,8,1]])

soma_matriz_nxn = np.sum(matriz_nxn)

soma_matrizes = soma_matriz + soma_matriz_nxn

print('A soma das 2 matrizes é: ', soma_matrizes)

#5.crie um array de números que vai de 0 a 1000.

print(np.arange(1001))

#6. crie uma matriz só de zeros.

print(np.zeros((3,3), dtype=np.int16))
