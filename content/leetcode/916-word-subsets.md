---
title: 916-Word-Subsets
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/word-subsets


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
  def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
    count = Counter()

    for b in B:
      count = count | Counter(b)

    return [a for a in A if Counter(a) & count == count]
```


```
new Solution().wordSubsets()
```


---
**Score: 5**