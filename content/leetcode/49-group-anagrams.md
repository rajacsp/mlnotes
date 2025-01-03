---
title: 49-Group-Anagrams
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/group-anagrams


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
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    dict = defaultdict(list)

    for str in strs:
      key = ''.join(sorted(str))
      dict[key].append(str)

    return dict.values()
```


```
new Solution().groupAnagrams()
```


---
**Score: 5**