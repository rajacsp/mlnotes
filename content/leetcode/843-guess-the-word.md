---
title: 843-Guess-The-Word
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/guess-the-word


```
import pyutil as pyu
pyu.get_local_pyinfo()
```


```
print(pyu.ps2("python-dotenv"))
```


```
from typing import List
```


```
# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# Class Master:
#   def guess(self, word: str) -> int:

class Solution:
  def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
    def getMatches(s1: str, s2: str) -> int:
      matches = 0
      for c1, c2 in zip(s1, s2):
        if c1 == c2:
          matches += 1
      return matches

    for _ in range(10):
      guessedWord = wordlist[randint(0, len(wordlist) - 1)]
      matches = master.guess(guessedWord)
      if matches == 6:
        break
      wordlist = [
          word for word in wordlist
          if getMatches(guessedWord, word) == matches]
```


```
new Solution().findSecretWord()
```


---
**Score: 5**