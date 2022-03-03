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

    def test_linked_list_remove(self) -> None:
        # Remove from the head
        linked_list = LinkedList()
        linked_list.add(10)
        linked_list.add(20)
        linked_list.add(30)
        linked_list.add(40)
        linked_list.add(50)
        linked_list.add(60)
        linked_list.add(70)
        assert (linked_list.size == 7)
        linked_list.remove(10)
        assert (linked_list.size == 6)
        assert (linked_list.contains(10) is False)

        # Remove from the middle
        assert (linked_list.size == 6)
        linked_list.remove(40)
        assert (linked_list.size == 5)
        assert (linked_list.contains(40) is False)

        # Remove from the tail
        assert (linked_list.size == 5)
        linked_list.remove(70)
        assert (linked_list.size == 4)
        assert (linked_list.contains(70) is False)

    def test_linked_list_clear(self) -> None:
        # Clear empty list
        linked_list = LinkedList()
        linked_list.clear()
        assert (linked_list.size == 0)

        linked_list.add(10)
        linked_list.clear()
        assert (linked_list.size == 0)

        linked_list.add(10)
        linked_list.add(20)
        linked_list.clear()
        assert (linked_list.size == 0)

        linked_list.add(10)
        linked_list.add(20)
        linked_list.add(30)
        linked_list.add(40)
        linked_list.add(50)
        linked_list.clear()
        assert (linked_list.size == 0)
