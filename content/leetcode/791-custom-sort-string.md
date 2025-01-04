---
title: 791-Custom-Sort-String
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/custom-sort-string


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
  def customSortString(self, S: str, T: str) -> str:
    ans = ""
    count = [0] * 26

    for c in T:
      count[ord(c) - ord('a')] += 1

    for c in S:
      while count[ord(c) - ord('a')] > 0:
        ans += c
        count[ord(c) - ord('a')] -= 1

    for c in string.ascii_lowercase:
      for _ in range(count[ord(c) - ord('a')]):
        ans += c

    return ans
```


```
new Solution().customSortString()
```


---
**Score: 5**