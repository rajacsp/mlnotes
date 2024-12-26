---
title: 108-Convert-Sorted-Array-To-Binary-Search-Tree
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree


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
  def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
    def build(l: int, r: int) -> Optional[TreeNode]:
      if l > r:
        return None

      m = (l + r) // 2
      return TreeNode(nums[m],
                      build(l, m - 1),
                      build(m + 1, r))

    return build(0, len(nums) - 1)
```


```
new Solution().sortedArrayToBST()
```


---
**Score: 5**