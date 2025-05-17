---
title: 101-Symmetric-Tree
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/symmetric-tree


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
  def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    def isSymmetric(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
      if not p or not q:
        return p == q

      return p.val == q.val and \
          isSymmetric(p.left, q.right) and \
          isSymmetric(p.right, q.left)

    return isSymmetric(root, root)
```


```
new Solution().isSymmetric()
```


---
**Score: 5**