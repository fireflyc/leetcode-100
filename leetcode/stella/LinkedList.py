from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    root = ListNode()
    set_aside, cur = 0, root
    while l1 or l2 or set_aside > 0:
        next_one = ListNode()
        total = (l1.val if l1 else 0) + (l2.val if l2 else 0) + set_aside
        next_one.val = total % 10
        set_aside = int(total / 10)
        cur.next = next_one
        cur = next_one
        l1, l2 = l1.next if l1 else None, l2.next if l2 else None
    return root.next


def middle_of_the_linked_list(head: ListNode) -> ListNode:
    middle, end, middle_distance, end_distance = head, head, 0, 0
    while end.next:
        end = end.next
        end_distance += 1
        middle_pos = int((end_distance + 1) / 2) if end_distance % 2 else int(end_distance / 2)
        while middle_distance < middle_pos:
            middle = middle.next
            middle_distance += 1
    return middle


def remove_nth_node_from_end_of_list(head: ListNode, n: int) -> ListNode:
    target, walk, distance = head, head, 0
    while walk.next:
        walk = walk.next
        if distance < n:
            distance += 1
        else:
            target = target.next
    if distance == n:
        target.next = target.next.next if target.next else None
        return head
    elif distance == n - 1:
        return head.next
    else:
        return head


def merge_two_sorted_lists(l1: ListNode, l2: ListNode) -> ListNode:
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    root = l1 if l1.val <= l2.val else l2
    node1, node2 = (l1.next, l2) if l1.val <= l2.val else (l1, l2.next)
    cur = root
    while node1 or node2:
        node = node1 if (node1 and node2 and node1.val <= node2.val) or (node1 and not node2) else node2
        cur.next = node
        if node == node1:
            node1 = node1.next
        elif node == node2:
            node2 = node2.next
        cur = cur.next
    return root


def merge_k_sorted_lists(lists: List[ListNode]) -> ListNode:
    root = ListNode()
    cur = root
    while lists:
        lists = [node for node in lists if node is not None]
        if lists:
            min_idx, min_val = 0, lists[0].val
            for i in range(0, len(lists)):
                if lists[i].val < min_val:
                    min_idx, min_val = i, lists[i].val
            cur.next = lists[min_idx]
            cur = cur.next
            lists[min_idx] = lists[min_idx].next
    return root.next


def remove_duplicates_from_sorted_list_ii(head: ListNode) -> ListNode:
    root = ListNode()
    non_repeat, walk, repeat_val = root, head, None
    while walk:
        if walk.val != repeat_val and (not walk.next or walk.next.val != walk.val):
            non_repeat.next = walk
            non_repeat = non_repeat.next
            repeat_val = None
        elif walk.val != repeat_val and walk.next and walk.next.val == walk.val:
            repeat_val = walk.val
            walk = walk.next
        walk = walk.next
        non_repeat.next = None
    return root.next


def partition_list(head: ListNode, x: int) -> ListNode:
    root, demarc = ListNode(next=head), None
    cur, less_than = root, root
    while cur.next:
        if cur.next.val < x:
            if demarc is None:
                less_than = cur.next
            else:
                tmp = cur.next
                cur.next = tmp.next
                tmp.next = less_than.next
                less_than.next = tmp
                less_than = less_than.next
                continue
        elif cur.next.val >= x and demarc is None:
            demarc = cur.next
        cur = cur.next
    return root.next


def rotate_list(head: ListNode, k: int) -> ListNode:
    if head is None or k == 0:
        return head
    start, end, distance = head, head, 0
    while end.next:
        end = end.next
        distance += 1
        if distance > k:
            start = start.next
    if k > distance:
        for i in range(0, distance - k % (distance + 1)):
            start = start.next
    if start != end:
        tmp = start.next
        start.next = None
        end.next = head
        head = tmp
    return head
