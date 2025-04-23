def menu():
    Menu =  ('''\nEscolha uma das opções abaixo:\n[1] - Saldo\n[2] - Saque\n[3] - Depósito\n[4] - Extrato\n[5] - Cadastrar Usuário\n[6] - Criar Conta Corrente\n[7] - Listas Contas\n[0] - Sair\n: ''')

    return Menu
   
def mostrar_saldo(saldo):
    print(f"Seu saldo é de R${saldo:.2f}")

    return saldo

def Saque(*, saldo, valor, extrato, LIMITE_SAQUE_D, numero_saques,LIMITE_SAQUES):

    if saldo == 0:
        print("Não foi possivel efetuar o saque, o saldo insufisiente!")

    if numero_saques == LIMITE_SAQUES:
        print("O limite de saques diários são 3!")

    elif valor > LIMITE_SAQUE_D:
        print("O valor máximo permitido é de R$ 500,00")

    elif valor and saldo > 0:
        saldo-=valor
        numero_saques+=1
            
        print(f"Você sacou R${valor:.2f}")
        extrato += f'Saque de R${valor:.2f}\n'


    return saldo, extrato, numero_saques

def Deposito(saldo, valor, extrato, /):
    
    if valor <= 0:
        print("O valor do depósito deve ser maior que zero!")
    else:
        saldo+=valor
        
        extrato += f'Depósito de R${valor:.2f}\n'
        print(f"Voce depositou R${valor:.2f}")
        
    return saldo, extrato

def mostrar_extrato(saldo,/,*,extrato):
    print('<========EXTRATO========>')
    print('Não foram realizadas movimentações.' if not extrato else extrato)
    print(f'Saldo atual: {saldo:.2f}')
    print('<=======================>')

def filtrar_usuario(cpf, usuarios):
   usuarios_filtrados = [usuario for usuario in usuarios if usuario["CPF"] == cpf]
   return usuarios_filtrados[0] if usuarios_filtrados else None

def cadastrar_usuario(usuarios):
    cpf = (input("Digite seu cpf: "))
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe um usuário com esse CPF!")
        return
     

    nome = input("Digite seu nome completo: ")
    data_nasc = (input("Digite sua data de nascimento: "))
    endereço = input("Digite seu endereço: ")

    usuarios.append({"nome": nome, "Data de Nascimento": data_nasc, "CPF": cpf, "Endereço": endereço})
    print("\nUsuário cadastrado com sucesso!")

def conta_corrente(agencia, numero_conta, usuarios):
    cpf = (input("Digite seu cpf: "))
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta Criada com Sucesso!")
        return {"agencia": agencia, "numero da conta": numero_conta, "usuario": usuario}

def listar_contas(contas):
    for conta in contas:
        linha = f'''
            Agência': {conta['agencia']}\n
            NumeroConta: {conta['numero da conta']}\n
            Titular: {conta['usuario']['nome']}\n
            '''
        print(linha)

def main():
    saldo = 0
    numero_saques = 0
    extrato = ""
    LIMITE_SAQUES = 3
    LIMITE_SAQUE_D = 500
    usuarios = []
    contas = []
    AGENCIA = "0001"
    numero_conta = 1

    while True:

        opcao = int(input(menu()))
    
        if opcao == 1:
            mostrar_saldo(saldo)
       
        elif opcao == 2:
            valor = int(input("Digite o valor de saque: "))
            saldo, extrato, numero_saques = Saque(
                saldo=saldo, 
                valor=valor, 
                extrato=extrato, 
                LIMITE_SAQUE_D=LIMITE_SAQUE_D, 
                numero_saques=numero_saques, 
                LIMITE_SAQUES=LIMITE_SAQUES
            )

        elif opcao == 3:
            valor = int(input("Digite o valor que deseja depositar: "))
            saldo, extrato = Deposito(saldo, valor, extrato)
              
        elif opcao == 4:
            mostrar_extrato(saldo, extrato=extrato)
        
        elif opcao == 5:
            cadastrar_usuario(usuarios)

        elif opcao == 6:
            numero_conta = len(contas) + 1
            conta = conta_corrente(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
                numero_conta +=1

        elif opcao == 7:
            listar_contas(contas)

        elif opcao == 0:
            print("Saindo...")
            break
    
        else:
            print("Comando Inválido!")

main()

