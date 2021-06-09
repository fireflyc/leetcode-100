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
    elif distance == n-1:
        return head.next
    else:
        return head
