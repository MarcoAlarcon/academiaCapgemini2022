from itertools import combinations
from re import X

def questaoTres():
    string = input("\nInforme uma string: ")

    #Cria e alimenta uma lista de possiveis substrings
    possiveisSubstrings=[string[x:y] for x,y in combinations(range(len(string)+1),r=2)]

    #Inicia uma lista que ao decorrer do código vai virar um vetor para validação de pares
    lista2D = []

    #FOR para inserir os dados e transformar a lista em um vetor com as possiveis combinações, os dados são inseridos separando os caracteres.
    for y in range(len(possiveisSubstrings)):
        lista2D.append(list(possiveisSubstrings[y]))

    #Um anagrama consiste em realocar as letras de uma sequencia de caracteres de difeentes maneiras, formando palavras ou não, isso significa que para uma substring ser anagrama de outra substring elas devem conter mais de um caractere e usar os mesmos caracteres. Para checar isso, esse laço FOR ordena em ordem alfabetica a lista que contem todas as possiveis substrings dividas em caracteres.
    for z in range(len(lista2D)):
        lista2D[z].sort()

    #Agora, basta olhar no vetor quais listas são repetidas para obter o numero de substrings pares que são anagramas entre si.
    contador = 0
    for i in range(len(lista2D)):
        if len(lista2D[i]) >=2:
            for j in range(len(lista2D)):
                if lista2D[i] == lista2D[j] and lista2D.index(lista2D[i]) != j:
                    contador += 1

    #Para ver a lista de possiveis substrings, apague o hashtag da próxima linha.
    #print(possiveisSubstrings)

    #Para ver o vetor com as listas de possiveis substrings ordenadas em ordem alfabetica, apague a hashtag da próxima linha.
    #print(lista2D)

    #Como a variavel contador reune a repetição de uma lista no vetor, ele sempre vai ser um número par, por isso para obter o numero de pares de substrings, basta dividir por 2.
    #Usei o metodo round() pois a variavel estava saindo como numero decimal. (ex:1.0), porém em nenhum caso irá se obter um valor quebrado. (ex: 1.5)
    print(str(round(contador/2)) + " par(es) de substrings que são anagramas entre si.")