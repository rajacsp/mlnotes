---
title: 230-Kth-Smallest-Element-In-A-Bst
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/kth-smallest-element-in-a-bst


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
  def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    def countNodes(root: Optional[TreeNode]) -> int:
      if not root:
        return 0
      return 1 + countNodes(root.left) + countNodes(root.right)

    leftCount = countNodes(root.left)

    if leftCount == k - 1:
      return root.val
    if leftCount >= k:
      return self.kthSmallest(root.left, k)
    return self.kthSmallest(root.right, k - 1 - leftCount)  # LeftCount < k
```


```
new Solution().kthSmallest()
```


---
**Score: 5**