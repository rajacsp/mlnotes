---
title: 594-Longest-Harmonious-Subsequence
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/longest-harmonious-subsequence


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
  def findLHS(self, nums: List[int]) -> int:
    ans = 0
    count = Counter(nums)

    for num, freq in count.items():
      if num + 1 in count:
        ans = max(ans, freq + count[num + 1])

    return ans
```


```
new Solution().findLHS()
```


---
**Score: 5**