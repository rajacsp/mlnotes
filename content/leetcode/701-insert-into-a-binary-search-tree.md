---
title: 701-Insert-Into-A-Binary-Search-Tree
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/insert-into-a-binary-search-tree


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
  def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if not root:
      return TreeNode(val)
    if root.val > val:
      root.left = self.insertIntoBST(root.left, val)
    else:
      root.right = self.insertIntoBST(root.right, val)
    return root
```


```
new Solution().insertIntoBST()
```


---
**Score: 5**