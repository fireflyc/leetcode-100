import unittest
from leetcode.stella import String


class StringTestCase(unittest.TestCase):

    def test_find_words_that_can_be_formed_by_characters(self):
        count_characters = String.find_words_that_can_be_formed_by_characters
        self.assertEqual(6, count_characters(words=["cat", "bt", "hat", "tree"], chars="atach"))
        self.assertEqual(10, count_characters(words=["hello", "world", "leetcode"], chars="welldonehoneyr"))

    def test_print_words_vertically(self):
        self.assertEqual(["HAY", "ORO", "WEU"], String.print_words_vertically("HOW ARE YOU"))
        self.assertEqual(["TBONTB", "OEROOE", "   T"], String.print_words_vertically("TO BE OR NOT TO BE"))
        self.assertEqual(["CIC", "OSO", "N M", "T I", "E N", "S G", "T"],
                         String.print_words_vertically("CONTEST IS COMING"))

    def test_string_without_aaa_or_bbb(self):
        self.assertIn(String.string_without_aaa_or_bbb(1, 2), ["abb", "bab", "bba"])
        self.assertEqual("aabaa", String.string_without_aaa_or_bbb(4, 1))
        self.assertEqual("bbab", String.string_without_aaa_or_bbb(1, 3))

    def test_implement_trie_prefix_tree(self):
        self.assertEqual([None, None, True, False, True, None, True], String.implement_trie_prefix_tree(
            operators=["Trie", "insert", "search", "search", "startsWith", "insert", "search"],
            operands=[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
        ))
        pass

