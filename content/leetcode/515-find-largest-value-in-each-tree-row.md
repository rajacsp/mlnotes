---
title: 515-Find-Largest-Value-In-Each-Tree-Row
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/find-largest-value-in-each-tree-row


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
  def largestValues(self, root: Optional[TreeNode]) -> List[int]:
    if not root:
      return []

    ans = []
    q = deque([root])

    while q:
      maxi = -math.inf
      for _ in range(len(q)):
        root = q.popleft()
        maxi = max(maxi, root.val)
        if root.left:
          q.append(root.left)
        if root.right:
          q.append(root.right)
      ans.append(maxi)

    return ans
```


```
new Solution().largestValues()
```


---
**Score: 5**