---
title: 700-Search-In-A-Binary-Search-Tree
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/search-in-a-binary-search-tree


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
  def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if not root:
      return None
    if root.val == val:
      return root
    if root.val > val:
      return self.searchBST(root.left, val)
    return self.searchBST(root.right, val)
```


```
new Solution().searchBST()
```


---
**Score: 5**