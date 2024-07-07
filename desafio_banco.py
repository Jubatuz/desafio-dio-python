menu = """

[1] Depósito
[2] Sacar
[3] Extrato
[4] Sair

===> """

saldo = 0
limite = 500
numero_saque = 0
LIMITE_SAQUES = 3
extrato = ""

while True:
    
    opcoes = int(input(menu))
    
    if opcoes == 1:
        valor = float(input("Digite o valor que deseja depositar: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito de R$ {valor:.2f}\n"
    
        else:
         print("não é possivel realizar esse depósito!")
    
    elif opcoes == 2:
        valor = float(input("Digite p valor que deseja sacar: "))

        excedeu_saldo = valor > saldo

        excedeu_valor = valor > limite

        excedeu_limite = numero_saque >=LIMITE_SAQUES

        if excedeu_valor:
            print("Operação inválida! valor do saque ultrapassou o saldo.")
        
        elif excedeu_limite:
            print("Operaçõa inálida! Ultrapassou o limite diário.")

        elif excedeu_valor:
            print("Operação Inválida! ultrapassou o limite de saques dia.")
        
        elif valor > 0:
            saldo -= valor
            extrato = f"Valor de saque: R${valor:.2f}\n"
            numero_saque +=1
        
        else:
            print("Operação inválida!")

    elif opcoes == 3:
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
    
    elif opcoes == 4:
        break

    else:
        print("Operação Inválida!")




    


