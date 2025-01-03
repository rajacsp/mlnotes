---
title: 687-Longest-Univalue-Path
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/longest-univalue-path


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
  def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
    ans = 0

    def longestUnivaluePathDownFrom(root: Optional[TreeNode]) -> int:
      nonlocal ans
      if not root:
        return 0

      l = longestUnivaluePathDownFrom(root.left)
      r = longestUnivaluePathDownFrom(root.right)
      arrowLeft = l + 1 if root.left and root.left.val == root.val else 0
      arrowRight = r + 1 if root.right and root.right.val == root.val else 0
      ans = max(ans, arrowLeft + arrowRight)
      return max(arrowLeft, arrowRight)

    longestUnivaluePathDownFrom(root)
    return ans
```


```
new Solution().longestUnivaluePath()
```


---
**Score: 5**