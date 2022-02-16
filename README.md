# Academia Capgemini

Neste repositório se encontra meu código para o desafio do programa Academia Capgemini 2022 promovido pela empresa Capgemini.

<h1>Instruções</h1>

A linguagem utilizada no script para esse teste foi a linguagem python, então antes de prosseguir com o restante das intruções, verifique se o python esa instalado na sua máquina.
Se não tiver o python instalado na máquina, baixe e instale para poder dar continuidade: https://www.python.org/downloads/

Após a instalação do python na sua máquina, baixe o repositório e execute o arquivo desafioCapgemini.py em algum IDE de sua preferência, mas lembre-se de deixar todos os arquivos na mesma máquina, pois o progroma usa OOP, se os arquivos estiverem espalhados, a importação de uma função para o funcionamento do script irá falhar.

<h1> Questão 03 - feedback </h3>

A terceira questão do desafio ficou díficil de entender, porque no enunciando pede um algoritmo que encontre o número de PARES de substrings que são anagramas. Porém no exemplo 1 o caracter 'o' é considerado um anagrama de 'o', só que um caracter pode ser considerado um anagrama de outro? Nesse caso não existe uma nova ordem de letras para formar uma palavra ou um conjunto de letras diferente. E no exemplo foi encontrado 3 pares de substrings, significando que tem 6 substrings anagramas?

Para não entregar uma questão em branco isso o meu resultado da questão 3 foi baseado no seguinte:
O algoritmo encontra as possiveis substrings de uma string e informa quantos pares de substrings são anagramas entre si. Exemplo: as possiveis substrings de "ovo" são: o,ov,ovo,v,vo,o.
Nesse caso ov e vo são anagramas entre si pois usam os mesmos caracteres, mas estão organizados de formas diferentes. logo temos 01 par de substrings que são anagramas entre si.
No arquivo questao3.py deixei comentarios que irão ajudar a seguir a linha de raciocínio que tive para formular a resposta.
