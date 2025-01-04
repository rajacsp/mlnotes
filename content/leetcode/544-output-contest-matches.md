---
title: 544-Output-Contest-Matches
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/output-contest-matches


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
  def findContestMatch(self, n: int) -> str:
    def generateMatches(matches: List[str]) -> str:
      if len(matches) == 1:
        return matches[0]

      nextMatches = []

      for i in range(len(matches) // 2):
        nextMatches.append(
            '(' + matches[i] + ',' + matches[len(matches) - 1 - i] + ')')

      return generateMatches(nextMatches)

    return generateMatches([str(i + 1) for i in range(n)])
```


```
new Solution().findContestMatch()
```


---
**Score: 5**