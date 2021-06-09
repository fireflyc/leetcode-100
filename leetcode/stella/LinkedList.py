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
