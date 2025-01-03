---
title: 129-Sum-Root-To-Leaf-Numbers
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/sum-root-to-leaf-numbers


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
  def sumNumbers(self, root: Optional[TreeNode]) -> int:
    ans = 0

    def dfs(root: Optional[TreeNode], path: int) -> None:
      nonlocal ans
      if not root:
        return
      if not root.left and not root.right:
        ans += path * 10 + root.val
        return

      dfs(root.left, path * 10 + root.val)
      dfs(root.right, path * 10 + root.val)

    dfs(root, 0)
    return ans
```


```
new Solution().sumNumbers()
```


---
**Score: 5**