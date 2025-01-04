---
title: 199-Binary-Tree-Right-Side-View
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/binary-tree-right-side-view


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
  def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    if not root:
      return []

    ans = []
    q = deque([root])

    while q:
      size = len(q)
      for i in range(size):
        root = q.popleft()
        if i == size - 1:
          ans.append(root.val)
        if root.left:
          q.append(root.left)
        if root.right:
          q.append(root.right)

    return ans
```


```
new Solution().rightSideView()
```


---
**Score: 5**