---
title: 345-Reverse-Vowels-Of-A-String
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/reverse-vowels-of-a-string


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
  def reverseVowels(self, s: str) -> str:
    charList = list(s)
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    l = 0
    r = len(s) - 1

    while l < r:
      while l < r and charList[l] not in vowels:
        l += 1
      while l < r and charList[r] not in vowels:
        r -= 1
      charList[l], charList[r] = charList[r], charList[l]
      l += 1
      r -= 1

    return ''.join(charList)
```


```
new Solution().reverseVowels()
```


---
**Score: 5**