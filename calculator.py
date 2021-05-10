print('Que calculo deseja fazer?:')

def soma():
	Numero1 = float(input("Digite o Primeiro valor:"))
	Numero2 = float(input("Digite o Segundo valor:"))
	resultado = Numero1 + Numero2

	print('\nO A sua conta é:\n ', Numero1, '\n+', Numero2, '\n=',resultado)

def subtracao():
	Numero1 = float(input("Digite o Primeiro valor:"))
	Numero2 = float(input("Digite o Segundo valor:"))
	resultado = Numero1 - Numero2

	print('\nO A sua conta é:\n ', Numero1, '\n-', Numero2, '\n=',resultado)

def multiplicacao():
	Numero1 = float(input("Digite o Primeiro valor:"))
	Numero2 = float(input("Digite o Segundo valor:"))
	resultado = Numero1 * Numero2

	print('\nO A sua conta é:\n ', Numero1, '\n*', Numero2, '\n=',resultado)

def divisao():
	Numero1 = float(input("Digite o Primeiro valor:"))
	Numero2 = float(input("Digite o Segundo valor:"))
	resultado = Numero1 / Numero2

	print('\nO A sua conta é:\n ', Numero1, '\n/', Numero2, '\n=',resultado)

def potencia():
	Numero1 = float(input("Digite o Primeiro valor:"))
	Numero2 = float(input("Digite o Segundo valor:"))
	resultado = Numero1 ** Numero2

	print('\nO A sua conta é:\n  ', Numero1, '\n**', Numero2, '\n=',resultado)


opção = 0 

while opção != 6:
	print('\nVamos para outro calculo?\n\n1.Soma\n2.Subtracao\n3.Multiplicacao\n4.Divisao\n5.Potencia\n6.Sair')
	opção = int(input('>'))
	if opção == 1:
		soma()
	elif opção == 2:
		subtracao()
	elif opção == 3:
		multiplicacao()
	elif opção == 4:
		divisao()
	elif opção == 5:
		potencia()
	elif opção == 6:
		print('\nTchaaau!')
	else:
		print('\nOpção inválida!')
