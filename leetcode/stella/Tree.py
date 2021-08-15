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


def lowest_common_ancestor_of_binary_tree(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    def get_ancestors(node, val):
        if not node:
            return []
        if node.val == val:
            return [node]
        if node.val != val:
            left_ancestor = get_ancestors(node.left, val)
            if left_ancestor:
                return [node] + left_ancestor
            right_ancestor = get_ancestors(node.right, val)
            if right_ancestor:
                return [node] + right_ancestor
        return []

    p_ancestors, q_ancestors = get_ancestors(root, p.val), get_ancestors(root, q.val)
    common_ancestor = None
    for i in range(0, min(len(p_ancestors), len(q_ancestors))):
        if p_ancestors[i].val == q_ancestors[i].val:
            common_ancestor = p_ancestors[i]
    return common_ancestor


def binary_tree_level_order_traversal(root: TreeNode) -> List[List[int]]:
    layers = []
    layer_nodes = [root] if root else []
    while layer_nodes:
        layers.append([n.val for n in layer_nodes])
        tmp = []
        for node in layer_nodes:
            if node.left:
                tmp.append(node.left)
            if node.right:
                tmp.append(node.right)
        layer_nodes = tmp
    return layers


def validate_binary_search_tree(root: TreeNode) -> bool:
    def is_bst(node, less_than=None, greater_than=None):
        if node is None:
            return True
        if less_than is not None and node.val >= less_than:
            return False
        if greater_than is not None and node.val <= greater_than:
            return False
        return is_bst(node.left, less_than=min(less_than, node.val) if less_than is not None else node.val, greater_than=greater_than) and is_bst(node.right, less_than=less_than, greater_than=max(greater_than,node.val) if greater_than is not None else node.val)

    return is_bst(root, None, None)


def powerx_n(x: float, n: int):
    cache = {}

    def power(x, n):
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == 2:
            return x*x
        if n in cache:
            return cache[n]
        data = power(x, int(n/2)) * power(x, n-int(n/2))
        cache[n] = data
        return data

    return power(1/x if n < 0 else x, abs(n))


def kth_smallest_element_in_a_bst(root: TreeNode, k: int):
    cache = {}

    def visit(node, nodes_before=0):
        if not node:
            return nodes_before
        nodes_before = visit(node.left, nodes_before=nodes_before)
        cache[nodes_before+1] = node.val
        nodes_before = visit(node.right, nodes_before+1)
        return nodes_before

    visit(root)
    return cache[k]


