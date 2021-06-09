import unittest
from leetcode.stella import LinkedList


def get_list_node(data):
    node = LinkedList.ListNode()
    cur = node
    for e in data:
        next_one = LinkedList.ListNode(val=e)
        cur.next = next_one
        cur = cur.next
    return node.next


class LinkedListTestCase(unittest.TestCase):
    def test_add_two_numbers(self):
        ret, actual = LinkedList.add_two_numbers(l1=get_list_node([2, 4, 3]), l2=get_list_node([5, 6, 4])), []
        while ret:
            actual.append(ret.val)
            ret = ret.next
        self.assertEqual([7, 0, 8], actual)

    def test_middle_of_the_linked_list(self):
        node = LinkedList.middle_of_the_linked_list(get_list_node([1, 2, 3, 4, 5]))
        self.assertEqual(3, node.val)
        node = LinkedList.middle_of_the_linked_list(get_list_node([1, 2, 3, 4, 5, 6]))
        self.assertEqual(4, node.val)

