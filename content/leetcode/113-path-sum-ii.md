---
title: 113-Path-Sum-Ii
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/path-sum-ii


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
  def pathSum(self, root: TreeNode, summ: int) -> List[List[int]]:
    ans = []

    def dfs(root: TreeNode, summ: int, path: List[int]) -> None:
      if not root:
        return
      if root.val == summ and not root.left and not root.right:
        ans.append(path + [root.val])
        return

      dfs(root.left, summ - root.val, path + [root.val])
      dfs(root.right, summ - root.val, path + [root.val])

    dfs(root, summ, [])
    return ans
```


```
new Solution().pathSum()
```


---
**Score: 5**