---
title: 884-Uncommon-Words-From-Two-Sentences
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/uncommon-words-from-two-sentences


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
  def uncommonFromSentences(self, A: str, B: str) -> List[str]:
    count = Counter((A + ' ' + B).split())
    return [word for word, freq in count.items() if freq == 1]
```


```
new Solution().uncommonFromSentences()
```


---
**Score: 5**