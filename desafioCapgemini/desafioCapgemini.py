from questao2 import questaoDois
from questão1 import questaoUm
from questao3 import questaoTres

print("Desafio Capgemini:")
repetir = "S"

while repetir != "N":
    print("\nMenu de questões:\n1 - Questão 1\n2 - Questão 2\n3 - Questão 3\n")
    escolha = int(input("Selecione uma das opcões: \n"))
    if escolha == 1:
        while repetir == "S":
            questaoUm()
            while repetir != "S" or repetir != "N":
                resposta = input("Deseja rodar a questão novamente(S/N)?: ")
                repetir = resposta.upper()
                if repetir == "S" or repetir == "N":
                    break
                else:
                    print("Informe uma opção válida.")
    if escolha == 2:
        while repetir == "S":
            questaoDois()
            while repetir != "S" or repetir != "N":
                resposta = input("Deseja rodar a questão novamente(S/N)?: ")
                repetir = resposta.upper()
                if repetir == "S" or repetir == "N":
                    break
                else:
                    print("Informe uma opção válida.")
    if escolha == 3:
        while repetir == "S":
            questaoTres()
            while repetir != "S" or repetir != "N":
                resposta = input("Deseja rodar a questão novamente(S/N)?: ")
                repetir = resposta.upper()
                if repetir == "S" or repetir == "N":
                    break
                else:
                    print("Informe uma opção válida.")
    while repetir != "S" or repetir != "N":
        resposta = input("Deseja voltar ao menu de questões(S/N)?: ")
        repetir = resposta.upper()
        if repetir == "S" or repetir == "N":
            break
        else:
            print("Informe uma opção válida.")