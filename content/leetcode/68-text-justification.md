---
title: 68-Text-Justification
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/text-justification


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
  def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
    ans = []
    row = []
    rowLetters = 0

    for word in words:
      if rowLetters + len(word) + len(row) > maxWidth:
        for i in range(maxWidth - rowLetters):
          row[i % (len(row) - 1 or 1)] += ' '
        ans.append(''.join(row))
        row = []
        rowLetters = 0
      row.append(word)
      rowLetters += len(word)

    return ans + [' '.join(row).ljust(maxWidth)]
```


```
new Solution().fullJustify()
```


---
**Score: 5**