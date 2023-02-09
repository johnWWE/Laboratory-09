"""Eliminar ultimo elemento de una lista circular"""
class Node:         #definiendo un nodo en una lista circular
    def __init__(self, data):
        self.data = data   #valor de cada nodo
        self.next = None   # referencia al siguiente nodo

class listaCircularEnlazada:  # una lista circular completa
    def __init__(self):
        self.head = None   # el atributo head apunta al primer nodo

    def agregarElementos(self, data):   # funcion para agregar elementos  en la ultima posicion
        if not self.head:               #si esta vacia, se crea un nuevo nodo y se sasigna al self.head
            self.head = Node(data)
            self.head.next = self.head
        else:                     #si no esta vacio se crea un nodo con el valor
            new_node = Node(data)
            aux = self.head
            while aux.next != self.head:   # recorremos para agregar elementos
                aux = aux.next   #nos ayudaremos del auxiliar para recorrer
            aux.next = new_node
            new_node.next = self.head

    def eliminarElemento(self, node):
        if self.head == None:   # si es vacio no hace nada
            return
        if self.head.next == self.head:  # si solo hay uno, entonces se asigna
            self.head = None
        else:
            aux = self.head    #usamos un auxiliar para eencontrar el ultimo, recorrieendo
                            # por las referencias hasta el siguiente
            while aux.next != self.head:
                aux1 = aux       # usamos dos auxiliares para no perder la referencia
                aux = aux.next  # su referencia queda en el penultimo nodo
            aux1.next = self.head   #ahora apunta al primer nodo

    def imprimirLista(self):
        aux = self.head
        while aux:
            print(aux.data)
            aux = aux.next
            if aux == self.head:
                break

lista = listaCircularEnlazada()
lista.agregarElementos("A")
lista.agregarElementos("B")
lista.agregarElementos("C")
lista.imprimirLista()    #mostramos los elementos totales actualmente antes de que sea eliminadop
lista.eliminarElemento(lista.head)
print("Lista actualizada =>")
lista.imprimirLista()   # eleementos despues de eliminar el ultimo
