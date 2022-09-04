from typing import List
from typing import Set


def wordBreak( s: str, wordDict: List[str]) -> bool:
    def wordBreakRecur(s: str, word_dict: Set[str], start: int):
        if start == len(s):
            return True
        for end in range(start + 1, len(s) + 1):
            if s[start:end] in word_dict and wordBreakRecur(s, word_dict, end):
                return True
        return False
    return wordBreakRecur(s, set(wordDict), 0)
s = "leetcode"
wordDict = ["leet","code"]
print(wordBreak(s,wordDict))