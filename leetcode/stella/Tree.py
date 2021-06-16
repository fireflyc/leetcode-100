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


def binary_tree_right_side_view(root: TreeNode) -> List[int]:
    view = []
    view_of_layer = [root] if root else []
    while view_of_layer:
        view.append(view_of_layer[-1].val)
        tmp = []
        for n in view_of_layer:
            if n.left:
                tmp.append(n.left)
            if n.right:
                tmp.append(n.right)
        view_of_layer = tmp
    return view


def subtree_of_another_tree(root: TreeNode, subRoot: TreeNode) -> bool:
    def is_subtree(node1, node2):
        if not node1 and not node2:
            return True
        if (not node1 and node2) or (node1 and not node2):
            return False
        return node1.val == node2.val and is_subtree(node1.left, node2.left) and is_subtree(node1.right, node2.right)

    def find_node(val):
        nodes = [root]
        idx = 0
        while idx < len(nodes):
            if nodes[idx].val == val:
                yield nodes[idx]
            if nodes[idx].left:
                nodes.append(nodes[idx].left)
            if nodes[idx].right:
                nodes.append(nodes[idx].right)
            idx += 1

    if subRoot is None:
        return True
    for n in find_node(subRoot.val):
        ret = is_subtree(n, subRoot)
        if ret:
            return True
    return False
