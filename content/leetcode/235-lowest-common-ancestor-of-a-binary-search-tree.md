---
title: 235-Lowest-Common-Ancestor-Of-A-Binary-Search-Tree
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree


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
  def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if root.val > max(p.val, q.val):
      return self.lowestCommonAncestor(root.left, p, q)
    if root.val < min(p.val, q.val):
      return self.lowestCommonAncestor(root.right, p, q)
    return root
```


```
new Solution().lowestCommonAncestor()
```


---
**Score: 5**