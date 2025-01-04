---
title: 144-Binary-Tree-Preorder-Traversal
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/binary-tree-preorder-traversal


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
  def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    ans = []

    def preorder(root: Optional[TreeNode]) -> None:
      if not root:
        return

      ans.append(root.val)
      preorder(root.left)
      preorder(root.right)

    preorder(root)
    return ans
```


```
new Solution().preorderTraversal()
```


---
**Score: 5**