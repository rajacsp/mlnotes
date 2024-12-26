---
title: 424-Longest-Repeating-Character-Replacement
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/longest-repeating-character-replacement


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
  def characterReplacement(self, s: str, k: int) -> int:
    ans = 0
    maxCount = 0
    count = Counter()

    l = 0
    for r, c in enumerate(s):
      count[c] += 1
      maxCount = max(maxCount, count[c])
      while maxCount + k < r - l + 1:
        count[s[l]] -= 1
        l += 1
      ans = max(ans, r - l + 1)

    return ans
```


```
new Solution().characterReplacement()
```


---
**Score: 5**