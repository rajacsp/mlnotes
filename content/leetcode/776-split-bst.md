---
title: 776-Split-Bst
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/split-bst


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
  def splitBST(self, root: Optional[TreeNode], target: int) -> List[Optional[TreeNode]]:
    if not root:
      return None, None
    if root.val > target:
      left, right = self.splitBST(root.left, target)
      root.left = right
      return left, root
    else:  # Root.val <= target
      left, right = self.splitBST(root.right, target)
      root.right = left
      return root, right
```


```
new Solution().splitBST()
```


---
**Score: 5**