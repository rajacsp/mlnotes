---
title: 250-Count-Univalue-Subtrees
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/count-univalue-subtrees


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
  def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
    ans = 0

    def isUnival(root: Optional[TreeNode], val: int) -> bool:
      nonlocal ans
      if not root:
        return True

      if isUnival(root.left, root.val) & isUnival(root.right, root.val):
        ans += 1
        return root.val == val

      return False

    isUnival(root, math.inf)
    return ans
```


```
new Solution().countUnivalSubtrees()
```


---
**Score: 5**