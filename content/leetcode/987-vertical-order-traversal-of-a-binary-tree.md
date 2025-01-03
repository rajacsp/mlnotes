---
title: 987-Vertical-Order-Traversal-Of-A-Binary-Tree
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree


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
  def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
    ans = []
    xToNodes = defaultdict(list)

    def dfs(node: Optional[TreeNode], x: int, y: int) -> None:
      if not node:
        return

      xToNodes[x].append((-y, node.val))
      dfs(node.left, x - 1, y - 1)
      dfs(node.right, x + 1, y - 1)

    dfs(root, 0, 0)

    for _, nodes in sorted(xToNodes.items(), key=lambda item: item[0]):
      ans.append([val for _, val in sorted(nodes)])

    return ans
```


```
new Solution().verticalTraversal()
```


---
**Score: 5**