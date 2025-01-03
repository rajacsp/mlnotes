---
title: 226-Invert-Binary-Tree
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/invert-binary-tree


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
  def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
      return None

    left = root.left
    right = root.right
    root.left = self.invertTree(right)
    root.right = self.invertTree(left)
    return root
```


```
new Solution().invertTree()
```


---
**Score: 5**