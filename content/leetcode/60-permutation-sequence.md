---
title: 60-Permutation-Sequence
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/permutation-sequence


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
  def getPermutation(self, n: int, k: int) -> str:
    ans = ''
    nums = [i + 1 for i in range(n)]
    factorial = [1] * (n + 1)  # factorial[i] := i!

    for i in range(2, n + 1):
      factorial[i] = factorial[i - 1] * i

    k -= 1  # 0-indexed

    for i in reversed(range(n)):
      j = k // factorial[i]
      k %= factorial[i]
      ans += str(nums[j])
      nums.pop(j)

    return ans
```


```
new Solution().getPermutation()
```


---
**Score: 5**