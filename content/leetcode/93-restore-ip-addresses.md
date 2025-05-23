---
title: 93-Restore-Ip-Addresses
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/restore-ip-addresses


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
  def restoreIpAddresses(self, s: str) -> List[str]:
    ans = []

    def dfs(start: int, path: List[int]) -> None:
      if len(path) == 4 and start == len(s):
        ans.append(path[0] + '.' + path[1] + '.' + path[2] + '.' + path[3])
        return
      if len(path) == 4 or start == len(s):
        return

      for length in range(1, 4):
        if start + length > len(s):
          return  # Out of bound
        if length > 1 and s[start] == '0':
          return  # Leading '0'
        num = s[start: start + length]
        if int(num) > 255:
          return
        dfs(start + length, path + [num])

    dfs(0, [])
    return ans
```


```
new Solution().restoreIpAddresses()
```


---
**Score: 5**