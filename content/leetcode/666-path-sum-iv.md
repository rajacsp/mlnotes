---
title: 666-Path-Sum-Iv
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/path-sum-iv


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
  def pathSum(self, nums: List[int]) -> int:
    ans = 0
    tree = [[-1] * 8 for _ in range(4)]

    for num in nums:
      d = num // 100 - 1
      p = (num % 100) // 10 - 1
      v = num % 10
      tree[d][p] = v

    def dfs(i: int, j: int, path: int) -> None:
      nonlocal ans
      if tree[i][j] == -1:
        return
      if i == 3 or max(tree[i + 1][j * 2], tree[i + 1][j * 2 + 1]) == -1:
        ans += path + tree[i][j]
        return

      dfs(i + 1, j * 2, path + tree[i][j])
      dfs(i + 1, j * 2 + 1, path + tree[i][j])

    dfs(0, 0, 0)
    return ans
```


```
new Solution().pathSum()
```


---
**Score: 5**