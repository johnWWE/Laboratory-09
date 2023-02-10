'''Eliminar el primer elemento de una lista circular'''
class Node:
    def __init__(self, data, next=None): #nodo none
        self.data = data
        self.next = next   #nodo que

class listaCircular:
    def __init__(self):
        self.head = None

    def agregarNodo(self, data):  #para agregar un nodo nueevo en la lista
        new_node = Node(data)
        if self.head is None:    #si lista está vacía,el nuevo nodo se convierte en el primer nodo y se hace que su next apunte a self.head
            self.head = new_node
            new_node.next = self.head
        else:                       # itera sobre la lista hasta llegar al último nodo
            auxiliar = self.head
            while auxiliar.next != self.head:
                auxiliar = auxiliar.next
            auxiliar.next = new_node
            new_node.next = self.head
#
    def eliminarPrimerNodo(self): # Metodo de la clase  listaCircular
        if self.head is None:    # Comprando si el primero es vacio
            return None
        else:           # si no es vacio se crea un auxiliar que apunte al primero
            auxiliar = self.head
            while auxiliar.next != self.head:  #recorreemos el aauxiliar hasta que ya no cumpla
                auxiliar = auxiliar.next
            auxiliar.next = self.head.next  #ya apuntamos al siguiente nodo
            self.head = self.head.next  # ya se apunta al segundo nodo, por ende eel primero ya se elimina

# creemos una lista circular y agreguemos aalgunos nodos
listaa = listaCircular()
listaa.agregarNodo(1)
listaa.agregarNodo(2)
listaa.agregarNodo(3)
listaa.agregarNodo(4)
# la lista seria 1,2,3,4

# eliminando
listaa.eliminarPrimerNodo()

# Reorremos la lista para verificar el resultado
auxiliar     = listaa.head  # apunta al primer nodo
while auxiliar:   #
    print(auxiliar.data)
    auxiliar = auxiliar.next  # avaanzamos al siguiente nodo
    if auxiliar == listaa.head:
        break    #llegamos al final de la lista, procediendo a detener el ciclo
