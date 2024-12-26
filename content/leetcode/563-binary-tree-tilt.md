---
title: 563-Binary-Tree-Tilt
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/binary-tree-tilt


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
  def findTilt(self, root: Optional[TreeNode]) -> int:
    ans = 0

    def summ(root: Optional[TreeNode]) -> None:
      nonlocal ans
      if not root:
        return 0

      l = summ(root.left)
      r = summ(root.right)
      ans += abs(l - r)
      return root.val + l + r

    summ(root)
    return ans
```


```
new Solution().findTilt()
```


---
**Score: 5**