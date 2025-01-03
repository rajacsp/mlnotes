---
title: 222-Count-Complete-Tree-Nodes
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/count-complete-tree-nodes


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
  def countNodes(self, root: Optional[TreeNode]) -> int:
    if not root:
      return 0
    return 1 + self.countNodes(root.left) + self.countNodes(root.right)
```


```
new Solution().countNodes()
```


---
**Score: 5**