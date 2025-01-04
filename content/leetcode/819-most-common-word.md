---
title: 819-Most-Common-Word
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/most-common-word


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
  def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
    banned = set(banned)
    words = re.findall(r'\w+', paragraph.lower())
    return Counter(word for word in words if word not in banned).most_common(1)[0][0]
```


```
new Solution().mostCommonWord()
```


---
**Score: 5**