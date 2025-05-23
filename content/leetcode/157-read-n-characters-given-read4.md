---
title: 157-Read-N-Characters-Given-Read4
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/read-n-characters-given-read4


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
"""
The read4 API is already defined for you.
    def read4(buf4: List[chr]) -> int:

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf4 = [' '] * 4 # Create buffer with enough space to store characters
read4(buf4) # Read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf4) # Read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf4) # Read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""


class Solution:
  def read(self, buf: List[str], n: int) -> int:
    buf4 = [' '] * 4
    i4 = 0  # buf4's index
    n4 = 0  # buf4's size
    i = 0  # buf's index

    while i < n:
      if i4 == n4:  # All characters in buf4 are consumed
        i4 = 0  # Reset buf4's index
        n4 = read4(buf4)  # Read 4 (or less) chars from file to buf4
        if n4 == 0:  # Reach the EOF
          return i
      buf[i] = buf4[i4]
      i += 1
      i4 += 1

    return i
```


```
new Solution().read()
```


---
**Score: 5**