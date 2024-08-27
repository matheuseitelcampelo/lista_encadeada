class Grafo:
    def __init__(self) -> None:
        self.grafo = {} #Ddicionário para armazenar vértices e suas arestas

    def adicionar_vertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = [] # Lista para armazenar os vizinhos do vertice

    def adicionar_aresta(self, vertice_origem, vertice_destino):
        if vertice_origem in self.grafo and vertice_destino in self.grafo:
            self.grafo[vertice_origem].append(vertice_destino)
        else:
            print(f"O vértice origem e ou vértice destino não existem")


# Exemplo de uso            
g = Grafo()
g.adicionar_vertice('A')
g.adicionar_vertice('B')

# A verificaçao correta
g.adicionar_aresta('A', 'B') # Funciona, pois ambos os vértices estão no grafo

print(list(g.grafo.keys()))