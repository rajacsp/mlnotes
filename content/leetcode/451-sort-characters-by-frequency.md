---
title: 451-Sort-Characters-By-Frequency
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/sort-characters-by-frequency


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
  def frequencySort(self, s: str) -> str:
    ans = []
    bucket = [[] for _ in range(len(s) + 1)]

    for c, freq in Counter(s).items():
      bucket[freq].append(c)

    for freq in reversed(range(len(bucket))):
      for c in bucket[freq]:
        ans.append(c * freq)

    return ''.join(ans)
```


```
new Solution().frequencySort()
```


---
**Score: 5**