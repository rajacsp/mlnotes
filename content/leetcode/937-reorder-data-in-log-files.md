---
title: 937-Reorder-Data-In-Log-Files
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/reorder-data-in-log-files


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
  def reorderLogFiles(self, logs: List[str]) -> List[str]:
    digitLogs = []
    letterLogs = []

    for log in logs:
      i = log.index(' ')
      if log[i + 1].isdigit():
        digitLogs.append(log)
      else:
        letterLogs.append((log[:i], log[i + 1:]))

    letterLogs.sort(key=lambda l: (l[1], l[0]))

    return [identifier + ' ' + letters for identifier, letters in letterLogs] + digitLogs
```


```
new Solution().reorderLogFiles()
```


---
**Score: 5**