---
title: 524-Longest-Word-In-Dictionary-Through-Deleting
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/longest-word-in-dictionary-through-deleting


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
  def findLongestWord(self, s: str, d: List[str]) -> str:
    ans = ''

    for word in d:
      i = 0
      for c in s:
        if i < len(word) and c == word[i]:
          i += 1
      if i == len(word):
        if len(word) > len(ans) or len(word) == len(ans) and word < ans:
          ans = word

    return ans
```


```
new Solution().findLongestWord()
```


---
**Score: 5**