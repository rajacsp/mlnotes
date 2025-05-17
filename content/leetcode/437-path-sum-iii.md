---
title: 437-Path-Sum-Iii
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/path-sum-iii


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
  def pathSum(self, root: TreeNode, summ: int) -> int:
    if not root:
      return 0

    def dfs(root: TreeNode, summ: int) -> int:
      if not root:
        return 0
      return (summ == root.val) + \
          dfs(root.left, summ - root.val) + \
          dfs(root.right, summ - root.val)

    return dfs(root, summ) + \
        self.pathSum(root.left, summ) + \
        self.pathSum(root.right, summ)
```


```
new Solution().pathSum()
```


---
**Score: 5**