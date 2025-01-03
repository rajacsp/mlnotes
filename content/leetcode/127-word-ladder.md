---
title: 127-Word-Ladder
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/word-ladder


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
class Solution:
  def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    wordSet = set(wordList)
    if endWord not in wordSet:
      return 0

    ans = 0
    q = deque([beginWord])

    while q:
      ans += 1
      for _ in range(len(q)):
        wordList = list(q.popleft())
        for i, cache in enumerate(wordList):
          for c in string.ascii_lowercase:
            wordList[i] = c
            word = ''.join(wordList)
            if word == endWord:
              return ans + 1
            if word in wordSet:
              q.append(word)
              wordSet.remove(word)
          wordList[i] = cache

    return 0
```


```
new Solution().ladderLength()
```


---
**Score: 5**