---
title: 744-Find-Smallest-Letter-Greater-Than-Target
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/find-smallest-letter-greater-than-target


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
  def nextGreatestLetter(self, letters: List[str], target: str) -> str:
    l = 0
    r = len(letters)

    while l < r:
      m = (l + r) >> 1
      if letters[m] <= target:
        l = m + 1
      else:
        r = m

    return letters[l % len(letters)]
```


```
new Solution().nextGreatestLetter()
```


---
**Score: 5**