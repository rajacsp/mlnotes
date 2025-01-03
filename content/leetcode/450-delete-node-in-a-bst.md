---
title: 450-Delete-Node-In-A-Bst
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/delete-node-in-a-bst


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
  def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    if not root:
      return None
    if root.val == key:
      if not root.left:
        return root.right
      if not root.right:
        return root.left
      minNode = self._getMin(root.right)
      root.right = self.deleteNode(root.right, minNode.val)
      minNode.left = root.left
      minNode.right = root.right
      root = minNode
    elif root.val < key:
      root.right = self.deleteNode(root.right, key)
    else:  # Root.val > key
      root.left = self.deleteNode(root.left, key)
    return root

  def _getMin(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
    while node.left:
      node = node.left
    return node
```


```
new Solution().deleteNode()
```


---
**Score: 5**