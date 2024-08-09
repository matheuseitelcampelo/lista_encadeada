import ListaEncadeada as le

#Cria o objeto

listaDeCompras = le.ListaEncadeada()

#exemplo de uso

listaDeCompras.insere("shampoo")
listaDeCompras.insere("biscoito")
listaDeCompras.insere("detergente")
listaDeCompras.insere("abobrinha")
listaDeCompras.insere("banana")

print("Conteudo da lista:", listaDeCompras)

listaDeCompras.remove("tesoura")

print("Conteudo da lista:", listaDeCompras)