---
title: 98-Validate-Binary-Search-Tree
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/validate-binary-search-tree


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
  def isValidBST(self, root: Optional[TreeNode]) -> bool:
    def isValidBST(root: Optional[TreeNode],
                   minNode: Optional[TreeNode], maxNode: Optional[TreeNode]) -> bool:
      if not root:
        return True
      if minNode and root.val <= minNode.val:
        return False
      if maxNode and root.val >= maxNode.val:
        return False

      return isValidBST(root.left, minNode, root) and \
          isValidBST(root.right, root, maxNode)

    return isValidBST(root, None, None)
```


```
new Solution().isValidBST()
```


---
**Score: 5**