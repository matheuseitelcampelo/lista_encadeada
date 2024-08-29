"""
Sua tarefa era desenvolver um algoritmo em Python que
identifique os influenciadores com base nas interações entre os usuários na rede. 

Entrada: Um grafo representando a rede social, onde os nós são os usuários e as
 arestas representam conexões ou interações entre eles. 

Saída: Uma lista dos usuários identificados como influenciadores na rede. 
Algoritmo para identificação de influenciadores:
"""

from typing import List, Dict

class Grafo:
    def __init__(self) -> None:
        # Dicionário que mapeia um vértice (string) para uma lista de vértices adjacentes
        self.adjacencias: Dict[str, List[str]] = {}

    def adicionar_vertice(self, vertice: str) -> None:
        """
        Adiciona um vértice ao grafo, se ele ainda não existir

        vertice: Nome do vértice como string.
        """
        if vertice not in self.adjacencias:
            self.adjacencias[vertice] = []

    def adicionar_aresta(self, origem: str, destino: str) -> None:
        """
        Adiciona uma aresta ao grafo, criando os vértices se necessário.

        origem: Vértice de origem como stirng.
        destino: Vértice de destino como string.
        """
        self.adicionar_vertice(origem)
        self.adicionar_vertice(destino)
        self.adjacencias[origem].append(destino)

    def grau_entrada(self, vertice: str) -> int:
        """
        Calcula o grau de entrada de um vértice, ou seja, o número de arestas que apontam para ele.

        vertice: Nome do vértice como string.
        Retorno: Grau da entrada como inteiro
        """
        return sum(1 for vizinhos in self.adjacencias.values() if vertice in vizinhos)

    def identificar_influenciadores(self) -> List[str]:
        """
        Identifica os influenciadores na rede, ou seja, aqueles que tem o maior grau de entrada
        em comparação com seus vizinhos.

        Retorno: Lista de influenciadores como lista de strings.
        """
        influenciadores = []
        for usuario in self.adjacencias:
            grau_entrada_usuario = self.grau_entrada(usuario)
            if all(grau_entrada_usuario > self.grau_entrada(vizinho) for vizinho in self.adjacencias[usuario]):
                influenciadores.append(usuario)
                return influenciadores
    
# Exemplo de uso do algoritmo
if __name__ == "__main__":
    rede_social = Grafo()

    rede_social.adicionar_aresta('Alice', 'Bob')
    rede_social.adicionar_aresta('Alice', 'Carol')
    rede_social.adicionar_aresta('Bob', 'Alice')
    rede_social.adicionar_aresta('Bob', 'Dave')
    rede_social.adicionar_aresta('Carol', 'Alice')
    rede_social.adicionar_aresta('Carol', 'Dave')
    rede_social.adicionar_aresta('Dave', 'Bob')
    rede_social.adicionar_aresta('Dave', 'Carol')
    rede_social.adicionar_aresta('Dave', 'Eve')
    rede_social.adicionar_aresta('Eve', 'Dave')

    influenciadores = rede_social.identificar_influenciadores()
    print(f"Influenciadores identificados: {influenciadores}")