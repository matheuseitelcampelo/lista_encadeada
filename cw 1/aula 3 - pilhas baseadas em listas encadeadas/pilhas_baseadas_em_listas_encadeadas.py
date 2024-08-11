class Item:    
    def __init__(self, valor=None, anterior=None) -> None:
        self.valor = valor
        self.anterior = anterior

    def __repr__(self) -> str:
        return '{}\n{}'.format(self.valor, self.anterior)

class Pilha:
    def __init__(self) -> None:
        self.topo = None

    def __repr__(self) -> str:
        return '\nTOPO\n{}\nRodapé'.format(self.topo)

    def push(self, valor) -> None:
        #instacia novo item
        item_novo = Item(valor)

        #Item.anterior recebe o atual Pilha.topo
        item_novo.anterior = self.topo

        #Pilha.topo é atualizado com o Item recem criado
        self.topo = item_novo

    def pop(self) -> Item:
        #verifica se a pilha não está vazia
        if not self.topo:
            raise IndexError('Erro, pilha vazia.')
        
        #Atualiza o topo da pilha
        self.topo = self.topo.anterior

def main():
    #Criar um novo objeto do tipo Pilha
    pilha = Pilha()

    #Insere alguns valores na pilha
    for valor in ['a', 'b', 'c', 'd']:
        pilha.push(valor)
    
    #Exibe o conteúdo da pilha
    print(pilha)

    #Removendo os dois ultimos itens
    pilha.pop()
    pilha.pop()
    print(pilha)


if __name__ == "__main__":
    main()