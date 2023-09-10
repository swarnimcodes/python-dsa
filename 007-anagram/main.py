"""
Question:
Given two strings s and t, return true if t is an anagram of s,
and false otherwise.

An Anagram is a word or phrase formed by rearranging the
letters of a different word or phrase, typically using all the
original letters exactly once.

Input: s = "anagram", t = "nagaram"
Output: true
"""

"""
Brute Force:
Quite slow and takes up a lot of memory.
"""


def anagram_brute(word: str, target: str) -> bool:
    if len(word) != len(target):
        return False
    word_char = []
    target_char = []
    for char in word:
        word_char.append(char)
    for char in target:
        target_char.append(char)
    word_char.sort()
    target_char.sort()
    if word_char == target_char:
        return True
    else:
        return False


"""
Optimized Approach 1:
"""


def anagram(word, target) -> bool:
    if len(word) != len(target):
        return False
    char_count = {}
    for char in word:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for char in target:
        if char in char_count:
            char_count[char] -= 1
            if char_count[char] < 0:
                return False
        else:
            return False
    return True

def main():
    word = "ccac"
    target = "aaca"
    cond = anagram(word, target)
    print(f"Condition: {cond}")


if __name__ == "__main__":
    main()
