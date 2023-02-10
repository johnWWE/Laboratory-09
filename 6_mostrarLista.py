''' mostrar lsita'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class listaCircular:
    def __init__(self):
        self.head = None

    def agregar(self, data):
        nodoNuevo = Node(data)
        if self.head is None:        #si lista está vacía,el nuevo nodo se convierte en el primer nodo y se hace que su next apunte a self.head
            self.head = nodoNuevo
            nodoNuevo.next = self.head
        else:                # itera sobre la lista hasta llegar al último nodo
            nodoActual = self.head
            while nodoActual.next != self.head:
                nodoActual = nodoActual.next
            nodoActual.next = nodoNuevo
            nodoNuevo.next = self.head

    def mostrarLista(self):
        nodoActual = self.head   # punteero en el primer nodo
        if self.head is not None:  # si no esta vacio lo iteramos
            while True:
                print(nodoActual.data)   # mostramso el dato de cada nodo hasta que ya apunte al primer nodo
                nodoActual = nodoActual.next
                if nodoActual == self.head:
                    break

# Crear una lista circular
listaa = listaCircular()
listaa.agregar(10)
listaa.agregar(20)
listaa.agregar(30)
listaa.agregar(40)

# Mostrar la lista circular
print("Mostrando la lista circular =>")
listaa.mostrarLista()
