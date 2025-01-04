---
title: 862-Shortest-Subarray-With-Sum-At-Least-K
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k


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
  def shortestSubarray(self, A: List[int], K: int) -> int:
    n = len(A)
    ans = n + 1
    q = deque()
    prefix = [0] + list(itertools.accumulate(A))

    for i in range(n + 1):
      while q and prefix[i] - prefix[q[0]] >= K:
        ans = min(ans, i - q.popleft())
      while q and prefix[i] <= prefix[q[-1]]:
        q.pop()
      q.append(i)

    return ans if ans <= n else -1
```


```
new Solution().shortestSubarray()
```


---
**Score: 5**