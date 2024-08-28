# Importações
from collections import deque

# Definição da classe Grafo
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

    
    def dfs(self, vertice, visitados=None):
        # Inicializa o conjunto de vértices visitados se ainda não foi passado
        if visitados in None:
            visitados = set() # visitados é uma variavel do tipo conjunto

        # Marca o vértice atual como visitado
            visitados.add(vertice)

        #Imprime o vértice atual
        print(vertice, end=' ')

        # Percorre todos os vizinhos do vértice atual
        for vizinho in self.grafo.get(vertice, []):
            # Se o vizinho ainda não foi visitado, chama recursivamente dfs para ele
            if vizinho not in visitados:
                self.dfs(vizinho, visitados)

    def bfs(grafo, inicio):
        """
        Realiza a busca em largura (BFS) a partir do vérice inivial fornecido.

        :param grafo: Dicionário representando o grafo, onde as chaves são vértices e os valores são listas de vizinhos.
        :param inicio: Vértice inicial para iniciar a busca.
        """

        visitado = set() # Conjunto para armazenar os nós já visitados
        fila = deque([inicio]) # Fila para armazenar os nós a serem explorados, começando pelo nó inicial

        while fila: # Enquanto houver elementos na fila
            vertice = fila.popleft() # Remove o elemento mais à esquerda da fila

            if vertice not in visitado: # Se o vértice ainda não foi visitado
                visitado.add(vertice) # Marca o vértice como visitado
                print(vertice, end=' ') # Imprime o vértice visitado

                # Adiciona todos os vizinhos não visitados do vértice atual à fila
                for vizinho in grafo.get(vertice, []):
                    if vizinho not in visitado:
                        fila.append(vizinho)
    


# Exemplo de uso            
g = Grafo()
g.adicionar_vertice('A')
g.adicionar_vertice('B')

# A verificaçao correta
g.adicionar_aresta('A', 'B') # Funciona, pois ambos os vértices estão no grafo

print(list(g.grafo.keys()))