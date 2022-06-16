from ctypes import pointer
from node import Node

sequencial = []

class LinkedList():
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self,elem):
        if self.head:
            # Inserção quando a lista já possui elementos
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            pointer.next = Node(elem)

        else:
            # Inserção quando a lista está vazia
            self.head = Node(elem)
        self.size += 1

    def __len__(self):
        # Retorna o tamanho da lista
        return self.size

    def __getitem__(self,index):
        # a = lista[6]
        # a = lista.get(6)
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("Index out of range")
        if pointer:
            return pointer.data
        else:
            raise IndexError("Index out of range")


    def __setitem__(self,index,elem):

        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("Index out of range")
        if pointer:
            pointer.data = elem
        else:
            raise IndexError("Index out of range")

    def index(self,elem):
        pointer = self.head
        i = 0
        while pointer:
            if pointer.data == elem:
                return i
            pointer = pointer.next
            i += 1

        raise ValueError(f"{elem} Value not found")

    def insert(self,index,elem):
        if index == 0:
            node = Node(elem)
            node.next = self.head
            self.head = node
        else:
            pointer = self.head
            for i in range(index-1):
                if pointer:
                    pointer = pointer.next
                else:
                    raise IndexError("Index out of range")
            if pointer:
                pointer.next = Node(elem,pointer.next)
            else:
                raise IndexError("Index out of range")
        self.size += 1

    


lista = LinkedList()

lista.append(1) 