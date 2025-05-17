---
title: 513-Find-Bottom-Left-Tree-Value
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/find-bottom-left-tree-value


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
  def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
    q = deque([root])

    while q:
      root = q.popleft()
      if root.right:
        q.append(root.right)
      if root.left:
        q.append(root.left)

    return root.val
```


```
new Solution().findBottomLeftValue()
```


---
**Score: 5**