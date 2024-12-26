---
title: 543-Diameter-Of-Binary-Tree
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/diameter-of-binary-tree


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
  def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    ans = 0

    def maxDepth(root: Optional[TreeNode]) -> int:
      nonlocal ans
      if not root:
        return 0

      l = maxDepth(root.left)
      r = maxDepth(root.right)
      ans = max(ans, l + r)
      return 1 + max(l, r)

    maxDepth(root)
    return ans
```


```
new Solution().diameterOfBinaryTree()
```


---
**Score: 5**