---
title: 107-Binary-Tree-Level-Order-Traversal-Ii
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/binary-tree-level-order-traversal-ii


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
  def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
      return []

    ans = []
    q = deque([root])

    while q:
      currLevel = []
      for _ in range(len(q)):
        node = q.popleft()
        currLevel.append(node.val)
        if node.left:
          q.append(node.left)
        if node.right:
          q.append(node.right)
      ans.append(currLevel)

    return ans[::-1]
```


```
new Solution().levelOrderBottom()
```


---
**Score: 5**