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

    def add(self, item: T) -> None:
        """
        Add the given value to the list
        :param item: the value to add to the list
        :return:
        """
        if self.head is None:
            self.head = Node(item)
        else:
            next_node = self.head
            while next_node.next is not None:
                next_node = next_node.next
            next_node.next = Node(item)

        self.size += 1

    def contains(self, item: T) -> bool:
        """
        Whether or not the given value is in the list
        :param item: the value to search for
        :return:
        """
        if self.head is None:
            return False
        if self.head.value == item:
            return True

        next_node = self.head
        while next_node.next is not None:
            next_node = next_node.next
            if item == next_node.value:
                return True

        return False

    def remove(self, item: T) -> None:
        if self.head is None:
            return

        if self.head.value == item:
            self.head = self.head.next
            self.size -= 1
            return
        else:
            head = self.head
            while head.next is not None:
                if head.next.value == item:
                    head.next = head.next.next
                    self.size -= 1
                    return
                head = head.next

    def clear(self) -> None:
        if self.head is None:
            self.size = 0
            return

        self.__clear__(self.head)
        self.head = None

    def __clear__(self, node: Node['T']) -> None:
        if node.next is not None:
            self.__clear__(node.next)

        node.next = None
        self.size -= 1

    def empty(self) -> bool:
        return self.size == 0
