---
title: 824-Goat-Latin
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/goat-latin


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
  def toGoatLatin(self, S: str) -> str:
    ans = ''
    vowels = 'aeiouAEIOU'
    words = S.split()
    i = 1

    for word in words:
      if i > 1:
        ans += ' '
      if word[0] in vowels:
        ans += word
      else:
        ans += word[1:] + word[0]
      ans += 'ma' + 'a' * i
      i += 1

    return ans
```


```
new Solution().toGoatLatin()
```


---
**Score: 5**