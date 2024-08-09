class RegistraLivro:
    def __init__(self, titulo, proximo = None) -> None:
        self.titulo = titulo
        self.proximo = proximo

    def __str__(self) -> str:
        return '{} => {}'.format(self.titulo, self.proximo)

class CriaPilhaDeLivros:
    def __init__(self) -> None:
        self.head = None

    def __str__(self) -> str:
        return '{}'.format(self.head)
        
    def addLivro(self, titulo) -> RegistraLivro:
        livro = RegistraLivro(titulo)
        livro.proximo = self.head
        self.head = livro

    def popLivro(self) -> None:
        if self.head.proximo:
            self.head = self.head.proximo
            print("livro no topo da pilha removido")
        else:
            print("Fim da pilha de livros")

pilha = CriaPilhaDeLivros()

pilha.addLivro("livro 1")
pilha.addLivro("livro 2")
pilha.addLivro("livro 3")
pilha.addLivro("livro 4")

print(pilha)


pilha.popLivro()
pilha.popLivro()
pilha.popLivro()
pilha.popLivro()
pilha.popLivro()

print(pilha)


