class Vertice:
    """Classe que representa um vértice de uma Árvore Binária."""

    def __init__(self, dado: str) -> None:
        self.dado = dado
        self.esquerda: Vertice | None = None
        self.direita: Vertice | None = None
        
    def __str__(self) -> str:
        return self.dado

    def representacao_com_parenteses(self) -> str:
        """Retorna a representação da árvore com aninhamento por parênteses."""
        esq = self.esquerda.representacao_com_parenteses() if self.esquerda else ''
        dir = self.direita.representacao_com_parenteses() if self.direita else ''
        return f'({self} {esq} {dir})'

    def representaca_com_recuo(self, numero_de_espacos: int = 0) -> str: 
        """Retorna uma representação da árvore com ruco."""
        espacos = ' ' * numero_de_espacos
        esq = self.esquerda.representaca_com_recuo(numero_de_espacos + 4) if self.esquerda else ''
        dir = self.direita.representaca_com_recuo(numero_de_espacos + 4) if self.direita else ''
        return f'{espacos}{self}\n{esq}{dir}'
    
    def imprimir_percurso_em_ordem(self) -> None:
        """Percorre a árvore em ordem simétrica (esquerda , vértice, direita) e imprime o dado do vértice."""
        if self.esquerda:
            self.esquerda.imprimir_percurso_em_ordem()
        print(self)
        if self.direita:
            self.direita.imprimir_percurso_em_ordem()

    def imprimir_percurso_pre_ordem(self) -> None:
        """Percorre a árvore em pré-ordem (vértice, esquerda, direita) e imprime o dado do vértice."""
        print(self)
        if self.esquerda:
            self.esquerda.imprimir_percurso_pre_ordem()
        if self.direita:
            self.direita.imprimir_percurso_pre_ordem()
        print(self)

    def imprimir_percurso_pos_ordem(self) -> None:
        """Percorre a árvore em pós-ordem (esquerda, direita, vértice) e imprime o dado do vértice."""
        if self.esquerda:
            self.esquerda.imprimir_percurso_pos_ordem()
        if self.direita:
            self.direita.imprimir_percurso_pos_ordem()
        print(self)

#Criação dos vértices
passeio = Vertice("Passeio")
diurno = Vertice("Diurno")
frio = Vertice("Frio")
planetario = Vertice("Planetário")
museu = Vertice("Museu")
calor = Vertice("Calor")
parque = Vertice("Parque")
praia = Vertice("Praia")
noturno = Vertice("Noturno")
restaurante = Vertice("Restaurante")
cinema_noturno = Vertice("Cinema")

#Contrução da árvore
passeio.esquerda = diurno
passeio.direita = noturno

diurno.esquerda = frio
diurno.direita = calor

frio.esquerda = planetario
frio.direita = museu

calor.esquerda = parque
calor.direita = praia

noturno.esquerda = restaurante
noturno.direita = cinema_noturno

#Impressão das representações e percursos
print(passeio.representacao_com_parenteses())
print()
print(passeio.representaca_com_recuo())
print()
print(passeio.imprimir_percurso_em_ordem())
print()
print(passeio.imprimir_percurso_pre_ordem())
print()
print(passeio.imprimir_percurso_pos_ordem())