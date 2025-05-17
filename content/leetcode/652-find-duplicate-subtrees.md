---
title: 652-Find-Duplicate-Subtrees
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/find-duplicate-subtrees


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
  def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
    ans = []
    count = Counter()

    def encode(root: Optional[TreeNode]) -> str:
      if not root:
        return ''

      encoded = str(root.val) + '#' + \
          encode(root.left) + '#' + \
          encode(root.right)
      count[encoded] += 1
      if count[encoded] == 2:
        ans.append(root)
      return encoded

    encode(root)
    return ans
```


```
new Solution().findDuplicateSubtrees()
```


---
**Score: 5**