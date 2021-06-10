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

    def test_remove_nth_node(self):
        data = LinkedList.remove_nth_node_from_end_of_list(get_list_node([1, 2, 3, 4, 5]), 2)
        actual = []
        while data:
            actual.append(data.val)
            data = data.next
        self.assertEqual([1, 2, 3, 5], actual)
        data = LinkedList.remove_nth_node_from_end_of_list(get_list_node([1, 2]), 2)
        actual = []
        while data:
            actual.append(data.val)
            data = data.next
        self.assertEqual([2], actual)

    def test_merge_two_sorted_lists(self):
        data = LinkedList.merge_two_sorted_lists(get_list_node([1, 2, 4]), get_list_node([1, 3, 4]))
        actual = []
        while data:
            actual.append(data.val)
            data = data.next
        self.assertEqual([1, 1, 2, 3, 4, 4], actual)
        self.assertEqual(None, LinkedList.merge_two_sorted_lists(get_list_node([]), get_list_node([])))
        pass
