from data_structures.linked_list import LinkedList


class TestLinkedList:

    def test_linked_list_construction(self) -> None:
        linked_list = LinkedList()
        assert (linked_list.size == 0)
        assert (linked_list.head is None)

    def test_linked_list_add(self) -> None:
        linked_list = LinkedList()
        linked_list.add(10)
        assert (linked_list.size == 1)
        linked_list.add(20)
        assert (linked_list.size == 2)
        linked_list.add(30)
        assert (linked_list.size == 3)

    def test_linked_list_contains(self) -> None:
        linked_list = LinkedList()
        linked_list.add(10)
        linked_list.add(20)
        linked_list.add(30)
        assert (linked_list.contains(30) is True)
        assert (linked_list.contains(10) is True)
        assert (linked_list.contains(20) is True)
        assert (linked_list.contains(50) is False)
