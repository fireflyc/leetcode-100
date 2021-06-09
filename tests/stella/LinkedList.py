import unittest
from leetcode.stella import LinkedList


class LinkedListTestCase(unittest.TestCase):
    def test_add_two_numbers(self):
        l1, l2, expect = [2, 4, 3], [5, 6, 4], [7, 0, 8]
        node1, node2 = LinkedList.ListNode(), LinkedList.ListNode()
        for node, data in [(node1, l1), (node2, l2)]:
            cur = node
            for e in data:
                next_one = LinkedList.ListNode(val=e)
                cur.next = next_one
                cur = cur.next
        ret, actual = LinkedList.add_two_numbers(l1=node1.next, l2=node2.next), []
        while ret:
            actual.append(ret.val)
            ret = ret.next
        self.assertEqual(expect, actual)

