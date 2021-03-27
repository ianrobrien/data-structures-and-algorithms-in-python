from typing import TypeVar, Generic, Optional

T = TypeVar('T')


class TreeNode(Generic[T]):
    left: Optional['TreeNode[T]'] = None
    right: Optional['TreeNode[T]'] = None
    value: Optional[T] = None

    def __init__(self, value: T):
        """
        Create a TreeNode with the given value
        :param value: the value of the TreeNode
        """
        self.value = value


class BinarySearchTree(Generic[T]):
    root: Optional[TreeNode[T]] = None
    value: T = None
    size: int = 0

    def add(self, value) -> None:
        """
        Add the given value to the tree
        :param value: the value to add to the tree
        :return:
        """
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self.__add__(value, self.root)

        self.size += 1

    def __add__(self, value: T, tree_node: TreeNode[T]) -> None:
        if value > tree_node.value:
            if tree_node.right is None:
                tree_node.right = TreeNode(value)
            else:
                self.__add__(value, tree_node.right)
        else:
            if tree_node.left is None:
                tree_node.left = TreeNode(value)
            else:
                self.__add__(value, tree_node.left)

    def contains(self, value: T) -> bool:
        """
        Whether or not the given value is contained in the tree
        :param value: the value to search for
        :return:
        """
        if self.root is None:
            return False
        if self.root.value == value:
            return True

        return self.__contains__(value, self.root)

    def __contains__(self, value: T, tree_node: TreeNode[T]) -> bool:
        if value > tree_node.value:
            if tree_node.right is None:
                return False
            if tree_node.right.value == value:
                return True
            return self.__contains__(value, tree_node.right)
        else:
            if tree_node.left is None:
                return False
            if tree_node.left.value == value:
                return True
            return self.__contains__(value, tree_node.left)
