import unittest
from leetcode.stella import String


class StringTestCase(unittest.TestCase):

    def test_find_words_that_can_be_formed_by_characters(self):
        count_characters = String.find_words_that_can_be_formed_by_characters
        self.assertEqual(6, count_characters(words=["cat", "bt", "hat", "tree"], chars="atach"))
        self.assertEqual(10, count_characters(words=["hello", "world", "leetcode"], chars="welldonehoneyr"))
