---
title: 318-Maximum-Product-Of-Word-Lengths
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/maximum-product-of-word-lengths


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
  def maxProduct(self, words: List[str]) -> int:
    ans = 0

    def getMask(word: str) -> int:
      mask = 0
      for c in word:
        mask |= 1 << ord(c) - ord('a')
      return mask

    masks = [getMask(word) for word in words]

    for i in range(len(words)):
      for j in range(i):
        if not (masks[i] & masks[j]):
          ans = max(ans, len(words[i]) * len(words[j]))

    return ans
```


```
new Solution().maxProduct()
```


---
**Score: 5**