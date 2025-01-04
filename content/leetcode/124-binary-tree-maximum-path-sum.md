---
title: 124-Binary-Tree-Maximum-Path-Sum
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/binary-tree-maximum-path-sum


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
  def maxPathSum(self, root: Optional[TreeNode]) -> int:
    ans = -math.inf

    def maxPathSumDownFrom(root: Optional[TreeNode]) -> int:
      nonlocal ans
      if not root:
        return 0

      l = max(0, maxPathSumDownFrom(root.left))
      r = max(0, maxPathSumDownFrom(root.right))
      ans = max(ans, root.val + l + r)
      return root.val + max(l, r)

    maxPathSumDownFrom(root)
    return ans
```


```
new Solution().maxPathSum()
```


---
**Score: 5**