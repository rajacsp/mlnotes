---
title: 28-Find-The-Index-Of-The-First-Occurrence-In-A-String
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string


```python
import pyutil as pyu
pyu.get_local_pyinfo()
```


```python
print(pyu.ps2("python-dotenv"))
```


```python
from typing import List
```


```python
class Solution:
  def strStr(self, haystack: str, needle: str) -> int:
    m = len(haystack)
    n = len(needle)

    for i in range(m - n + 1):
      if haystack[i:i + n] == needle:
        return i

    return -1
```


```python
new Solution().strStr()
```


---
**Score: 5**