from typing import List, Tuple

class Grafo:
    def __init__(self, vertices) -> None:
        self.V: int = vertices # Número de vértices no grafo
        self.arestas: List[Tuple[int, int, int]] = [] # Lista para armazenar as arestas

    def adicionar_aresta(self, origem: int, destino: int, peso: int) -> None:
        self.arestas.append((origem, destino, peso))

    def encontrar(self, pai: List[int], i: int) -> int:
        # Função para encontrar o "representante" do conjunto de um vértice
        if pai[i] == i:
            return i
        return self.encontrar(pai, pai[i])
        
    def unir(self, pai: List[int], rank: List[int], x: int, y: int) -> None:
        # Função para unir (combinar) duas subconjuntos
        raiz_x: int = self.encontrar(pai, x)
        raiz_y: int = self.encontrar(pai, y)

        # União por rank para otimização
        if rank[raiz_x] < rank[raiz_y]:
            pai[raiz_x] = raiz_y
        elif rank [raiz_x] > rank[raiz_y]:
            pai[raiz_y] = raiz_x
        else:
            pai[raiz_y] = raiz_x
            rank[raiz_x] += 1

    def kruskal(self) -> List[Tuple[int, int, int]]:
        resultado: List[Tuple[int, int, int]] = [] # Lista para armazenar as arestas da MST
        i, e = 0, 0 # i = índice das arestas ordenadas, e = número de arestas na MST

        # Passo 1: Ordenar as arestas pelo peso
        self.arestas = sorted(self.arestas, key=lambda item: item[2])

        pai: List[int] = []
        rank: List[int] = []

        # Inicializar os subconjuntos (cada vértice é seu próprio subconjunto)
        for vertice in range(self.V):
            pai.append(vertice)
            rank.append(0)

        # Passo 2: Adicionar arestas à MST até que ela tenha V-1 arestas
        while e < self.V -1:
            origem, destino, peso = self.arestas[i]
            i += 1
            x = self.encontrar(pai, origem)
            y = self.encontrar(pai, destino)

            # Se aresta não formar um circulo, adicioná-la à MST
            if x != y:
                e += 1
                resultado.append((origem, destino, peso))
                self.unir(pai, rank, x, y)

            # Retorna a lista de arestas na árvore geradora mínima (MST)
            return resultado

# Exemplo de uso
g = Grafo(4)
g.adicionar_aresta(0, 1, 10)
g.adicionar_aresta(0, 2, 6)
g.adicionar_aresta(0, 3, 5)
g.adicionar_aresta(1, 3, 15)

resultado_mst = g.kruskal()

# Imprime as arestas selecionadas para o MST
print('Arestas na árvore geradora mínima:')
for origem, destino, peso in resultado_mst:
    print(f"{origem} -- {destino} == {peso}")