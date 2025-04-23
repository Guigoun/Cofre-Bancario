#Gabriel Lopes 2314290121 | Guilherme Licati 2314290112 | Caio Corrêa 2314290100 | Guilherme Segatto 2314290094

def menu():
    Menu =  ('''\nEscolha uma das opções abaixo:
[1] - Saldo
[2] - Saque
[3] - Depósito
[4] - Extrato
[5] - Simular Investimento
[0] - Sair
: ''')
    return Menu

def mostrar_saldo(saldo):
    print(f"Seu saldo é de R${saldo:.2f}")
    return saldo

def Saque(*, saldo, valor, extrato, LIMITE_SAQUE_D, numero_saques, LIMITE_SAQUES):
    if saldo == 0:
        print("Não foi possível efetuar o saque, saldo insuficiente!")
    elif numero_saques == LIMITE_SAQUES:
        print("O limite de saques diários são 3!")
    elif valor > LIMITE_SAQUE_D:
        print("O valor máximo permitido é de R$ 500,00")
    elif valor > saldo:
        print("Saldo insuficiente para este saque.")
    else:
        saldo -= valor
        numero_saques += 1
        print(f"Você sacou R${valor:.2f}")
        extrato += f'Saque de R${valor:.2f}\n'

    return saldo, extrato, numero_saques

def Deposito(saldo, valor, extrato, /):
    if valor <= 0:
        print("O valor do depósito deve ser maior que zero!")
    else:
        saldo += valor
        extrato += f'Depósito de R${valor:.2f}\n'
        print(f"Você depositou R${valor:.2f}")
    return saldo, extrato

def mostrar_extrato(saldo, /, *, extrato):
    print('<======== EXTRATO ========>')
    print('Não foram realizadas movimentações.' if not extrato else extrato)
    print(f'Saldo atual: R${saldo:.2f}')
    print('<=========================>')


def calcular_rendimento(valor_investido, dias):
    taxa_anual = 0.1415
    taxa_diaria = (1 + taxa_anual) ** (1 / 365) - 1

    rendimento_bruto = valor_investido * ((1 + taxa_diaria) ** dias - 1)
    desconto_iof = calcular_iof(rendimento_bruto, dias)
    desconto_ir = calcular_ir(rendimento_bruto - desconto_iof, dias)

    valor_liquido = valor_investido + rendimento_bruto - desconto_iof - desconto_ir

    return {
        "valor_investido": valor_investido,
        "rendimento_bruto": rendimento_bruto,
        "desconto_iof": desconto_iof,
        "desconto_ir": desconto_ir,
        "valor_liquido": valor_liquido
    }

def calcular_iof(rendimento, dias):
    if dias > 30:
        return 0.0
    tabela_iof = [
        0.96, 0.93, 0.90, 0.86, 0.83, 0.80, 0.76, 0.73, 0.70, 0.66,
        0.63, 0.60, 0.56, 0.53, 0.50, 0.46, 0.43, 0.40, 0.36, 0.33,
        0.30, 0.26, 0.23, 0.20, 0.16, 0.13, 0.10, 0.06, 0.03, 0.00
    ]
    return rendimento * tabela_iof[dias - 1]

def calcular_ir(rendimento, dias):
    if dias <= 180:
        aliquota = 0.225
    elif dias <= 360:
        aliquota = 0.20
    elif dias <= 720:
        aliquota = 0.175
    else:
        aliquota = 0.15
    return rendimento * aliquota

def simular_investimento():
    print("\n=== Simulador da Caixinha Super Cofrinho ===")
    try:
        valor = float(input("Digite o valor a ser investido (ex: 1000.00): R$ "))
        dias = int(input("Digite o tempo do investimento (em dias): "))

        resultado = calcular_rendimento(valor, dias)

        print("\n=== Resultado da Simulação ===")
        print(f"Valor investido:       R$ {resultado['valor_investido']:.2f}")
        print(f"Rendimento bruto:      R$ {resultado['rendimento_bruto']:.2f}")
        print(f"Desconto IOF:          R$ {resultado['desconto_iof']:.2f}")
        print(f"Desconto IR:           R$ {resultado['desconto_ir']:.2f}")
        print(f"Valor líquido final:   R$ {resultado['valor_liquido']:.2f}")
    except ValueError:
        print("Entrada inválida. Por favor, digite números válidos.")

def main():
    saldo = 0
    numero_saques = 0
    extrato = ""
    LIMITE_SAQUES = 3
    LIMITE_SAQUE_D = 500

    while True:
        try:
            opcao = int(input(menu()))
        except ValueError:
            print("Entrada inválida. Digite um número correspondente à opção.")
            continue

        if opcao == 1:
            mostrar_saldo(saldo)
        elif opcao == 2:
            valor = float(input("Digite o valor de saque: R$ "))
            saldo, extrato, numero_saques = Saque(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                LIMITE_SAQUE_D=LIMITE_SAQUE_D,
                numero_saques=numero_saques,
                LIMITE_SAQUES=LIMITE_SAQUES
            )
        elif opcao == 3:
            valor = float(input("Digite o valor que deseja depositar: R$ "))
            saldo, extrato = Deposito(saldo, valor, extrato)
        elif opcao == 4:
            mostrar_extrato(saldo, extrato=extrato)
        elif opcao == 5:
            simular_investimento()
        elif opcao == 0:
            print("Saindo...")
            break
        else:
            print("Comando Inválido!")

if __name__ == "__main__":
    main()
