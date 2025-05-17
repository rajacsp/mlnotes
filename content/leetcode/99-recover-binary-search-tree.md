---
title: 99-Recover-Binary-Search-Tree
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/recover-binary-search-tree


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
  def recoverTree(self, root: Optional[TreeNode]) -> None:
    def swap(x: Optional[TreeNode], y: Optional[TreeNode]) -> None:
      temp = x.val
      x.val = y.val
      y.val = temp

    def inorder(root: Optional[TreeNode]) -> None:
      if not root:
        return

      inorder(root.left)

      if self.pred and root.val < self.pred.val:
        self.y = root
        if not self.x:
          self.x = self.pred
        else:
          return
      self.pred = root

      inorder(root.right)

    inorder(root)
    swap(self.x, self.y)

  pred = None
  x = None  # 1st wrong node
  y = None  # 2nd wrong node
```


```
new Solution().recoverTree()
```


---
**Score: 5**