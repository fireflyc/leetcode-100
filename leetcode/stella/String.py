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
    limit_row, limit_col, limit_word = len(board), len(board[0]), max([len(w) for w in words])
    found = set()

    def match(row, col, prefix="", traversed=set()):
        if not (len(prefix) < limit_word and 0 <= row < limit_row and 0 <= col < limit_col and (row, col) not in traversed):
            return
        s = prefix + board[row][col]
        if s in words:
            found.add(s)
        match(row + 1, col, s, traversed | {(row, col)})
        match(row - 1, col, s, traversed | {(row, col)})
        match(row, col + 1, s, traversed | {(row, col)})
        match(row, col - 1, s, traversed | {(row, col)})

    for r in range(0, len(board)):
        for c in range(0, len(board[r])):
            match(r, c)
    return list(found)

