from typing import Optional

class Vertice:
    """
    Classe que representa um vértice em uma árvore N-ária.
    """
    def __init__(self, dado: str):
        self.dado: str = dado
        self.filhos: Optional[Filhos] = None

    def __str__(self) -> str:
        return self.dado

    def representacao_com_parenteses(self) -> str:
        filhos_repr = self.filhos.representacao_com_parenteses() if self.filhos else ''
        return f'({self} {filhos_repr})'

    def representacao_com_recuo(self, numero_de_espacos: int = 0) -> str:
        filhos_repr = self.filhos.representacao_com_recuo(numero_de_espacos + 2) if self.filhos else ''
        espacos = ' ' * numero_de_espacos
        return f'{espacos}{self}\n{filhos_repr}'

    def inserir_filho(self, dado: str) -> 'Vertice':
        if self.filhos is None:
            self.filhos = Filhos()
        return self.filhos.inserir(dado)

    def imprimir_percurso_pre_ordem(self) -> None:
        print(self)
        if self.filhos:
            self.filhos.imprimir_percurso_pre_ordem()

    def imprimir_percurso_pos_ordem(self) -> None:
        if self.filhos:
            self.filhos.imprimir_percurso_pos_ordem()
        print(self)

class Filhos:
    """
    Classe que representa a coleção de filhos de um vértice.
    """
    def __init__(self):
        self._vertices: list[Vertice] = []

    def representacao_com_parenteses(self) -> str:
        return ' '.join(vertice.representacao_com_parenteses() for vertice in self._vertices)

    def representacao_com_recuo(self, numero_de_espacos: int = 0) -> str:
        return '\n'.join(vertice.representacao_com_recuo(numero_de_espacos) for vertice in self._vertices)

    def inserir(self, dado: str) -> Vertice:
        novo_vertice = Vertice(dado)
        self._vertices.append(novo_vertice)
        return novo_vertice

    def imprimir_percurso_pre_ordem(self) -> None:
        for vertice in self._vertices:
            vertice.imprimir_percurso_pre_ordem()

    def imprimir_percurso_pos_ordem(self) -> None:
        for vertice in self._vertices:
            vertice.imprimir_percurso_pos_ordem()

# Criando a árvore de pacotes turísticos
raiz = Vertice("Pacotes Turísticos")

tranquilidade = raiz.inserir_filho("Tranquilidade")
aventura = raiz.inserir_filho("Aventura")
luxo = raiz.inserir_filho("Luxo")

rafting = aventura.inserir_filho("Rafting")
escalada = aventura.inserir_filho("Escalada")
tirolesa = aventura.inserir_filho("Tirolesa")

# Exibindo representações da árvore
print("\nRepresentação com Recuo:\n")
print(raiz.representacao_com_recuo())

print("\nRepresentação com Parênteses:\n")
print(raiz.representacao_com_parenteses())

# Percorrendo a árvore em pré-ordem
print("\nPercurso em Pré-Ordem:\n")
raiz.imprimir_percurso_pre_ordem()

# Percorrendo a árvore em pós-ordem
print("\nPercurso em Pós-Ordem:\n")
raiz.imprimir_percurso_pos_ordem()

# Percorrendo a subárvore "Aventura" em pré-ordem
print("\nSubárvore 'Aventura' em Pré-Ordem:\n")
aventura.imprimir_percurso_pre_ordem()

# Percorrendo a subárvore "Aventura" em pós-ordem
print("\nSubárvore 'Aventura' em Pós-Ordem:\n")
aventura.imprimir_percurso_pos_ordem()
