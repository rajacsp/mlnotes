---
title: 500-Keyboard-Row
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/keyboard-row


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
  def findWords(self, words: List[str]) -> List[str]:
    ans = []
    rows = [set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')]

    for word in words:
      lowerWord = set(word.lower())
      if any(lowerWord <= row for row in rows):
        ans.append(word)

    return ans
```


```
new Solution().findWords()
```


---
**Score: 5**