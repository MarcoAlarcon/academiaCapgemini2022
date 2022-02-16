def questaoDois():

    caractereEspecial = ["!","@","#","$","%","^","&","*","(",")","-","+"]

    print("\nPara criar uma senha forte, tenha em mente os seguintes topicos:\n1 - Possuir no mínimo 6 caracteres\n2 - Contém no mínimo 1 digito.\n3 - Contém no mínimo 1 letra em minúsculo.\n4 - Contém no mínimo 1 letra em maiúsculo.\n5 - Contém no mínimo 1 dos caracteres especiais: ",end="")
    print(*caractereEspecial,sep=", ")

    senha = input("\nCrie sua senha: ")

    listaErros=[]

    if len(senha) < 1 or len(senha) < 6:
        caracteresFaltantes = 6 - len(senha)
        listaErros.append(str(caracteresFaltantes) + " caracteres faltantes.")
    if any(car.isdigit() for car in senha) == False:
        listaErros.append("Falta um numero.")
    if senha.isupper():
        listaErros.append("Falta uma letra minuscula.")
    if senha.islower():
        listaErros.append("Falta uma letra maiuscula.")
    if any(car in senha for car in caractereEspecial) == False:
        listaErros.append("Falta um caractere especial.")            
    if listaErros:
        print("")
        print(*listaErros,sep="\n")
    else:
        print("Senha forte cadastrada com sucesso!")