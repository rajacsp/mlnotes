---
title: 522-Longest-Uncommon-Subsequence-Ii
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/longest-uncommon-subsequence-ii


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
  def findLUSlength(self, strs: List[str]) -> int:
    def isSubsequence(a: str, b: str) -> bool:
      i = 0
      j = 0

      while i < len(a) and j < len(b):
        if a[i] == b[j]:
          i += 1
        j += 1

      return i == len(a)

    seen = set()
    duplicates = set()

    for s in strs:
      if s in seen:
        duplicates.add(s)
      seen.add(s)

    strs.sort(key=lambda s: -len(s))

    for i in range(len(strs)):
      if strs[i] in duplicates:
        continue
      isASubsequence = False
      for j in range(i):
        isASubsequence |= isSubsequence(strs[i], strs[j])
      if not isASubsequence:
        return len(strs[i])

    return -1
```


```
new Solution().findLUSlength()
```


---
**Score: 5**