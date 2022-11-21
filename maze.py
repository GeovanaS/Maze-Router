# Trabalho 2 - Ferramentas de CAD 
# Geovana Silva da Silveira
# Algoritmo Maze Router para uma matriz de tamanho 40x40

source = "S" #inicio do caminho
target = "T" #destino do caminho

#Função utilizada para leitura do arquivo txt de entrada e criação da matriz
def leMatriz():
	with open("entrada.txt") as arquivo: #abre arquivo de entrada
		matriz = []
		linhas = arquivo.readlines() #le linhas do arquivo
		for l in linhas: #percorre as linhas da matriz
			aux = l.replace(" ","").replace("\n","") 
			m = []
			for c in aux:
				m.append(c)
			matriz.append(m)
		return matriz

#le o arquivo de entrada e cria matriz
matriz = leMatriz()


#funcao auxiliar para escrever a matriz com a solucao
def escreveSaida():
	with open("saida.txt","w") as arquivo:
		for linha in matriz:
			for elemento in linha:
				arquivo.write("{:3}".format(elemento))
			arquivo.write("\n")


#funcao que verifica se achou o target
def encontrouAlvo(matriz,linha,coluna):
	#verifica se achou um "T" em alguma das quatros direcoes 
    if (matriz[linha-1][coluna]==target or matriz[linha+1][coluna]==target or matriz[linha][coluna-1]==target or matriz[linha][coluna+1]==target):
          return True
    else:
          return False      

#funcao que verifica se pode expandir o caminho
def podeExpandir(matriz,linha,coluna):
	#verifica se tem caminho livre para expandir
	if (matriz[linha][coluna]=="0" and matriz[linha][coluna]!="#" and matriz[linha][coluna]!='-' and matriz[linha][coluna]!="X"):
		return True
	else:
		return False


#Expande o S até o caminho T seja encontrado e fornece o comprimento deste caminho
def expandeS(matriz,source):
    caminho = ""

    for linha in range (0,39): #percorre as 40 linhas da matriz
    	for coluna in range (0,39): #percorre as 40 colunas da matriz
            if matriz[linha][coluna] == source: 
               if source =="S":  #verifica se matriz esta no ponto inicial do caminho
               	if(not(encontrouAlvo(matriz,linha,coluna))): 
               		matriz[linha][coluna] = "1" #se está no S marca como primeiro visitado 
               		caminho = "1"
               	else:
               		print("Comprimento: 1") #se achou o target, imprime comprimento 1 
               		return target

               else:
               	if(not(encontrouAlvo(matriz,linha,coluna))): #se ainda nao achou target
               		if(podeExpandir(matriz,linha-1,coluna)): #verifica se pode expandir para cima
               				matriz[linha-1][coluna] = str(int(source)+1) #move para cima

               		if(podeExpandir(matriz,linha+1,coluna)): #verifica se pode expandir para baixo
               				matriz[linha+1][coluna] = str(int(source)+1) #move para  baixo

               		if(podeExpandir(matriz,linha,coluna-1)): #verifica se pode expandir para esquerda
               				matriz[linha][coluna-1] = str(int(source)+1) #move para esquerda 

               		if(podeExpandir(matriz,linha,coluna+1)): #verifica se pode expandir para direita
               				matriz[linha][coluna+1] = str(int(source)+1) #move para direita

               		caminho = str(int(source)+1) 

               	else: #se achou o target
               		print("Comprimento:",source)  #imprime o comprimento do caminho
               		return target 

    return caminho 


def main():
	caminho=source #inicia o caminho pelo S
	while(caminho!=target): #enquanto o caminho for diferente do target(T) expande o caminho
		caminho = expandeS(matriz,caminho)

	escreveSaida() #cria arquivo txt de saida


main()


