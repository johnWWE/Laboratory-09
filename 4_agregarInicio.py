'''agregar elemento al inicio de unaa lista circular'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class listaCircularEnlaazada:
    def __init__(self):
        self.head = None

    def agregar(self, data):
        new_node = Node(data)
        if self.head is None:    # si esta vacia, la cabeza es el nuevo nodo
            self.head = new_node
            new_node.next = self.head      # se apunta  al mismo
        else:
            aux = self.head
            while aux.next != self.head:
                aux = aux.next
            aux.next = new_node
            new_node.next = self.head

      #agregar nuevo elemento al inicio de la
      #lista y reemplazamos elemento actual de la cabeza
    def reemplazo(self, data):
        new_node = Node(data)
        aux = self.head   #aasignamos la cabeza a un auxiliaar
        new_node.next = self.head
#Si la lista no está vacía, recorremos hasta llegar al  último nodo y establecemos
#  el siguiente elemento del último nodo como  nuestro nuevo nodo.
        if not self.head:
            new_node.next = new_node
        else:
            while aux.next != self.head:
                aux = aux.next
            aux.next = new_node
        self.head = new_node

    def imprimir(self):
        aux = self.head
        while aux:
            print(aux.data)
            aux = aux.next
            if aux == self.head:
                break

cllist = listaCircularEnlaazada()
cllist.reemplazo(1)
cllist.reemplazo(2)
cllist.reemplazo(3)
cllist.imprimir()
# 3 2 1, por que se esta agregando al inicio