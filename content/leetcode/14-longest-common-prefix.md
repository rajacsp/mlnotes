---
title: 14-Longest-Common-Prefix
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/longest-common-prefix


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
  def longestCommonPrefix(self, strs: List[str]) -> str:
    if not strs:
      return ''

    for i in range(len(strs[0])):
      for j in range(1, len(strs)):
        if i == len(strs[j]) or strs[j][i] != strs[0][i]:
          return strs[0][:i]

    return strs[0]
```


```
new Solution().longestCommonPrefix()
```


---
**Score: 5**