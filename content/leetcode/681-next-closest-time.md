---
title: 681-Next-Closest-Time
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/next-closest-time


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
  def nextClosestTime(self, time: str) -> str:
    ans = list(time)
    digits = sorted(ans)

    def nextClosest(digit: chr, limit: chr) -> chr:
      next = bisect_right(digits, digit)
      return digits[0] if next == 4 or digits[next] > limit else digits[next]

    ans[4] = nextClosest(ans[4], '9')
    if time[4] < ans[4]:
      return ''.join(ans)

    ans[3] = nextClosest(ans[3], '5')
    if time[3] < ans[3]:
      return ''.join(ans)

    ans[1] = nextClosest(ans[1], '3' if ans[0] == '2' else '9')
    if time[1] < ans[1]:
      return ''.join(ans)

    ans[0] = nextClosest(ans[0], '2')
    return ''.join(ans)
```


```
new Solution().nextClosestTime()
```


---
**Score: 5**