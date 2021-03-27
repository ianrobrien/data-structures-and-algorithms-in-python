from data_structures.binary_search_tree import BinarySearchTree


class TestBinarySearchTree:

    def test_construction(self):
        binary_search_tree = BinarySearchTree()

        assert (binary_search_tree.size == 0)
        assert (binary_search_tree.root is None)

    def test_add(self):
        binary_search_tree = BinarySearchTree()
        binary_search_tree.add(50)
        binary_search_tree.add(100)
        binary_search_tree.add(0)
        binary_search_tree.add(75)
        binary_search_tree.add(25)
        binary_search_tree.add(88)
        binary_search_tree.add(33)
        binary_search_tree.add(66)
        binary_search_tree.add(11)

        assert (binary_search_tree.size == 9)

    def test_contains(self):
        binary_search_tree = BinarySearchTree()
        binary_search_tree.add(50)
        binary_search_tree.add(100)
        binary_search_tree.add(0)
        binary_search_tree.add(75)
        binary_search_tree.add(25)
        binary_search_tree.add(88)
        binary_search_tree.add(33)
        binary_search_tree.add(66)
        binary_search_tree.add(11)

        assert (binary_search_tree.contains(50) is True)
        assert (binary_search_tree.contains(100) is True)
        assert (binary_search_tree.contains(0) is True)
        assert (binary_search_tree.contains(75) is True)
        assert (binary_search_tree.contains(25) is True)
        assert (binary_search_tree.contains(88) is True)
        assert (binary_search_tree.contains(33) is True)
        assert (binary_search_tree.contains(66) is True)
        assert (binary_search_tree.contains(11) is True)

        assert (binary_search_tree.contains(99) is False)
