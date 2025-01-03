---
title: 249-Group-Shifted-Strings
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/group-shifted-strings


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
  def groupStrings(self, strings: List[str]) -> List[List[str]]:
    keyToStrings = defaultdict(list)

    # 'abc' . '11' because diff(a, b) = 1 and diff(b, c) = 1
    def getKey(s: str) -> str:
      key = ''

      for i in range(1, len(s)):
        diff = (ord(s[i]) - ord(s[i - 1]) + 26) % 26
        key += str(diff) + ','

      return key

    for s in strings:
      keyToStrings[getKey(s)].append(s)

    return keyToStrings.values()
```


```
new Solution().groupStrings()
```


---
**Score: 5**