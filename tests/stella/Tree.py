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

    def test_maximum_depth_of_binary_tree(self):
        self.assertEqual(3, Tree.maximum_depth_of_binary_tree(build_tree([3, 9, 20, None, None, 15, 7])))

    def test_convert_sorted_array_to_bst(self):
        sa2bst = Tree.convert_sorted_array_to_binary_search_tree
        actual = flatten_tree(sa2bst([-10, -3, 0, 5, 9]))
        self.assertEqual([i for i in [0, -3, 9, -10, None, 5] if i is not None], [i for i in actual if i is not None])

    def test_binary_tree_right_side_view(self):
        self.assertEqual([1, 3, 4], Tree.binary_tree_right_side_view(build_tree([1, 2, 3, None, 5, None, 4])))
        self.assertEqual([1, 3, 4], Tree.binary_tree_right_side_view(build_tree([1, 2, 3, 4])))

    def test_subtree_of_another_tree(self):
        self.assertEqual(False, Tree.subtree_of_another_tree(build_tree([3, 4, 5, 1, 2]), build_tree([4, 1, 2, 0])))
        self.assertEqual(True, Tree.subtree_of_another_tree(build_tree([3, 4, 5, 1, 2]), build_tree([4, 1, 2])))
        self.assertEqual(False, Tree.subtree_of_another_tree(build_tree([1]), build_tree([0])))
        self.assertEqual(True, Tree.subtree_of_another_tree(build_tree([1, 1]), build_tree([1])))

    def test_lowest_common_ancestor_of_binary_tree(self):
        lowest_ancestor = Tree.lowest_common_ancestor_of_binary_tree
        actual = lowest_ancestor(build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]), Tree.TreeNode(val=5),
                                 Tree.TreeNode(val=4))
        self.assertEqual(5, actual.val)
        actual = lowest_ancestor(build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]), Tree.TreeNode(val=5),
                                 Tree.TreeNode(val=1))
        self.assertEqual(3, actual.val)
        actual = lowest_ancestor(build_tree([1, 2]), Tree.TreeNode(val=1), Tree.TreeNode(val=2))
        self.assertEqual(1, actual.val)

    def test_binary_tree_level_order_traversal(self):
        level_order = Tree.binary_tree_level_order_traversal
        self.assertEqual([[3], [9, 20], [15, 7]], level_order(build_tree([3, 9, 20, None, None, 15, 7])))
