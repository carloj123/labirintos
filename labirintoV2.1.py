from Vertex import Nodo
lista_2 = list()
testeeee = [['1001','1010','1010','0110'],["0101",'1001','1010','1100'],['0101','0101','1101','0111'],['0011','0010','0010','1010']]
for j in testeeee:
    lista_2.append(j)

def mostra(lista):
    entradas = list()
    i = j = 0
    while i <=len(lista)-1:
        while j <=len(lista[i])-1:
            if i == 0 and j == 0 and (lista[i][j][0] == '0' or lista[i][j][3] == '0'):
                entradas.append(str(i)+' '+str(j))

            elif i == 0 and lista[i][j][0] == '0':
                entradas.append(str(i)+' '+str(j))

            elif i == 0 and j == len(lista[i])-1 and (lista[i][j][0] == '0' or lista[i][j][1] == '0'):
                entradas.append(str(i)+' '+str(j))

            elif i == len(lista)-1 and j == 0 and (lista[i][j][2] == '0' or lista[i][j][3] == '0'):
                entradas.append(str(i)+' '+str(j))

            elif i == len(lista)-1 and j == len(lista[i])-1 and (lista[i][j][2] == '0' or lista[i][j][1] == '0'):
                entradas.append(str(i)+' '+str(j))

            elif (j == 0 and lista[i][j][3] == '0' )or (j == len(lista[i])-1 and lista[i][j][1] == '0'):
                entradas.append(str(i)+' '+str(j))

            elif i == len(lista)-1 and lista[i][j][2] == '0':
                entradas.append(str(i)+' '+str(j))

            j += 1
        i += 1
        j = 0
    #print(entradas)
    return entradas

#da as direcoes liberadas
def vai_para(dado):
    comando = []
    if dado[0] == '0':
        comando.append('s')
    if dado[1] == '0':
        comando.append('d')
    if dado[2] == '0':
        comando.append('i')
    if dado[3] == '0':
        comando.append('e')
    return comando

#descreve as coordenadas na matriz de acordo com as direcoes
def coordenas_na_matriz(linha,coluna,direcao,lista):
    caminho = list()
    linha_aux = linha
    coluna_aux = coluna
    for i in direcao:
        if i == 's':
            l = linha_aux - 1
            if l>=0:
                caminho.append([l,coluna])
        if i == 'i':
            l = linha_aux + 1
            if l<=len(lista):
                caminho.append([l,coluna])
        if i == 'd':
            c = coluna_aux +1
            if c<= len(lista):
                caminho.append([linha,c])
        if i == 'e':
            c = coluna_aux - 1
            if c >= 0:
                caminho.append([linha,c])
    return caminho

entrada_saida = mostra(testeeee)
entrada = entrada_saida[0]
saida = entrada_saida[1]
target = 0
caminhado = list()
entradax = entrada.split(' ')
Nodo(testeeee[int(entradax[0])][entradax[1]],entrada,False,[])
def caminhando(nodo):
    dado = nodo.dado
    nodo.m = True
    dir = vai_para(dado)
