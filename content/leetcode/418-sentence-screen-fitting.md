---
title: 418-Sentence-Screen-Fitting
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/sentence-screen-fitting


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
  def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
    combined = ' '.join(sentence) + ' '
    n = len(combined)
    i = 0

    for _ in range(rows):
      i += cols
      if combined[i % n] == ' ':
        i += 1
      else:
        while i > 0 and combined[(i - 1) % n] != ' ':
          i -= 1

    return i // n
```


```
new Solution().wordsTyping()
```


---
**Score: 5**