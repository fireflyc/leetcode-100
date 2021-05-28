from typing import List


def find_words_that_can_be_formed_by_characters(words: List[str], chars: str) -> int:
    def match_character(w):
        matching = chars
        for i in range(0, len(w)):
            pos = matching.find(w[i])
            if pos > -1:
                matching = matching[:pos]+matching[pos+1:]
            else:
                return 0
        return len(w)

    total_match = 0
    for word in words:
        total_match += match_character(word)

    return total_match


def print_words_vertically(s: str) -> List[str]:
    words = []
    blank = " "
    pos = 0
    for c in s:
        if c == blank:
            pos = 0
            continue
        if len(words) <= pos:
            words.append("")
        if len(words[pos]) < len(words[0])-1:
            words[pos] += blank*(len(words[0])-1-len(words[pos]))
        words[pos] += c
        pos += 1
    return words


def string_without_aaa_or_bbb(a: int, b: int) -> str:
    s = ""
    letters = {'a': a, 'b': b}
    while len(s) < a + b:
        if letters['a'] != letters['b']:
            l1, l2 = ('a', 'b') if letters['a'] > letters['b'] else ('b', 'a')
            if len(s) > 1 and s[-2:] == l1*2:
                s += l2
                letters[l2] -= 1
            else:
                s += l1
                letters[l1] -= 1
        else:
            s += 'ab'*letters['a'] if s and s[-1] == 'b' else 'ba'*letters['b']
            letters['a'], letters['b'] = 0, 0
    return s


class TrieNode:
    def __init__(self, value: str = None):
        self.value = value
        self.children = []

    def find_child(self, value):
        for child in self.children:
            if child.value == value:
                return child

    def append_child(self, child):
        self.children.append(child)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word+"\n":
            child = cur.find_child(c)
            if child:
                cur = child
            else:
                node = TrieNode(c)
                cur.append_child(node)
                cur = node

    def search(self, word: str) -> bool:
        return self.startsWith(word+"\n")

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            cur = cur.find_child(c)
            if not cur:
                return False
        return True


def implement_trie_prefix_tree(operators: List[str], operands: List[List]) -> List:
    trie, output = None, []
    for i, operator in enumerate(operators):
        operand = operands[i]
        if operator == "Trie":
            trie = Trie()
            output.append(None)
        if operator == "insert":
            output.append(trie.insert(*operand))
        if operator == "search":
            output.append(trie.search(*operand))
        if operator == "startsWith":
            output.append(trie.startsWith(*operand))
    return output


def longest_happy_prefix(s: str) -> str:
    prefix = ""
    for i in range(1, len(s)):
        if s[:i] == s[-1*i:]:
            prefix = s[:i]
    return prefix


def word_search_ii(board: List[List[str]], words: List[str]) -> List[str]:
    limit_row, limit_col = len(board), len(board[0])
    char_collection = set([board[r][c] for c in range(0, limit_col) for r in range(0, limit_row)])
    words = [w for w in words if set(w).issubset(char_collection)]

    def match(row, col, target):
        if board[row][col] != target[0]:
            return False
        matched, nth_letter, match_rc = target[0], 1, [(row, col, {(row, col)})]
        while nth_letter < len(target) and match_rc:
            tmp = []
            for match_r, match_c, traversed in match_rc:
                for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    ri, cj = match_r + i, match_c + j
                    if (ri, cj) not in traversed and 0 <= ri < limit_row and 0 <= cj < limit_col and \
                            target[nth_letter] == board[ri][cj]:
                        tmp.append((ri, cj, traversed | {(ri, cj)}))
            if not tmp:
                break
            match_rc = tmp
            matched += target[nth_letter]
            nth_letter += 1
        return matched == target

    found = set()
    for r in range(0, limit_row):
        for c in range(0, limit_col):
            for w in words:
                if w not in found and match(r, c, w):
                    found.add(w)
    return list(found)


def short_encoding_of_words(words: List[str]) -> int:
    fragments = []
    for w in words:
        to_insert = True
        for i, f in enumerate(fragments):
            if f.endswith(w) or w.endswith(f):
                fragments[i] = f if len(f) > len(w) else w
                to_insert = False
                break
        if to_insert:
            fragments.append(w)
    return len("#".join(fragments))+1


def is_unique_lcci(astr: str) -> bool:
    for i in range(1, len(astr)):
        for j in range(0, i):
            if astr[i] == astr[j]:
                return False
    return True


def check_permutation_lcci(s1: str, s2: str) -> bool:
    if len(s1) < len(s2):
        return False
    i = 0
    while i < len(s1):
        count = 0
        while s2[0] != s1[i] and count < len(s2):
            s2 = s2[1:]+s2[0]
            count += 1
        if count < len(s2):
            s2 = s2[1:]
        else:
            break
        i += 1
    return i >= len(s1)


def longest_substring_without_repeating_characters(s: str) -> int:
    substring_length = 0
    for i in range(0, len(s)):
        for j in range(i, len(s)):
            repeat = False
            for k in range(i, j):
                if s[k] == s[j]:
                    repeat = True
                    break
            if repeat:
                break
            else:
                substring_length = max(j-i+1, substring_length)
    return substring_length


def string_to_integer_atoi(s: str) -> int:
    numbers, blank, minus, plus = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"], " ", "-", "+"

    start, be_minus = 0, False
    for i, c in enumerate(s):
        if c in [blank]:
            start += 1
            continue
        elif c in numbers:
            start = i
            break
        elif c in [minus, plus]:
            be_minus = True if c == minus else False
            start = i+1 if i+1 < len(s) and s[i+1] in numbers else start-1
            break
        else:
            start -= 1
            break
    if start < 0:
        return 0

    digits = []
    for i in range(start, len(s)):
        if s[i] in numbers:
            digits.append(int(s[i]))
            continue
        break

    upper_limit, lower_limit = (2**31)-1, -1*(2**31)
    int_s, signed_int = 0, 0
    for d in digits:
        int_s = int_s*10 + d
        signed_int = int_s * (-1 if be_minus else 1)
        if signed_int <= lower_limit:
            return lower_limit
        if signed_int >= upper_limit:
            return upper_limit
    return signed_int


