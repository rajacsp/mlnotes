---
title: 272-Closest-Binary-Search-Tree-Value-Ii
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/closest-binary-search-tree-value-ii


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
  def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
    q = deque()

    def inorder(root: Optional[TreeNode]) -> None:
      if not root:
        return

      inorder(root.left)
      q.append(root.val)
      inorder(root.right)

    inorder(root)

    while len(q) > k:
      if abs(q[0] - target) > abs(q[-1] - target):
        q.popleft()
      else:
        q.pop()

    return list(q)
```


```
new Solution().closestKValues()
```


---
**Score: 5**