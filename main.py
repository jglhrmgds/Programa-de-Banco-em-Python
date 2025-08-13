def mostrar_saldo():
    print(f"Seu saldo é: R${saldo:.2f}")

def depositar():
    quantidade = float(input("Insira uma quantidade a ser depositada: "))

    if quantidade < 0:
        print("Essa não é uma quantidade válida")
        return 0
    else:
        return quantidade

def sacar():
    quantidade = float(input("Insira uma quantidade a ser sacada: "))

    if quantidade > saldo:
        print("Saldo insuficiente")
        return 0
    elif quantidade < 0:
        print("Quantidade precisa ser maior que 0")
        return 0
    else:
        return quantidade

saldo = 0
esta_rodando = True

while esta_rodando:
    print("Programa de Banco")
    print("1. Mostrar saldo bancário")
    print("2. Depositar")
    print("3. Sacar")
    print("4. Sair")

    escolha = input("Insira sua escolha (1-4): ")

    if escolha == '1':
        mostrar_saldo()
    elif escolha == '2':
        saldo += depositar()
    elif escolha == '3':
        saldo -= sacar()
    elif escolha == '4':
        esta_rodando = False
    else:
        print("Escolha inválida")

print("Obrigado, tenha um ótimo dia")
