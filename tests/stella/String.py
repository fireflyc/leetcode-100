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

    def test_string_to_integer_atoi(self):
        self.assertEqual(42, String.string_to_integer_atoi("42"))
        self.assertEqual(-42, String.string_to_integer_atoi("   -42"))
        self.assertEqual(4193, String.string_to_integer_atoi("4193 with words"))
        self.assertEqual(0, String.string_to_integer_atoi("words and 987"))
        self.assertEqual(-2147483648, String.string_to_integer_atoi("-91283472332"))
        self.assertEqual(0, String.string_to_integer_atoi("-"))
        self.assertEqual(1, String.string_to_integer_atoi("+1"))
        self.assertEqual(1, String.string_to_integer_atoi("  +01"))

    def test_reverse_words_in_a_string(self):
        self.assertEqual("blue is sky the", String.reverse_words_in_a_string("the sky is blue"))
        self.assertEqual("world hello", String.reverse_words_in_a_string("  hello world  "))
        self.assertEqual("example good a", String.reverse_words_in_a_string("a good   example"))
        self.assertEqual("Alice Loves Bob", String.reverse_words_in_a_string("  Bob    Loves  Alice   "))
        self.assertEqual("bob like even not does Alice",
                         String.reverse_words_in_a_string("Alice does not even like bob"))

    def test_integer_to_english_words(self):
        self.assertEqual("One Hundred Twenty Three", String.integer_to_english_words(123))
        self.assertEqual("Twelve Thousand Three Hundred Forty Five", String.integer_to_english_words(12345))
        self.assertEqual("One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven",
                         String.integer_to_english_words(1234567))
        self.assertEqual("One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred "
                         "Ninety One", String.integer_to_english_words(1234567891))
        self.assertEqual("Eighty Three", String.integer_to_english_words(83))
        self.assertEqual("Zero", String.integer_to_english_words(0))

    def test_count_the_repetitions(self):
        self.assertEqual(2, String.count_max_repetitions(s1="acb", n1=4, s2="ab", n2=2))
        self.assertEqual(1, String.count_max_repetitions(s1="acb", n1=1, s2="acb", n2=1))
        self.assertEqual(4, String.count_max_repetitions(s1="aaa", n1=3, s2="aa", n2=1))
        self.assertEqual(2468, String.count_max_repetitions(s1="niconiconi", n1=99981, s2="nico", n2=81))
        self.assertEqual(10000, String.count_max_repetitions(
            s1="phqghumeaylnlfdxfircvscxggbwkfnqduxwfnfozvsrtkjpre", n1=1000000, s2="pggxr", n2=100
        ))
        self.assertEqual(27, String.count_max_repetitions(
            s1="phqghumeaylnlfdxfircvscxggbwkfnqduxwfnfozvsrtkjprepggxrpnrvystmwcysyycqpevikeffmznimkkasvw",
            n1=100000, s2="srenzkycxfxtlsgypsfadpooefxzbcoej", n2=333
        ))
        self.assertEqual(5620, String.count_max_repetitions(
            s1="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", n1=1000000,
            s2="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", n2=103
        ))

    def test_super_palindromes(self):
        self.assertEqual(4, String.super_palindromes(left="4", right="1000"))
        self.assertEqual(2, String.super_palindromes(left="40000000000000000", right="50000000000000000"))
        self.assertEqual(47, String.super_palindromes(left="4", right=str(10 ** 16)))

    def test_word_subsets(self):
        self.assertEqual(["facebook", "google", "leetcode"], String.word_subsets(
            words1=["amazon", "apple", "facebook", "google", "leetcode"], words2=["e", "o"]
        ))
        self.assertEqual(["apple", "google", "leetcode"], String.word_subsets(
            words1=["amazon", "apple", "facebook", "google", "leetcode"], words2=["l", "e"]
        ))
        self.assertEqual(["facebook", "google"], String.word_subsets(
            words1=["amazon", "apple", "facebook", "google", "leetcode"], words2=["e", "oo"]
        ))
        self.assertEqual(["google", "leetcode"], String.word_subsets(
            words1=["amazon", "apple", "facebook", "google", "leetcode"], words2=["lo", "eo"]
        ))
        self.assertEqual(["facebook", "leetcode"], String.word_subsets(
            words1=["amazon", "apple", "facebook", "google", "leetcode"], words2=["ec", "oc", "ceo"]
        ))
