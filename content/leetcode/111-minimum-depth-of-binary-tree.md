---
title: 111-Minimum-Depth-Of-Binary-Tree
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/minimum-depth-of-binary-tree


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
  def minDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
      return 0
    if not root.left:
      return self.minDepth(root.right) + 1
    if not root.right:
      return self.minDepth(root.left) + 1
    return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
```


```
new Solution().minDepth()
```


---
**Score: 5**