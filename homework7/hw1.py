"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.

Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from collections import defaultdict
from itertools import chain
from typing import Any

# Example tree:
example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        }
     },
    "fourth": "RED",
}


class Tree:
    def __init__(self, tree: dict):
        self.root = {'root': tree}
        self.current_node = self.root
        self._marked = defaultdict(bool)
        self._element_cnt = 0

    def _traverse_and_count(self,
                            start_node: Any = None,
                            element: Any = None) -> None:
        """
        Recursively traverses a tree and counts occurrences
        of the element given.
        """
        if start_node is None:
            start_node = list(self.root).pop(0)  # начинаем с корня
        self._marked[str(start_node)] = True
        try:
            successors = self.current_node[start_node]
            self.current_node = successors
        except (KeyError, TypeError):
            successors = []
        if type(successors) in [int, str, bool]:  # не можем по ним итерировать
            successors = [successors]
        for successor in successors:
            if type(successor) == dict:  # словарь, который является листом
                successor = list(chain(*successor.items()))
            if element in successor or element == successor:
                self._element_cnt += 1
            if not self._marked[str(successor)]:
                self._traverse_and_count(successor, element)
            self.current_node = successors

    def find_occurrences(self, element: Any) -> int:
        self._traverse_and_count(element=element)
        cnt, self._element_cnt = self._element_cnt, 0
        return cnt


def find_occurrences(tree: dict, element: Any) -> int:
    """
    Takes an element and finds the number of occurrences
    of this element in the tree, which is a dictionary
    and can contain multiple nested structures.
    :param tree: dict-like structure
    :param element: str, list, tuple, dict, set, int, bool
    :return: int
        number of occurrences
    """
    tree_ = Tree(tree)
    return tree_.find_occurrences(element=element)


if __name__ == '__main__':
    print(find_occurrences(example_tree, "RED"))  # 6
