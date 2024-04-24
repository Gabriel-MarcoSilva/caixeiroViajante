import math
import matplotlib.pyplot as plt
import time

#abre o arquivo
arquivo = open('./kroA100.txt', "r")

#inicialização das variáveis
lista = []
menoresValores = []
x = []
y = []
index = []
indexX = []
indexY = []

def leArquivo():
    for i in arquivo: #faz uma verificação se em cada linha o primeiro elemento é um número
        try: #se sim é atribuído à lista a linha constendo as coordenadas do ponto
            numero = int(i.split(' ')[0])
            lista.append(i[len(str(numero)) + 1 :len(i)-1]) #1 -> [1:final-1]; 10 -> [2: final-1]; 100 -> [3: final-1]
        except: #caso contrário nada faz
            None

    for i in lista: #formata a lista para que só tenha as coordenadas separando em X e Y, ambas fazem a mesma coisa, mas como 1 e 10 tem quantidade de dígitos diferentes aparece um ' ' que deve ser retirado
        x.append(float(i.split(' ')[0]))
        y.append(float(i.split(' ')[1]))
        

def euclidiana(val1, val2, val3, val4): #faz a distância euclidiana
    conta = math.sqrt(((val2-val1)**2 + (val4-val3)**2)) # √((x_2-x_1)² + ((y_1 - y_2)²))
    return float(format(conta, '.2f')) #formata o retorno para duas casas decimais

def montaMatriz (x,y): #monta a matriz com as distâncias de cada ponto
    matriz = []
    for (index, i) in enumerate(x):
        linha = []
        for (jindex, j) in enumerate(y): #cria a matriz
            if index != jindex :
                linha.append(euclidiana(x[index], x[jindex], y[index], y[jindex])) # cria linha por linha
            else: #quando os index são iguais então recebe 0
                linha.append(0.0)
        matriz.append(linha)
    return matriz

def vizinhoMaisProximo (): #gera as arestas

    indexContinua = 51
    index.append(indexContinua)

    while len(index) < len(matrizMontada) :
        menor = 100000

        for i, linha in enumerate(matrizMontada[indexContinua]):
            if menor > linha and linha > 0 and not(i in index):
                menor = linha
                indexContinua = i

        index.append(indexContinua)
        menoresValores.append(menor)

    primeiroIndex = (x[index[0]], y[index[0]])
    ultimoIndex = (x[index[len(index)-1]], y[index[len(index)-1]])

    ultimaRota = euclidiana(primeiroIndex[0], ultimoIndex[0], primeiroIndex[1], ultimoIndex[1]) #faz a interligação com do ultimo com o primiero vertice
    
    menoresValores.append(ultimaRota)
    index.append(index[0])

    for i in index:
        indexX.append(x[i])
        indexY.append(y[i])

def somaTermos():
    soma = 0
    cont = 0
    for i, linha in enumerate(matrizMontada):
        soma += linha[0]
        cont += 1
    print(f'{soma:.2f} km')


def plotaGrafico(x, y): #plota o gráfico
    pontos = list(zip(x, y))
    
    plt.scatter(x, y, color='red')
    

    x.append(x[0])
    y.append(y[0])

    # plt.plot(x, y, color='blue', linestyle='-')
    plt.plot(indexX, indexY, color='green', linestyle='-')
    for i, (x, y) in enumerate(pontos):
        plt.text(x, y, f'{i+1}', fontsize=10, ha='right', va='bottom')
    
    # Adicionar legendas e título
    plt.xlabel('Coordenada X')
    plt.ylabel('Coordenada Y')
    plt.title('kroA100')

    # Exibir o gráfico
    plt.show()

# #vizinhança, modo guloso

#chama as funções

start_time = time.time()

leArquivo()

matrizMontada = montaMatriz(x,y)

vizinhoMaisProximo()

# somaTermos()

soma = 0.00     

for i in menoresValores:
    soma += i

end_time = time.time()
print(f'custo computacional: {end_time-start_time:.6f}s')
print(f'menor distância: {soma:.2f}km')

plotaGrafico(x,y)
