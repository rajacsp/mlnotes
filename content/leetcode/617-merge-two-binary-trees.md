---
title: 617-Merge-Two-Binary-Trees
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/merge-two-binary-trees


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
  def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root1 and not root2:
      return None
    val = (root1.val if root1 else 0) + (root2.val if root2 else 0)
    root = TreeNode(val)
    root.left = self.mergeTrees(root1.left if root1 else None,
                                root2.left if root2 else None)
    root.right = self.mergeTrees(root1.right if root1 else None,
                                 root2.right if root2 else None)
    return root
```


```
new Solution().mergeTrees()
```


---
**Score: 5**