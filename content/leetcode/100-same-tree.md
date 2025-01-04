---
title: 100-Same-Tree
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/same-tree


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
  def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p or not q:
      return p == q
    return p.val == q.val and \
        self.isSameTree(p.left, q.left) and \
        self.isSameTree(p.right, q.right)
```


```
new Solution().isSameTree()
```


---
**Score: 5**