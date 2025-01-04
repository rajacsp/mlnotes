---
title: 654-Maximum-Binary-Tree
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/maximum-binary-tree


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
  def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
    def build(i: int, j: int) -> Optional[TreeNode]:
      if i > j:
        return None

      maxNum = max(nums[i:j + 1])
      maxIndex = nums.index(maxNum)

      root = TreeNode(maxNum)
      root.left = build(i, maxIndex - 1)
      root.right = build(maxIndex + 1, j)
      return root

    return build(0, len(nums) - 1)
```


```
new Solution().constructMaximumBinaryTree()
```


---
**Score: 5**