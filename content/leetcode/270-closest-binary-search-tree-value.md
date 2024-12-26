---
title: 270-Closest-Binary-Search-Tree-Value
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/closest-binary-search-tree-value


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
  def closestValue(self, root: Optional[TreeNode], target: float) -> int:
    # If target < root.val, search left subtree
    if target < root.val and root.left:
      left = self.closestValue(root.left, target)
      if abs(left - target) < abs(root.val - target):
        return left

    # If target > root.val, search right subtree
    if target > root.val and root.right:
      right = self.closestValue(root.right, target)
      if abs(right - target) < abs(root.val - target):
        return right

    return root.val
```


```
new Solution().closestValue()
```


---
**Score: 5**