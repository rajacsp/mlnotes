---
title: 479-Largest-Palindrome-Product
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/largest-palindrome-product


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
  def largestPalindrome(self, n: int) -> int:
    if n == 1:
      return 9

    kMod = 1337
    upper = pow(10, n) - 1
    lower = pow(10, n - 1) - 1

    for i in range(upper, lower, -1):
      cand = int(str(i) + str(i)[::-1])
      j = upper
      while j * j >= cand:
        if cand % j == 0:
          return cand % kMod
        j -= 1
```


```
new Solution().largestPalindrome()
```


---
**Score: 5**