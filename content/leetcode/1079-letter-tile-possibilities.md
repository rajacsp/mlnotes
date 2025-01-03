---
title: 1079-Letter-Tile-Possibilities
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/letter-tile-possibilities


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
  def numTilePossibilities(self, tiles: str) -> int:
    count = Counter(tiles)

    def dfs(count: Dict[int, int]) -> int:
      possibleSequences = 0

      for k, v in count.items():
        if v == 0:
          continue
        # Put c in the current position. We only care about the # of possible
        # sequences of letters but don't care about the actual combination.
        count[k] -= 1
        possibleSequences += 1 + dfs(count)
        count[k] += 1

      return possibleSequences

    return dfs(count)
```


```
new Solution().numTilePossibilities()
```


---
**Score: 5**