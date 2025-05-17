---
title: 9-Palindrome-Number
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/palindrome-number


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
  def isPalindrome(self, x: int) -> bool:
    if x < 0:
      return False

    rev = 0
    y = x

    while y:
      rev = rev * 10 + y % 10
      y //= 10

    return rev == x
```


```
new Solution().isPalindrome()
```


---
**Score: 5**