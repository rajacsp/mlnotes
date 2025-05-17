---
title: 748-Shortest-Completing-Word
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/shortest-completing-word


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
  def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
    def isMatch(word: str) -> bool:
      wordCount = Counter(word)
      return False if any(wordCount[i] < count[i] for i in string.ascii_letters) else True

    ans = '*' * 16
    count = defaultdict(int)

    for c in licensePlate:
      if c.isalpha():
        count[c.lower()] += 1

    for word in words:
      if len(word) < len(ans) and isMatch(word):
        ans = word

    return ans
```


```
new Solution().shortestCompletingWord()
```


---
**Score: 5**