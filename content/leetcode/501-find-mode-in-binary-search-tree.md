---
title: 501-Find-Mode-In-Binary-Search-Tree
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/find-mode-in-binary-search-tree


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
  def findMode(self, root: Optional[TreeNode]) -> List[int]:
    self.ans = []
    self.pred = None
    self.count = 0
    self.maxCount = 0

    def updateCount(root: Optional[TreeNode]) -> None:
      if self.pred and self.pred.val == root.val:
        self.count += 1
      else:
        self.count = 1

      if self.count > self.maxCount:
        self.maxCount = self.count
        self.ans = [root.val]
      elif self.count == self.maxCount:
        self.ans.append(root.val)

      self.pred = root

    def inorder(root: Optional[TreeNode]) -> None:
      if not root:
        return

      inorder(root.left)
      updateCount(root)
      inorder(root.right)

    inorder(root)
    return self.ans
```


```
new Solution().findMode()
```


---
**Score: 5**