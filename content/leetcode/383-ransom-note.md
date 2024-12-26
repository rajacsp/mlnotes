---
title: 383-Ransom-Note
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/ransom-note


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
  def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    count1 = Counter(ransomNote)
    count2 = Counter(magazine)
    return all(count1[c] <= count2[c] for c in string.ascii_lowercase)
```


```
new Solution().canConstruct()
```


---
**Score: 5**