---
title: 940-Distinct-Subsequences-Ii
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/distinct-subsequences-ii


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
  def distinctSubseqII(self, s: str) -> int:
    kMod = 1_000_000_007
    # endsWith[i] := # Of subseqs ends with 'a' + i
    endsWith = [0] * 26

    for c in s:
      endsWith[ord(c) - ord('a')] = (sum(endsWith) + 1) % kMod

    return sum(endsWith) % kMod
```


```
new Solution().distinctSubseqII()
```


---
**Score: 5**