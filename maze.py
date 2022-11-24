#coding=UTF-8
#Trabalho 2 - Ferramentas de CAD
#Geovana Silva da Silveira
#Algoritmo Maze Router para uma matriz de tamanho 40x40

source = "S" #inicio do caminho
target = "T" #destino do caminho

#Função utilizada para leitura do arquivo txt de entrada e criação da matriz
def leArquivo():
    with open("entrada.txt") as arquivo:
        matriz = []
        linhas = arquivo.readlines() #le linhas do arquivo
        for l in linhas: #percorre as linhas da matriz
            aux = l.replace(" ","") #remove espacos
            m=[]
            for c in aux:
                m.append(c) 
            matriz.append(m) 
        return matriz

#Le arquivo de entrada e recebe matriz criada
matriz = leArquivo()  

#Função que verifica se achou o target(T)
def encontrouAlvo(matriz,linha,coluna):
    #Verifica se achou um "T" em alguma das quatros direções
    if(matriz[linha-1][coluna]==target or matriz[linha+1][coluna]==target or matriz[linha][coluna-1]==target or matriz[linha][coluna+1]==target):
        return True
    else: #se nao achou um T retorna falso
        return False

#Função que verifica se pode expandir o caminho
def podeExpandir(matriz,linha,coluna):
    #Verifica se tem algum caminho livre(representado pelo 0) para expandir
    if(matriz[linha][coluna]=="0" and matriz[linha][coluna]!="X" and matriz[linha][coluna]!="#" and matriz[linha][coluna]!="-"):
        return True
    else: #Se existe algum bloqueio, retorna falso
        return False

# Função que expande o S até o caminho final T e fornece o comprimento do caminho percorrido
def ExpandeS(matriz,estadoAtual):
    caminho = ""
    
    for linha in range(0,39): #percorre as 40 linhas da matriz
        for coluna in range(0,39): #percorre as 40 colunas da matriz
            if(matriz[linha][coluna]==estadoAtual): #verifica se a matriz está no estado atual
                #verifica se a matriz está no ponto inicial
                if estadoAtual == "S": 
                    #Se o T não estiver na vertical/horizontal
                    if((encontrouAlvo(matriz,linha,coluna))==False):
                        #Marca S como primeiro visitado
                        matriz[linha][coluna]="1"
                        caminho="1"
                    else: #Se o T estiver na vertical/horizontal, imprime comprimento do caminho
                        print("Comprimento: 1")
                        return target #retorna T
                    
                else: #Se nao estiver no S
                    if((encontrouAlvo(matriz,linha,coluna))==False): #se ainda nao achou o target
                        #Verifica se pode expandir para cima
                        if(podeExpandir(matriz,linha-1,coluna)):
                            matriz[linha-1][coluna] = str(int(estadoAtual)+1) #expande para cima
                        #Verifica se pode expandir para baixo
                        if(podeExpandir(matriz,linha+1,coluna)):
                            matriz[linha+1][coluna]= str(int(estadoAtual)+1) #expande para baixo
                        #Verifica se pode expandir para esquerda
                        if(podeExpandir(matriz,linha,coluna-1)):
                            matriz[linha][coluna-1] = str(int(estadoAtual)+1) #expande para esquerda
                        #Verifica se pode expandir para direita
                        if(podeExpandir(matriz,linha,coluna+1)):
                            matriz[linha][coluna+1] = str(int(estadoAtual)+1) #expande para direita
                        
                        #recebe caminho percorrido
                        caminho = str(int(estadoAtual)+1) 
                    else: #Se achou target    
                        #imprime o comprimento do caminho percorrido
                        print("Comprimento:",estadoAtual)
                        return target #retorna T

    return caminho                                        

def imprimeSaida():
    #cria arquivo de saida e permite escrita
    with open("saida.txt","w") as arquivo:
        for linha in matriz:
            for elemento in linha:
                arquivo.write("{:3}".format(elemento))
            arquivo.write("\n")

def main():
    #Inicia o caminho pelo S
    caminho = source
    #Enquanto o caminho for diferente do target(T) expande o caminho
    while(caminho!=target):
        caminho = ExpandeS(matriz,caminho)    

    imprimeSaida() #cria arquivo txt e imprime saida

main()
