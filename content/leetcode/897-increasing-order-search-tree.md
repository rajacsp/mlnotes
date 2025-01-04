---
title: 897-Increasing-Order-Search-Tree
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/increasing-order-search-tree


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
  def increasingBST(self, root: TreeNode, tail: TreeNode = None) -> TreeNode:
    if not root:
      return tail

    res = self.increasingBST(root.left, root)
    root.left = None
    root.right = self.increasingBST(root.right, tail)
    return res
```


```
new Solution().increasingBST()
```


---
**Score: 5**