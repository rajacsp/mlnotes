---
title: 187-Repeated-Dna-Sequences
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/repeated-dna-sequences


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
  def findRepeatedDnaSequences(self, s: str) -> List[str]:
    ans = set()
    seen = set()

    for i in range(len(s) - 9):
      seq = s[i:i + 10]
      if seq in seen:
        ans.add(seq)
      seen.add(seq)

    return list(ans)
```


```
new Solution().findRepeatedDnaSequences()
```


---
**Score: 5**