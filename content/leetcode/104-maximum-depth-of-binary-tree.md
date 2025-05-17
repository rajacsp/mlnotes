---
title: 104-Maximum-Depth-Of-Binary-Tree
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/maximum-depth-of-binary-tree


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
  def maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
      return 0
    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
```


```
new Solution().maxDepth()
```


---
**Score: 5**