from Vertex import Vertex
color_finish = 'blue'
class Graph:
    vertices = {}
    time = 0
    dictio= dict()
    fila = list()

    def add_vertex(self,vert):
        if isinstance(vert,Vertex) and vert.name not in self.vertices:
            self.vertices[vert.name] = vert
            return True
        else:
            return False

    print('olhar o add_edge')
    def add_edge(self,u,v):
        if u in self.vertices and v in self.vertices:
            #confere se a chave esta nos vertices e se possui um valor associado nela
            #for key, value in self.vertices.items():
            try:
                self.vertices.get(u).add_neighbor(v)
            except:
                print('ERRO')
                exit()
                pass
            try:
                self.vertices.get(v).add_neighbor(u)
            except:
                print('ERRO')
                exit()
                pass

            return True
        else:
            return False

    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighbors))

    def print_graph_dfs_way(self):
        for key in sorted(list(self.vertices.keys())):
            if self.vertices[key].color == 'red':
                print(key + str(self.vertices[key].color))


    def _dfs(self, vertex,vertex_saida):
        global time, color_finish


        vertex.color = 'red'
        #Graph.fila.append(vertex.name)
        vertex.discovery =0
        flag = False
        for v in vertex.neighbors:
            if self.vertices[v].color == 'black':
              if self._dfs(self.vertices[v],vertex_saida):
                    flag = True
                    Graph.dictio[vertex.name] = self.vertices[v].name
                    
                    return True

            vertex.color = color_finish
            vertex.finish = time
            time += 1
            if vertex.name == vertex_saida.name:
                Graph.dictio[vertex.name] = self.vertices[v].name
                return True

    def dfs(self, vertex,vertex_saida):
        global time
        time = 1
        self._dfs(vertex,vertex_saida)
        for i in Graph.dictio.values():
            Graph.fila.append(str(i))
