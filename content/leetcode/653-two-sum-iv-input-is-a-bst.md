---
title: 653-Two-Sum-Iv-Input-Is-A-Bst
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/two-sum-iv-input-is-a-bst


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
class BSTIterator:
  def __init__(self, root: Optional[TreeNode], leftToRight: bool):
    self.stack = []
    self.leftToRight = leftToRight
    self.pushUntilNone(root)

  def next(self) -> int:
    node = self.stack.pop()
    if self.leftToRight:
      self.pushUntilNone(node.right)
    else:
      self.pushUntilNone(node.left)
    return node.val

  def pushUntilNone(self, root: Optional[TreeNode]):
    while root:
      self.stack.append(root)
      root = root.left if self.leftToRight else root.right


class Solution:
  def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
    if not root:
      return False

    left = BSTIterator(root, True)
    right = BSTIterator(root, False)

    l = left.next()
    r = right.next()

    while l < r:
      summ = l + r
      if summ == k:
        return True
      if summ < k:
        l = left.next()
      else:
        r = right.next()

    return False
```


```
new Solution().findTarget()
```


---
**Score: 5**