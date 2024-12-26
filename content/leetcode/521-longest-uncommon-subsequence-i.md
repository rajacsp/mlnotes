---
title: 521-Longest-Uncommon-Subsequence-I
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/longest-uncommon-subsequence-i


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
  def findLUSlength(self, a: str, b: str) -> int:
    return -1 if a == b else max(len(a), len(b))
```


```
new Solution().findLUSlength()
```


---
**Score: 5**