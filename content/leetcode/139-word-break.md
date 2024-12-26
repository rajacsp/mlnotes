---
title: 139-Word-Break
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/word-break


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
  def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    wordSet = set(wordDict)

    @functools.lru_cache(None)
    def wordBreak(s: str) -> bool:
      if s in wordSet:
        return True
      return any(s[:i] in wordSet and wordBreak(s[i:]) for i in range(len(s)))

    return wordBreak(s)
```


```
new Solution().wordBreak()
```


---
**Score: 5**