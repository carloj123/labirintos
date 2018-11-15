from Graph import Graph
from Vertex import Vertex
import math
import datetime
import sys

# o sys acessa o sistema do computador. E com o metodo que eu estou usando de sys, consigo aumentar o tamanho da pilha de recursoes, pois o python estava
#limitando as recursoes do programa
sys.setrecursionlimit(1500)

lista = list()
def main():
    arquivos = ['25','50','75','100','150','200','250','300','400','500']
    numero_arqivo = input('Favor digite o numero do arquivo ')
    if numero_arqivo not in arquivos:
        print('Favor, digite um arquivo da lista\n')
        print(arquivos)
        exit()
    metragem = ''
    dicionario_hexa = dict()
    foras = list()
    j = 0

    for i in range(1000000):
        dicionario_hexa[hex(j).replace('0x',"").upper()]=j
        j+=1

    with open('./dados/caso'+numero_arqivo+'a.txt','r') as tal:
        entradas = tal.readlines()
    #com isso eu faco a matriz
    for i in entradas:
        i = i.split(' ')

        if len(i)<= 2:
            metragem = i
        else:
            lista_aux = list()
            for k in i:
                #print(str(len(i))+'lista - '+str(len(lista_aux))+'lista_aux')
                if k !='\n':
                    lista.append(bin(dicionario_hexa.get(k.replace('\n',"").upper())).replace("0b","").zfill(4))

    metragem[1] = metragem[1].replace('\n',"")
    fr= open("teste.svg","w+")
    fr.write("<?xml version=\"1.0\" standalone=\"no\"?>\n")
    fr.write("\t<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"%scm\" height=\"%scm\" viewBox=\"-0.1 -0.1 %s.2 %s.2\">\n" % (metragem[0], metragem[1], metragem[0], metragem[1]))
    fr.write("\t\t<g style=\"stroke-width:.1; stroke:black; stroke-linejoin:miter; stroke-linecap:butt;\">\n")

    def escreveLinha(x1,y1,x2,y2):
        fr.write("\t\t\t<polyline points=\"%d,%d %d,%d\" />\n" % (x1,y1,x2,y2))

    def escreveCirculo(x, y,arquivo):
        fr.write("\t\t\t<circle cx=\"%.1f\" cy=\"%.1f\" r=\"0.2\" stroke=\"red\" fill=\"red\" />\n" % (x+0.5,y+0.5))

    l = 0
    c = 0
    #lista = ['1001','1010','1010','0110',"0101",'1001','1010','1100','0101','0101','1101','0111','0011','0010','0010','1100']

    for i in range(0,len(lista)):
        palavra = lista[i]
        
        if palavra[0] == '1':
            escreveLinha(c, l, c+1, l)
        if palavra[1] == '1':
            escreveLinha(c+1, l, c+1, l+1)
        if palavra[2] == '1':
            escreveLinha(c, l+1, c+1, l+1)
        if palavra[3] == '1':
            escreveLinha(c, l, c, l+1)

        

        c += 1
        if c == int(metragem[1]):
            c = 0
            l += 1

    def arestas(tamanho_linha,inicio,fim):
        global lista,foras,arestar_time

        tamanho_linha = tamanho_linha
        saidas = list()
        saida = ''
        i = 0
        while i < len(lista):
            if i == inicio:
                saidas.append(str(i)+','+'noneA')
                i += 1
                if i>= len(lista):
                    print('Arestas feitas')
                    return saidas

            if i == fim:
                saidas.append(str(i)+','+'noneB')
                i += 1
                if i>= len(lista):
                    print('Arestas feitas')
                    return saidas

            if lista[i][0] == '0':
                ind = i
                saida = str(ind)+','+str(ind-tamanho_linha)
                saidas.append(saida)


            if lista[i][1] == '0':
                ind = i
                saida = str(ind)+','+str(ind+1)
                saidas.append(saida)

            if lista[i][2] == '0':
                ind = i
                saida = str(ind)+','+str(ind+tamanho_linha)
                saidas.append(saida)   
            if lista[i][3] == '0':
                ind = i
                saida = str(ind)+','+str(ind-1)
                saidas.append(saida) 
            i += 1

        print('Arestas feitas')
        return saidas


    def mostra(lista,tamanho_linha):
        entradas= set()
        i = 0

        while i < tamanho_linha:
            try:
                k = lista[i]
            except:
                print(lista)
                print(i)
                exit()
            if i>= 0 and i<tamanho_linha:
                if i == 0:
                    if k[0] == '0' or k[3] == '0':
                        entradas.add(i)

                elif i == tamanho_linha-1:
                    if k[0] == '0' or k[1] == '0':
                        entradas.add(i)

                elif k[0] == '0':
                    entradas.add(i)
            i += 1
        while i < len(lista):
            k = lista[i]

            if i > (math.pow(tamanho_linha,2) - tamanho_linha) and i < math.pow(tamanho_linha,2):
                if i == (math.pow(tamanho_linha,2)-1) - tamanho_linha:
                    if k[2] == '0' or k[3] == '0':
                        entradas.add(i)

                elif i == math.pow(tamanho_linha,2)-1:
                    if k[2] == '0' or k[1] == '0':
                        entradas.add(i)

                elif k[2] == '0':
                    entradas.add(i)
            i += 1

        if len(entradas) <= 1:
            j = tamanho_linha-1
            while j < math.pow(tamanho_linha,2):
                if lista[j][1] == '0':
                    entradas.add(j)

                j += tamanho_linha

        if len(entradas) <= 1:
            j = 0
            while j < math.pow(tamanho_linha, 2):
                if lista[j][3] == '0':
                    entradas.add(j)
                j += tamanho_linha



        print(entradas)
        return entradas



    ##############################


    print('Momento de iniciacao do programa: '+str(datetime.datetime.now().microsecond))
    tam_linha = int(numero_arqivo)
    entrada_saida = mostra(lista,tam_linha)
    inicio = entrada_saida.pop()
    fim = entrada_saida.pop()

    g = Graph()
    #a = Vertex('3')
    auxA = Vertex('noneA')
    auxB = Vertex('noneB')
    #g.add_vertex(a)
    g.add_vertex(auxA)
    g.add_vertex(auxB)

    # g.add_vertex(Vertex('B'))
    #ord() pega um inteiro que representa o unicode que pega o conteudo
    for i in range(0,len(lista)):
        g.add_vertex(Vertex(str(i)))
    print('vertices no grafo')

    edges = arestas(tam_linha,inicio,fim)
    for edge in edges:
        edge_aux = edge.split(',')
        g.add_edge(edge_aux[0],edge_aux[1])
    print('Arestas no grafo')

    g.dfs(auxA,auxB)


    # for j in g.vertices.keys():
    #     if
    #g.print_graph()
    print('#########################')

    print(g.fila)
    g.fila.remove('noneB')
    print('\n\nApos a remocao do noneB: ',g.fila)
    print('Tamanho do caminho',len(g.fila))
    #g.print_graph_dfs_way()
    #print(edges)

    l = 0
    c = 0
    cg = 0
    lg = 0

    for i in range(0,len(lista)):
        palavra = lista[i]
        
        if palavra[0] == '1':
            escreveLinha(c, l, c+1, l)
        if palavra[1] == '1':
            escreveLinha(c+1, l, c+1, l+1)
        if palavra[2] == '1':
            escreveLinha(c, l+1, c+1, l+1)
        if palavra[3] == '1':
            escreveLinha(c, l, c, l+1)

        c += 1
        if c == int(metragem[1]):
            c = 0
            l += 1

    novaFila = map(int, g.fila)
    maxi = max(novaFila)
    for i in novaFila:
        print(i)

    print('\n######################################################')
    for i in range(0, maxi+1):
        if cg == int(metragem[1]):
            cg = 0
            lg += 1
        j = str(i)
        if j in g.fila:
            escreveCirculo(cg, lg,fr)

        cg += 1
        i += 1
            
        

    fr.write("</g>")
    fr.write("</svg>")
    fr.close()
    print('Momento em que o programa parou: '+str(datetime.datetime.now().microsecond))
    print('Tamanho do caminho '+str(len(g.fila)))

if __name__ == "__main__":
    main()