---
title: 465-Optimal-Account-Balancing
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/optimal-account-balancing


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
  def minTransfers(self, transactions: List[List[int]]) -> int:
    balance = [0] * 21

    for u, v, amount in transactions:
      balance[u] -= amount
      balance[v] += amount

    debt = [b for b in balance if b]

    def dfs(s: int) -> int:
      while s < len(debt) and not debt[s]:
        s += 1
      if s == len(debt):
        return 0

      ans = math.inf

      for i in range(s + 1, len(debt)):
        if debt[i] * debt[s] < 0:
          debt[i] += debt[s]  # debt[s] is settled
          ans = min(ans, 1 + dfs(s + 1))
          debt[i] -= debt[s]  # Backtrack

      return ans

    return dfs(0)
```


```
new Solution().minTransfers()
```


---
**Score: 5**