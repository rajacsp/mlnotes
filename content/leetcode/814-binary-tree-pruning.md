---
title: 814-Binary-Tree-Pruning
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/binary-tree-pruning


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
  def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
      return None
    root.left = self.pruneTree(root.left)
    root.right = self.pruneTree(root.right)
    if not root.left and not root.right and not root.val:
      return None
    return root
```


```
new Solution().pruneTree()
```


---
**Score: 5**