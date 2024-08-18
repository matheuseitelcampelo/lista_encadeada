class Node:
    def __init__(self, value: str) -> None:
        self.value = value
        self.children = []

    def add_child(self, child_node) -> None:
        self.children.append(child_node)

    def get_children(self) -> list:
        return self.children


root = Node('valor = root')

livre = Node('valor = livre')
dez_anos = Node('valor = dez_anos')
doze_anos = Node('valor = doze anos')

root.add_child(livre)
root.add_child(dez_anos)
root.add_child(doze_anos)