from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def delete_leaves_with_a_given_value(root: TreeNode, target: int) -> TreeNode:
    def is_leave(some_node):
        return some_node and some_node.left is None and some_node.right is None

    def delete_leaves(node):
        if not node:
            return
        delete_leaves(node.left)
        delete_leaves(node.right)
        if is_leave(node.left) and node.left.val == target:
            node.left = None
        if is_leave(node.right) and node.right.val == target:
            node.right = None

    delete_leaves(root)
    return None if is_leave(root) and root.val == target else root


def maximum_depth_of_binary_tree(root: TreeNode) -> int:
    def depth(node):
        return 1 + max(depth(node.left), depth(node.right)) if node else 0

    return depth(root)


def convert_sorted_array_to_binary_search_tree(nums: List[int]) -> TreeNode:
    def bst(arr: List[int]):
        if len(arr) == 1:
            return TreeNode(val=arr[0])
        if not arr:
            return None
        pos = int(len(arr) / 2)
        node = TreeNode(val=arr[pos], left=bst(arr[:pos]), right=bst(arr[pos + 1:]))
        return node

    return bst(nums)
