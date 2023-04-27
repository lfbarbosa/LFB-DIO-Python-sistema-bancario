
menu= '''

[d] Depositar
[s] Sacar
[e] Extrato
[q] sair


=> '''

saldo = 0
limite = 500
extrato = ""
numero_saques = 3
LIMITE_SAQUES = 500

while True:

	opcao = input(menu)

	if opcao == "d":
		print("Depósito")
		valor_deposito = float(input("insira o valor do depósito: "))
		if(valor_deposito>0):
			saldo+=valor_deposito
			print("depósito realizado com sucesso")
			extrato = extrato + f"depósito realidado no valor de R$ {valor_deposito}\n"
		else:
			print("Valor invalido inserido, tente realizar a operaçao novamente")

	elif opcao == "s":
		print("Saque")
		valor_saque = float(input("insisra o valor do saque: "))
		if valor_saque>0 and valor_saque <=saldo and valor_saque<=500 and numero_saques>0:
			saldo -= valor_saque
			numero_saques -= 1
			print("saque realizado com sucesso")
			extrato = extrato + f"saque realizado no valor de R$ {valor_saque}\n"
		elif saldo<valor_saque:
			print("nao foi possivel realizar o saque, saldo insuficiente!")
		elif LIMITE_SAQUES<valor_saque:
			print("nao foi possivel realizar o saque, o valor excede o valor permitido para saques")
		elif numero_saques<=0:
			print("nao foi possivel realizar o saque, numero de saques diario excedido") 
		else:
			print("O valor informado é invalido!")

	elif opcao == "e":
		print("############EXTRATO############")
		print(extrato)
		print(f"saldo: R$ {saldo}")
		print("###############################")
		continue
	
	elif opcao == "q":
		break		

	else:
		print("Operacao invalida, por favor escolha uma opcao valida")

