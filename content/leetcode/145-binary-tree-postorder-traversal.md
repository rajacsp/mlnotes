---
title: 145-Binary-Tree-Postorder-Traversal
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/binary-tree-postorder-traversal


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
  def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    ans = []

    def postorder(root: Optional[TreeNode]) -> None:
      if not root:
        return

      postorder(root.left)
      postorder(root.right)
      ans.append(root.val)

    postorder(root)
    return ans
```


```
new Solution().postorderTraversal()
```


---
**Score: 5**