---
title: 998-Maximum-Binary-Tree-Ii
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/maximum-binary-tree-ii


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
  def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if not root:
      return TreeNode(val)
    if root.val < val:
      return TreeNode(val, root, None)
    root.right = self.insertIntoMaxTree(root.right, val)
    return root
```


```
new Solution().insertIntoMaxTree()
```


---
**Score: 5**