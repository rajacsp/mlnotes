---
title: 337-House-Robber-Iii
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/house-robber-iii


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
  def rob(self, root: Optional[TreeNode]) -> int:
    def robOrNot(root: Optional[TreeNode]) -> tuple:
      if not root:
        return (0, 0)

      robLeft, notRobLeft = robOrNot(root.left)
      robRight, notRobRight = robOrNot(root.right)

      return (root.val + notRobLeft + notRobRight,
              max(robLeft, notRobLeft) + max(robRight, notRobRight))

    return max(robOrNot(root))
```


```
new Solution().rob()
```


---
**Score: 5**