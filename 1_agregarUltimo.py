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
            auxiliar = self.head
            while auxiliar.next != self.head:   # recorremos para agregar elementos
                auxiliar = auxiliar.next   #nos ayudaremos del auxiliar para recorrer
            auxiliar.next = new_node
            new_node.next = self.head

    def imprimirListaCircular(self):
        auxiliar = self.head        #se s recorre a lista siguiendo las referencias next hasta que
                                    #se llega al primer nodo de nuevo
        while auxiliar:
            print(auxiliar.data)
            auxiliar = auxiliar.next
            if auxiliar == self.head:
                break      # evitando el bucle infinito

listaSupuesta = listaCircularEnlazada()
listaSupuesta.agregarElementos("A")   #instancia de la clase para agregar elementos a la lista
listaSupuesta.agregarElementos("B")
listaSupuesta.agregarElementos("C")
listaSupuesta.imprimirListaCircular()  #imprimir los elementos en orden estabecido
