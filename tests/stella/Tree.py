import unittest
from leetcode.stella import Tree
from typing import List


def build_tree(vals: List):
    if not vals:
        return None
    nodes = []
    for val in vals:
        nodes.append(Tree.TreeNode(val=val) if val is not None else None)
    idx = 0
    for node in nodes:
        if idx >= len(nodes):
            break
        if node is not None:
            idx += 1
            if idx < len(nodes):
                node.left = nodes[idx]
            idx += 1
            if idx < len(nodes):
                node.right = nodes[idx]
    return nodes[0]


def flatten_tree(tree: Tree.TreeNode):
    if not tree:
        return []
    nodes = [tree]
    idx = 0
    while idx < len(nodes):
        node = nodes[idx]
        if node is not None:
            if node.right or node.left:
                nodes.extend([node.left, node.right])
        idx += 1
    return [n.val if n else None for n in nodes]


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
