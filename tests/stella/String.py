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

    def test_longest_happy_prefix(self):
        self.assertEqual("l", String.longest_happy_prefix("level"))
        self.assertEqual("abab", String.longest_happy_prefix("ababab"))
        self.assertEqual("leet", String.longest_happy_prefix("leetcodeleet"))
        self.assertEqual("", String.longest_happy_prefix("a"))

    def test_word_search_ii(self):
        self.assertEqual(set(["eat", "oath"]), set(String.word_search_ii(
            board=[["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
            words=["oath", "pea", "eat", "rain"]
        )))
        self.assertEqual(set([]), set(String.word_search_ii(board=[["a", "b"], ["c", "d"]], words=["abcb"])))
        self.assertEqual([], String.word_search_ii(board=[["a"]], words=["ab"]))
        with open("word_search_ii.json", 'r') as fr:
            import json
            data = json.load(fr)
            self.assertEqual(["ababababab"], String.word_search_ii(board=data['board'], words=data['words']))

    def test_short_encoding_of_words(self):
        self.assertEqual(10, String.short_encoding_of_words(["time", "me", "bell"]))
        self.assertEqual(2, String.short_encoding_of_words(["t"]))

    def test_is_unique_lcci(self):
        self.assertEqual(False, String.is_unique_lcci("leetcode"))
        self.assertEqual(True, String.is_unique_lcci("abc"))

    def test_check_permutation_lcci(self):
        self.assertEqual(True, String.check_permutation_lcci(s1="abc", s2="bca"))
        self.assertEqual(False, String.check_permutation_lcci(s1="abc", s2="bad"))
        self.assertEqual(False, String.check_permutation_lcci(s1="a", s2="ab"))

    def test_longest_substring_without_repeating_characters(self):
        longest_substring = String.longest_substring_without_repeating_characters
        self.assertEqual(3, longest_substring("abcabcbb"))
        self.assertEqual(1, longest_substring("bbbbb"))
        self.assertEqual(3, longest_substring("pwwkew"))
        self.assertEqual(0, longest_substring(""))
