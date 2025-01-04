---
title: 538-Convert-Bst-To-Greater-Tree
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/convert-bst-to-greater-tree


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
  def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    prefix = 0

    def reversedInorder(root: Optional[TreeNode]) -> None:
      nonlocal prefix
      if not root:
        return

      reversedInorder(root.right)
      prefix += root.val
      root.val = prefix
      reversedInorder(root.left)

    reversedInorder(root)
    return root
```


```
new Solution().convertBST()
```


---
**Score: 5**