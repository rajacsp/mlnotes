---
title: 1008-Construct-Binary-Search-Tree-From-Preorder-Traversal
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal


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
  def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
    root = TreeNode(preorder[0])
    stack = [root]

    for i in range(1, len(preorder)):
      parent = stack[-1]
      child = TreeNode(preorder[i])
      # Adjust parent
      while stack and stack[-1].val < child.val:
        parent = stack.pop()
      # Create parent-child link according to BST property
      if parent.val > child.val:
        parent.left = child
      else:
        parent.right = child
      stack.append(child)

    return root
```


```
new Solution().bstFromPreorder()
```


---
**Score: 5**