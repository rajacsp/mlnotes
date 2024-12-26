---
title: 582-Kill-Process
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/kill-process


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
  def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
    ans = []
    tree = defaultdict(list)

    for v, u in zip(pid, ppid):
      if u == 0:
        continue
      tree[u].append(v)

    def dfs(u: int) -> None:
      ans.append(u)
      for v in tree.get(u, []):
        dfs(v)

    dfs(kill)
    return ans
```


```
new Solution().killProcess()
```


---
**Score: 5**