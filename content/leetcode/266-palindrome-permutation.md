---
title: 266-Palindrome-Permutation
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/palindrome-permutation


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
  def canPermutePalindrome(self, s: str) -> bool:
    seen = set()

    for c in s:
      if c in seen:
        seen.remove(c)
      else:
        seen.add(c)

    return len(seen) <= 1
```


```
new Solution().canPermutePalindrome()
```


---
**Score: 5**