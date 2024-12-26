---
title: 1048-Longest-String-Chain
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/longest-string-chain


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
  def longestStrChain(self, words: List[str]) -> int:
    wordsSet = set(words)

    # Dp(s) := longest chain where s is the last word
    @functools.lru_cache(None)
    def dp(s: str) -> int:
      ans = 1
      for i in range(len(s)):
        pred = s[:i] + s[i + 1:]
        if pred in wordsSet:
          ans = max(ans, dp(pred) + 1)
      return ans

    return max(dp(word) for word in words)
```


```
new Solution().longestStrChain()
```


---
**Score: 5**