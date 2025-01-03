---
title: 257-Binary-Tree-Paths
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/binary-tree-paths


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
  def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
    ans = []

    def dfs(root: Optional[TreeNode], path: List[str]) -> None:
      if not root:
        return
      if not root.left and not root.right:
        ans.append(''.join(path) + str(root.val))
        return

      path.append(str(root.val) + '->')
      dfs(root.left, path)
      dfs(root.right, path)
      path.pop()

    dfs(root, [])
    return ans
```


```
new Solution().binaryTreePaths()
```


---
**Score: 5**