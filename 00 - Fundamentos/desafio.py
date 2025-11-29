import textwrap

def mensagem():
    return "\nRetornando ao menu... \n"

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuarios = []

    menu = f"""

    {"=".center(50,"=")}
    {" Sistema Bancário DIO ".center(50,"=")}
    {"=".center(50,"=")}

    Olá, Usuário. O que você quer fazer hoje?

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [c] Criar usuário
    [n] Nova conta
    [q] Sair

    => """

    while True:

        opcao = input(textwrap.dedent(menu))

        if opcao == "d":
            deposito(saldo, extrato)        

        elif opcao == "s":
            sacar(
                saldo=saldo, 
                limite=limite, 
                limite_saques=LIMITE_SAQUES, 
                numero_saques=numero_saques
            )


        elif opcao == "e":
            mostrar_extrato(saldo, extrato=extrato)
        
        elif opcao == "c":
            criar_usuarios(usuarios)

        elif opcao == "a":
            criar_conta()

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

def deposito(saldo, extrato, /):
    valor = float(input("Informe o valor do depósito: \n\n"))

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depositado o valor de {valor:.2f} com sucesso!\n\n")
        print(f"Saldo Atual: {saldo}\n")
        print(print(mensagem()))

    else:
        print("Operação falhou! O valor informado é inválido.\n")
        print(print(mensagem()))

    return saldo, extrato

def sacar(*, saldo, limite, numero_saques, limite_saques):
    valor = float(input("Informe o valor do saque: "))

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
        print(mensagem())

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
        print(mensagem())

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
        print(mensagem())

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(mensagem())

    else:
        print("Operação falhou! O valor informado é inválido.")
        print(mensagem())


def mostrar_extrato(saldo, /, *, extrato):
    print(" EXTRATO ".center(50,"="))
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=".center(50,"="))

def criar_usuarios(usuarios):
    novo_usuario = {}
    novo_usuario["cpf"] = input("CPF: ")
    logradouro = ""
    numero = ""
    bairro = ""
    cidade = ""
    estado = ""

    if novo_usuario in usuarios:
        print("\nEsse CPF já possui cadastro, utilize outro.")
        criar_usuarios(usuarios)

    novo_usuario["nome"] = input("Nome: ")
    novo_usuario["data_nascimento"] = input("Data de nascimento: ")
    logradouro = input("Rua: ")
    numero = input("N°: ")
    bairro = input("Bairro: ")
    novo_usuario["endereco"] = f"{logradouro}, {numero} - {bairro} - {cidade}/{estado}"
    usuarios.append(novo_usuario)
    print("\nUsuário cadastrado com sucesso!")


def criar_conta():
    print("Criando conta")

main()