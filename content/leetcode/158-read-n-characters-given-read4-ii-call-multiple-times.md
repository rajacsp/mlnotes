---
title: 158-Read-N-Characters-Given-Read4-Ii-Call-Multiple-Times
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times


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
# The read4 API is already defined for you.
# Def read4(buf4: List[str]) -> int:

class Solution:
  def read(self, buf: List[str], n: int) -> int:
    i = 0  # buf's index

    while i < n:
      if self.i4 == self.n4:  # All characters in buf4 are consumed
        self.i4 = 0  # Reset buf4's index
        self.n4 = read4(self.buf4)  # Read 4 (or less) chars from file to buf4
        if self.n4 == 0:  # Reach the EOF
          return i
      buf[i] = self.buf4[self.i4]
      i += 1
      self.i4 += 1

    return i

  buf4 = [' '] * 4
  i4 = 0  # buf4's index
  n4 = 0  # buf4's size
```


```
new Solution().read()
```


---
**Score: 5**