---
title: 156-Binary-Tree-Upside-Down
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/binary-tree-upside-down


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
  def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root or not root.left:
      return root

    newRoot = self.upsideDownBinaryTree(root.left)
    root.left.left = root.right  # 2's left = 3 (root's right)
    root.left.right = root  # 2's right = 1 (root)
    root.left = None
    root.right = None
    return newRoot
```


```
new Solution().upsideDownBinaryTree()
```


---
**Score: 5**