def is_anagram(word1: str, word2: str):
    word1_set = set(word1)
    word2_set = set(word2)
    return word1_set == word2_set


word1 = "listen"
word2 = "silent"

print(is_anagram(word1, word2))
