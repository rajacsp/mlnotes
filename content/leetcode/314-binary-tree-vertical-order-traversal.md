---
title: 314-Binary-Tree-Vertical-Order-Traversal
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/binary-tree-vertical-order-traversal


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
  def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
      return []

    range_ = [0] * 2

    def getRange(root: Optional[TreeNode], x: int) -> None:
      if not root:
        return

      range_[0] = min(range_[0], x)
      range_[1] = max(range_[1], x)

      getRange(root.left, x - 1)
      getRange(root.right, x + 1)

    getRange(root, 0)  # Get the leftmost and rightmost x index

    ans = [[] for _ in range(range_[1] - range_[0] + 1)]
    q = deque([(root, -range_[0])])  # (TreeNode, x)

    while q:
      node, x = q.popleft()
      ans[x].append(node.val)
      if node.left:
        q.append((node.left, x - 1))
      if node.right:
        q.append((node.right, x + 1))

    return ans
```


```
new Solution().verticalOrder()
```


---
**Score: 5**