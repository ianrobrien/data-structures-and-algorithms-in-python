from typing import TypeVar, Generic, Optional

T = TypeVar('T')


class Node(Generic[T]):
    next: Optional['Node[T]'] = None
    value: T

    def __init__(self, value: T) -> None:
        self.value = value
        self.next = None


class LinkedList(Generic[T]):
    head: Optional[Node['T']] = None
    size: int = 0

    def add(self, value: T) -> None:
        """
        Add the given value to the list
        :param value: the value to add to the list
        :return:
        """
        if self.head is None:
            self.head = Node(value)
        else:
            next_node = self.head
            while next_node.next is not None:
                next_node = next_node.next
            next_node.next = Node(value)

        self.size += 1

    def contains(self, value: T) -> bool:
        """
        Whether or not the given value is in the list
        :param value: the value to search for
        :return:
        """
        if self.head is None:
            return False
        if self.head.value == value:
            return True

        next_node = self.head
        while next_node.next is not None:
            next_node = next_node.next
            if value == next_node.value:
                return True

        return False
