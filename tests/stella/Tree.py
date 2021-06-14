import unittest
from leetcode.stella import Tree
from typing import List


def build_tree(vals: List): ...


def flatten_tree(tree: Tree.TreeNode): ...


class TreeTestCase(unittest.TestCase):

    def test_build_and_flatten_tree(self):
        data = [1, 2, 3, 2, None, 2, 4]
        tree = build_tree(data)
        self.assertEqual(data, flatten_tree(tree))

    def test_delete_leaves_with_a_given_value(self):
        root, target, expect = [1, 2, 3, 2, None, 2, 4], 2, [1, None, 3, None, 4]
        self.assertEqual(expect, flatten_tree(Tree.delete_leaves_with_a_given_value(build_tree(root), target)))
        root, target, expect = [1, 3, 3, 3, 2], 3, [1, 3, None, None, 2]
        self.assertEqual(expect, flatten_tree(Tree.delete_leaves_with_a_given_value(build_tree(root), target)))
        root, target, expect = [1, 2, None, 2, None, 2], 2, [1]
        self.assertEqual(expect, flatten_tree(Tree.delete_leaves_with_a_given_value(build_tree(root), target)))
        root, target, expect = [1, 1, 1], 1, []
        self.assertEqual(expect, flatten_tree(Tree.delete_leaves_with_a_given_value(build_tree(root), target)))
        root, target, expect = [1, 2, 3], 1, [1, 2, 3]
        self.assertEqual(expect, flatten_tree(Tree.delete_leaves_with_a_given_value(build_tree(root), target)))
