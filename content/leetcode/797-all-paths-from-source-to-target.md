---
title: 797-All-Paths-From-Source-To-Target
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/all-paths-from-source-to-target


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
  def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
    ans = []

    def dfs(u: int, path: List[int]) -> None:
      if u == len(graph) - 1:
        ans.append(path)
        return

      for v in graph[u]:
        dfs(v, path + [v])

    dfs(0, [0])
    return ans
```


```
new Solution().allPathsSourceTarget()
```


---
**Score: 5**