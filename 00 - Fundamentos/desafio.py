import textwrap

def mensagem():
    print("\nRetornando ao menu... \n")

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

    Olá! O que você quer fazer hoje?

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [c] Criar usuário
    [n] Nova Conta
    [q] Sair

    => """

    while True:

        opcao = input(textwrap.dedent(menu))

        if opcao == "d":
           saldo, extrato = deposito(saldo, extrato)        

        elif opcao == "s":
           saldo, extrato = sacar(
                saldo=saldo, 
                limite=limite, 
                limite_saques=LIMITE_SAQUES, 
                numero_saques=numero_saques,
                extrato=extrato
            )


        elif opcao == "e":
            mostrar_extrato(saldo, extrato=extrato)
        
        elif opcao == "c":
            usuarios = cadastrar_usuarios(usuarios)

        elif opcao == "n":
            usuarios = nova_conta(usuarios)

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
        mensagem()

    else:
        print("Operação falhou! O valor informado é inválido.\n")
        mensagem()

    return saldo, extrato

def sacar(*, saldo, limite, numero_saques, limite_saques, extrato):
    valor = float(input("Informe o valor do saque: "))

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
        mensagem()

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
        mensagem()

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
        mensagem()

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        mensagem()

    else:
        print("Operação falhou! O valor informado é inválido.")
        mensagem()

    return saldo, extrato

def mostrar_extrato(saldo, /, *, extrato):
    print(" EXTRATO ".center(50,"="))
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=".center(50,"="))

def cadastrar_usuarios(usuarios):
    cpf_check = input("CPF: ")

    if len(usuarios) == 0:
        usuarios.append(adiciona_usuario(cpf_check))
        return usuarios
    
    lista_cpfs = []
    for usuario in usuarios:
        lista_cpfs.append(usuario['cpf'])
        

    if cpf_check in lista_cpfs:
        print("\nEsse CPF já possui cadastro, por favor tente outro.")
        return usuarios
    else:
        usuarios.append(adiciona_usuario(cpf_check))
        return usuarios

def adiciona_usuario(cpf):
    novo_usuario = {}
    logradouro = ""
    numero = ""
    bairro = ""
    cidade = ""
    estado = ""
    
    novo_usuario["cpf"] = cpf
    novo_usuario["nome"] = input("Nome: ")
    novo_usuario["data_nascimento"] = input("Data de nascimento: ")
    logradouro = input("Rua: ")
    numero = input("N°: ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    estado = input("Sigla Estado: ")
    novo_usuario["endereco"] = f"{logradouro}, {numero} - {bairro} - {cidade}/{estado}"

    print("\nUsuário cadastrado com sucesso!")
    mensagem()
    return novo_usuario

def nova_conta(usuarios):
    
    if not usuarios:
        print("\nNenhum usuário em nossa base, selecione a opção 'c' do menu para cadastrar um usuário.\n")
        mensagem()
        return usuarios
    
    agencia = "0001"
    cpf_check = input("Informe o CPF do usuário: ")
    lista_cpfs = [usuario["cpf"] for usuario in usuarios]

    if cpf_check not in lista_cpfs:
            print("\nNenhum usuário cadastrado com esse CPF.\n")
            mensagem()
    else:
        for usuario in usuarios:
            if usuario.get("cpf") != cpf_check:
                continue
            else:
                lista_chaves = list(usuario.keys())

                if "contas" not in lista_chaves:
                    usuario["contas"] = [{
                        "conta": 1,
                        "agencia": agencia
                    }]
                    print("\nConta 1 criada com sucesso!\n")
                else:
                    numero_contas = len(usuario.get("contas"))

                    usuario["contas"].append({
                        "conta": numero_contas + 1,
                        "agencia": agencia
                    })
                    print(f"\nConta {numero_contas + 1} criada com sucesso!\n")

            break
    return usuarios

main()