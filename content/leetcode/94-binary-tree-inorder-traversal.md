---
title: 94-Binary-Tree-Inorder-Traversal
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/binary-tree-inorder-traversal


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
  def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    ans = []
    stack = []

    while root or stack:
      while root:
        stack.append(root)
        root = root.left
      root = stack.pop()
      ans.append(root.val)
      root = root.right

    return ans
```


```
new Solution().inorderTraversal()
```


---
**Score: 5**