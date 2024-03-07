from typing import TypeVar, Generic
from node import Node

T = TypeVar("T")
class DobleList(Generic[T]):
    def __init__(self):
        self.__head: Node[T] | None = None
        self.__tail: Node[T] | None = None
        self.__size: int = 0
        self.__current: Node[T] | None = None
    def append(self, data: T):
        new_node = Node(data)
        if self.is_empty():
            self.__head = new_node
            self.__tail = new_node
            self.__tail.next = None
        else:
            pass


    def is_empty(self) -> bool:
        return self.__head is None and self.__tail is None
    def __iter__(self):
        self.__current = self.__head
        return self

    """Mover hacia el siguiente"""
    def __next__(self):
        if self.__current is None:
            raise StopIteration

        data = self.__current.data
        self.__current = self.__current.next
        if self.__current is self.__tail.next:
            self.__current = None
        return data



def __len__(self):
    point = 0
    for _ in self:
        point += 1
    return point