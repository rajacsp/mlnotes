---
title: 638-Shopping-Offers
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/shopping-offers


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
  def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
    def dfs(s: int) -> int:
      ans = 0
      for i, need in enumerate(needs):
        ans += need * price[i]

      for i in range(s, len(special)):
        offer = special[i]
        if all(offer[j] <= need for j, need in enumerate(needs)):
          # Use special[i]
          for j in range(len(needs)):
            needs[j] -= offer[j]
          ans = min(ans, offer[-1] + dfs(i))
          # Backtracking - unuse special[i]
          for j in range(len(needs)):
            needs[j] += offer[j]

      return ans

    return dfs(0)
```


```
new Solution().shoppingOffers()
```


---
**Score: 5**