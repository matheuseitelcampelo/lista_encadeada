class ItemLista:

    def __init__(self, data = 0, nextItem = None):
        self.data = data
        self.next = nextItem

    def __repr__(self):
        
        return '%s => %s' % (self.data, self.next)
    

class ListaEncadeada:
    def __init__(self):
        self.head = None

    def __repr__(self):
        
        return "%s" % (self.head)
    
    def insere(self, data):

        #cria um objeto para armazenar um novo item da lista

        item = ItemLista(data)

        #apos o objeto ItemLista ser criado, ele recebe em seu
        #atributo next o atual valor em head da ListaEncadeada

        item.next = self.head
    
        #ListaEncadeada atualiza o valor de head, apontando
        #para o ultimo objeto ItemLista criado

        self.head = item

    def remove(self, data):
        
        """
        Remove o primeiro item da lista com o valor especificado
        """

        #Verifica se o item a ser removido é o head (primeiro item da lsita)

        if self.head and self.head.data == data:
            
            #Se o head contem o valor que procuramos, basta
            #apontar o head para o proximo item
            
            self.head = self.head.next
            print("Elemento econtrado")
        
        else:
            
            #Caso contrário, precisamos encontrar o item na lista
            
            before = None #'before' vai guardar o item anterior ao que estamos analisando
            current = self.head #Começamos a navegação a partir do head

            #navegue pela lista para encontrar o item com o valor especificado
            while current and current.data != data:
                before = current #before guarda o item atual
                current = current.next #current avança para o proximo item

            #verifica se encontramos o item
            if current:
                #'before.next' agora pula o item que queremos remover
                before.next = current.next
                print("Elemento encontrado")

            else:
                print("Elemento não encontrado")