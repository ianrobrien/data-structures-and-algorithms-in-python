from typing import TypeVar, Generic, Optional

T = TypeVar('T')


class TreeNode(Generic[T]):
    left: Optional['TreeNode[T]'] = None
    right: Optional['TreeNode[T]'] = None
    value: Optional[T] = None

    def __init__(self, item: T):
        """
        Create a TreeNode with the given value
        :param item: the value of the TreeNode
        """
        self.value = item


class BinarySearchTree(Generic[T]):
    root: Optional[TreeNode[T]] = None
    value: T = None
    size: int = 0

    def add(self, item) -> None:
        """
        Add the given value to the tree
        :param item: the value to add to the tree
        :return:
        """
        if self.root is None:
            self.root = TreeNode(item)
        else:
            self.__add__(item, self.root)

        self.size += 1

    def __add__(self, value: T, root: TreeNode[T]) -> None:
        if value > root.value:
            if root.right is None:
                root.right = TreeNode(value)
            else:
                self.__add__(value, root.right)
        else:
            if root.left is None:
                root.left = TreeNode(value)
            else:
                self.__add__(value, root.left)

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

    def __contains__(self, value: T, root: TreeNode[T]) -> bool:
        if value > root.value:
            if root.right is None:
                return False
            if root.right.value == value:
                return True
            return self.__contains__(value, root.right)
        else:
            if root.left is None:
                return False
            if root.left.value == value:
                return True
            return self.__contains__(value, root.left)
