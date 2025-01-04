---
title: 114-Flatten-Binary-Tree-To-Linked-List
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/flatten-binary-tree-to-linked-list


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
  def flatten(self, root: Optional[TreeNode]) -> None:
    if not root:
      return

    self.flatten(root.left)
    self.flatten(root.right)

    left = root.left  # Flattened left
    right = root.right  # Flattened right

    root.left = None
    root.right = left

    # Connect the original right subtree
    # To the end of new right subtree
    rightmost = root
    while rightmost.right:
      rightmost = rightmost.right
    rightmost.right = right
```


```
new Solution().flatten()
```


---
**Score: 5**