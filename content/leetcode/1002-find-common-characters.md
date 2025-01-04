---
title: 1002-Find-Common-Characters
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/find-common-characters


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
  def commonChars(self, A: List[str]) -> List[str]:
    ans = []
    commonCount = [math.inf] * 26

    for a in A:
      count = [0] * 26
      for c in a:
        count[ord(c) - ord('a')] += 1
      for i in range(26):
        commonCount[i] = min(commonCount[i], count[i])

    for c in string.ascii_lowercase:
      for j in range(commonCount[ord(c) - ord('a')]):
        ans.append(c)

    return ans
```


```
new Solution().commonChars()
```


---
**Score: 5**