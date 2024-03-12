from typing import TypeVar, Generic
from node import Node

T = TypeVar("T")
class DobleList(Generic[T]):
    def __init__(self):
        self.__head: Node[T] | None = None
        self.__tail: Node[T] | None = None
        self.__size: int = 0 #Tamaño de la lista
        self.__current: Node[T] | None = None

    def is_empty(self) -> bool:
        return self.__head is None and self.__tail is None

    def append(self, data: T):
        new_node = Node(data)
        if self.is_empty():
            self.__head = new_node
            self.__tail = new_node
        else:
            current = self.__tail
            self.__tail = new_node
            current.next = new_node
            self.__tail.prev = current
        self.__size += 1

    def prepend(self, data: T):
        new_node = Node(data)
        if self.is_empty():
            self.__head = new_node
            self.__tail = new_node
        else:
            new_node.next = self.__head
            self.__head.prev = None
            self.__head = new_node
        self.__size += 1

    def travel(self):
        current = self.__head
        while current != None:
            print(current.data)
            current = current.next

    def travel_end(self):
        current = self.__head
        while current:
            print(current.data)
            current = current.prev

    def size(self):
        print(self.__size)

    def eliminar_inicio(self):
        if self.is_empty():
            print("Lista vacía")
        elif self.__head.next == None:
            self.__head = self.__tail = None
            self.__size = 0
        else:
            self.__head = self.__head.next
            self.__head.prev = None
            self.__size -= 1

    def eliminar_final(self):
        if self.is_empty():
            print("La lista está vacía")
        elif self.__head.next == None:
            self.__head = self.__tail = None
            self.__size = 0
        else:
            self.__tail = self.__tail.prev
            self.__tail.next = None
            self.__size -= 1



