---
title: 112-Path-Sum
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/path-sum


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
  def hasPathSum(self, root: TreeNode, summ: int) -> bool:
    if not root:
      return False
    if root.val == summ and not root.left and not root.right:
      return True
    return self.hasPathSum(root.left, summ - root.val) or \
        self.hasPathSum(root.right, summ - root.val)
```


```
new Solution().hasPathSum()
```


---
**Score: 5**