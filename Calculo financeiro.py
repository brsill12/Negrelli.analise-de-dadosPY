import os

def limpar_tela():
    os.system('cls')

def pausa():
    print("\n\n")
    os.system('pause')

def mostra_menu():
    print("\n\n\tSimpifica Finanças")
    print("Menu de opções:")
    print("1- Cadastrar Receita") #Chamar funcao add_receita
    print("2- Cadastrar Despesa")#Chamar funcao add_despesa
    print("3- Ver Saldo")#Chamar funcao ver_saldo
    print("4- Listar Extrato")#Chamar funcao listar_extrato
    print("5- Sair") # Sair

def add_receita(receitas):
    descricao = input("Digite a descrição da receita: ")
    valor = float(input("Digite o valor da receita: "))
    receitas.append({"descricao": descricao, "valor" : valor})
    print("Receita cadastrada com sucesso")
    pausa()

def add_despesa(despesas):
    descricao = input("Digite a descrição da despesa: ")
    valor = float(input("Digite o valor da despesa: "))
    despesas.append({"descricao": descricao, "valor" : valor})
    print("Despesa cadastrada com sucesso")
    pausa()

def listar_saldo(receitas,despesas):
    total_receitas = 0
    total_despesas = 0

    for receita in receitas:
        total_receitas +=receita["valor"]
        
    for despesa in despesas:
        total_despesas += despesa["valor"]

    saldo = total_receitas - total_despesas
    print(f"O saldo da conta é {saldo:.2f}")


def listar_extrato(receitas,despesas):
    print("Extrato:")
    print("Receitas:")
    for receita in receitas:
        print(f"{receita['descricao']}: {receita['valor']:.2f}")

    print("Despesas:")
    for despesa in despesas:
        print(f"{despesa['descricao']}: {despesa['valor']:.2f}")
    pausa()
    

def main():
    receitas = []
    despesas =  []
    while True:
        mostra_menu()
        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            add_receita(receitas)
        elif opcao == 2:
            add_despesa(despesas)
        elif opcao == 3:
            listar_saldo(receitas,despesas)
        elif opcao == 4:
            listar_extrato(receitas,despesas)
        elif opcao == 5:
            print("Saindo do Programa...")
            break
        else:
            print("Opção Inválida. Por favor escolha a opção correta")

main()
