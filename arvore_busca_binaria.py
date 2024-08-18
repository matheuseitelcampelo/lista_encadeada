class No:
    """
    Classe que representa um nó em uma arvore binaria
    """

    def __init__(self, valor: int) -> None:
        self.valor : int = valor
        self.esquerda: No | None = None
        self.direita: No | None = None

def inserir(raiz: No | None, valor: int) -> No:
    """
    Insere um novo nó na árvore binária de busca.

    Args:
        raiz (No | None): A raíz da subárvore onde o valor deve ser inserido.
        valor (int): O valor a ser inserido.

    Returns: 
        No: A raiz da subárvore após a inserção.
    """

    if raiz is None:
        return No(valor)
    else:
        if valor < raiz.valor:
            raiz.esqueda = inserir(raiz.esquerda, valor)
        else:
            raiz.direita = inserir(raiz.direita, valor)
    return raiz

#Criação da árvore e inserção de elementos
raiz = No(14) #Raiz árvore com o primeiro valor

sequencia = [4, 18, 0, 21, 17, 1, 8, 13]
for valor in sequencia:
    inserir(raiz, valor)