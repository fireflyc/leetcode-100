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
