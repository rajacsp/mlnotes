---
title: 298-Binary-Tree-Longest-Consecutive-Sequence
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/binary-tree-longest-consecutive-sequence


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
  def longestConsecutive(self, root: Optional[TreeNode]) -> int:
    if not root:
      return 0

    def dfs(root: Optional[TreeNode], target: int, length: int, maxLength: int) -> int:
      if not root:
        return maxLength
      if root.val == target:
        length += 1
        maxLength = max(maxLength, length)
      else:
        length = 1
      return max(dfs(root.left, root.val + 1, length, maxLength),
                 dfs(root.right, root.val + 1, length, maxLength))

    return dfs(root, root.val, 0, 0)
```


```
new Solution().longestConsecutive()
```


---
**Score: 5**