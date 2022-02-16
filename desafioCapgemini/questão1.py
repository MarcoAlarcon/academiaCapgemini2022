def questaoUm():
    try:
        numeroEscada = int(input("\nInforme um número inteiro para criar a escada: "))
        if numeroEscada > 0:
            for x in range(1,numeroEscada+1):
                qtdeEspaco = numeroEscada - x 
                qtdeAsterisco = numeroEscada - qtdeEspaco
                espaco = " " * qtdeEspaco
                asterisco = "*" * qtdeAsterisco
                print(espaco + asterisco)
        else:
            print("Informe um número maior que zero.")
    except:
        print("Insira um número inteiro.")