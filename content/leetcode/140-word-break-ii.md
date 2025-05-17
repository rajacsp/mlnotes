---
title: 140-Word-Break-Ii
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/word-break-ii


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
  def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
    wordSet = set(wordDict)

    @functools.lru_cache(None)
    def wordBreak(s: str) -> List[str]:
      ans = []

      # 1 <= len(prefix) < len(s)
      for i in range(1, len(s)):
        prefix = s[0:i]
        suffix = s[i:]
        if prefix in wordSet:
          for word in wordBreak(suffix):
            ans.append(prefix + ' ' + word)

      # Contains whole string, so don't add any space
      if s in wordSet:
        ans.append(s)

      return ans

    return wordBreak(s)
```


```
new Solution().wordBreak()
```


---
**Score: 5**