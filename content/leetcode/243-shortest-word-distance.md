---
title: 243-Shortest-Word-Distance
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/shortest-word-distance


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
  def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
    ans = len(wordsDict)
    index1 = -1  # wordsDict[index1] == word1
    index2 = -1  # wordsDict[index2] == word2

    for i, word in enumerate(wordsDict):
      if word == word1:
        index1 = i
        if index2 != -1:
          ans = min(ans, index1 - index2)
      if word == word2:
        index2 = i
        if index1 != -1:
          ans = min(ans, index2 - index1)

    return ans
```


```
new Solution().shortestDistance()
```


---
**Score: 5**