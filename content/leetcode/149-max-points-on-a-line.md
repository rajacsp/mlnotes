---
title: 149-Max-Points-On-A-Line
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/max-points-on-a-line


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
  def maxPoints(self, points: List[List[int]]) -> int:
    ans = 0

    def gcd(a: int, b: int) -> int:
      return a if b == 0 else gcd(b, a % b)

    def getSlope(p: List[int], q: List[int]) -> Tuple[int, int]:
      dx = p[0] - q[0]
      dy = p[1] - q[1]
      if dx == 0:
        return (0, p[0])
      if dy == 0:
        return (p[1], 0)
      d = gcd(dx, dy)
      return (dx // d, dy // d)

    for i, p in enumerate(points):
      slopeCount = defaultdict(int)
      samePoints = 1
      maxPoints = 0
      for j in range(i + 1, len(points)):
        q = points[j]
        if p == q:
          samePoints += 1
        else:
          slope = getSlope(p, q)
          slopeCount[slope] += 1
          maxPoints = max(maxPoints, slopeCount[slope])
      ans = max(ans, samePoints + maxPoints)

    return ans
```


```
new Solution().maxPoints()
```


---
**Score: 5**