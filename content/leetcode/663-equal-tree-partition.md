---
title: 663-Equal-Tree-Partition
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/equal-tree-partition


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
  def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
    if not root:
      return False

    seen = set()

    def dfs(root: Optional[TreeNode]) -> int:
      if not root:
        return 0

      summ = root.val + dfs(root.left) + dfs(root.right)
      seen.add(summ)
      return summ

    summ = root.val + dfs(root.left) + dfs(root.right)
    return summ % 2 == 0 and summ // 2 in seen
```


```
new Solution().checkEqualTree()
```


---
**Score: 5**