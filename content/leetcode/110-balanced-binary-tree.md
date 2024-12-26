---
title: 110-Balanced-Binary-Tree
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/balanced-binary-tree


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
  def isBalanced(self, root: Optional[TreeNode]) -> bool:
    if not root:
      return True

    def maxDepth(root: Optional[TreeNode]) -> int:
      if not root:
        return 0
      return 1 + max(maxDepth(root.left), maxDepth(root.right))

    return abs(maxDepth(root.left) - maxDepth(root.right)) <= 1 and \
        self.isBalanced(root.left) and self.isBalanced(root.right)
```


```
new Solution().isBalanced()
```


---
**Score: 5**