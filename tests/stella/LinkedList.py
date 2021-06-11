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


def link_to_list(root):
    actual = []
    while root:
        actual.append(root.val)
        root = root.next
    return actual


class LinkedListTestCase(unittest.TestCase):
    def test_add_two_numbers(self):
        ret = LinkedList.add_two_numbers(l1=get_list_node([2, 4, 3]), l2=get_list_node([5, 6, 4]))
        self.assertEqual([7, 0, 8], link_to_list(ret))

    def test_middle_of_the_linked_list(self):
        node = LinkedList.middle_of_the_linked_list(get_list_node([1, 2, 3, 4, 5]))
        self.assertEqual(3, node.val)
        node = LinkedList.middle_of_the_linked_list(get_list_node([1, 2, 3, 4, 5, 6]))
        self.assertEqual(4, node.val)

    def test_remove_nth_node(self):
        data = LinkedList.remove_nth_node_from_end_of_list(get_list_node([1, 2, 3, 4, 5]), 2)
        self.assertEqual([1, 2, 3, 5], link_to_list(data))
        data = LinkedList.remove_nth_node_from_end_of_list(get_list_node([1, 2]), 2)
        self.assertEqual([2], link_to_list(data))

    def test_merge_two_sorted_lists(self):
        data = LinkedList.merge_two_sorted_lists(get_list_node([1, 2, 4]), get_list_node([1, 3, 4]))
        self.assertEqual([1, 1, 2, 3, 4, 4], link_to_list(data))
        self.assertEqual(None, LinkedList.merge_two_sorted_lists(get_list_node([]), get_list_node([])))

    def test_merge_k_sorted_lists(self):
        data = LinkedList.merge_k_sorted_lists([get_list_node(i) for i in [[1, 4, 5], [1, 3, 4], [2, 6]]])
        self.assertEqual([1, 1, 2, 3, 4, 4, 5, 6], link_to_list(data))
        self.assertEqual([], link_to_list(LinkedList.merge_k_sorted_lists([])))
        self.assertEqual([], link_to_list(LinkedList.merge_k_sorted_lists([get_list_node(i) for i in [[]]])))

    def test_remove_duplicates_from_sorted_list_ii(self):
        remove_duplicates = LinkedList.remove_duplicates_from_sorted_list_ii
        self.assertEqual([1, 2, 5], link_to_list(remove_duplicates(get_list_node([1, 2, 3, 3, 4, 4, 5]))))
        self.assertEqual([2, 3], link_to_list(remove_duplicates(get_list_node([1, 1, 1, 2, 3]))))
        self.assertEqual([], link_to_list(remove_duplicates(get_list_node([1, 1]))))
        self.assertEqual([1], link_to_list(remove_duplicates(get_list_node([1, 2, 2]))))

    def test_partition_list(self):
        partition = LinkedList.partition_list
        self.assertEqual([1, 2, 2, 4, 3, 5], link_to_list(partition(get_list_node([1, 4, 3, 2, 5, 2]), 3)))
        self.assertEqual([1, 2], link_to_list(partition(get_list_node([2, 1]), 2)))
        self.assertEqual([], link_to_list(partition(get_list_node([]), 0)))
        self.assertEqual([1, 0, 2, 2, 4, 3, 5], link_to_list(partition(get_list_node([1, 4, 3, 0, 2, 5, 2]), 3)))
        self.assertEqual([1, 1], link_to_list(partition(get_list_node([1, 1]), 2)))
        self.assertEqual([2, 0, 1, 3, 1, 0, 3, 4, 4],
                         link_to_list(partition(get_list_node([2, 0, 4, 1, 3, 1, 4, 0, 3]), 4)))

    def test_rotate_list(self):
        self.assertEqual([4, 5, 1, 2, 3], link_to_list(LinkedList.rotate_list(get_list_node([1, 2, 3, 4, 5]), 2)))
        self.assertEqual([2, 0, 1], link_to_list(LinkedList.rotate_list(get_list_node([0, 1, 2]), 4)))
        self.assertEqual([1], link_to_list(LinkedList.rotate_list(get_list_node([1]), 1)))
        self.assertEqual([1, 1], link_to_list(LinkedList.rotate_list(get_list_node([1, 1]), 2)))

