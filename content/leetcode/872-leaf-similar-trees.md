---
title: 872-Leaf-Similar-Trees
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/leaf-similar-trees


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
  def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    def dfs(root: Optional[TreeNode]) -> None:
      if not root:
        return
      if not root.left and not root.right:
        yield root.val
        return

      yield from dfs(root.left)
      yield from dfs(root.right)

    return list(dfs(root1)) == list(dfs(root2))
```


```
new Solution().leafSimilar()
```


---
**Score: 5**