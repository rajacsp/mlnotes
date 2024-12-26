---
title: 871-Minimum-Number-Of-Refueling-Stops
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/minimum-number-of-refueling-stops


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
  def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
    # dp[i] := farthest position we can reach w / i refuels
    dp = [startFuel] + [0] * len(stations)

    for i, station in enumerate(stations):
      for j in range(i + 1, 0, -1):
        if dp[j - 1] >= station[0]:  # With j - 1 refuels, we can reach stations[i][0]
          dp[j] = max(dp[j], dp[j - 1] + station[1])

    for i, d in enumerate(dp):
      if d >= target:
        return i

    return -1
```


```
new Solution().minRefuelStops()
```


---
**Score: 5**