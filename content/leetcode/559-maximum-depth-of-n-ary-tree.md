---
title: 559-Maximum-Depth-Of-N-Ary-Tree
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/maximum-depth-of-n-ary-tree


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
  def maxDepth(self, root: 'Node') -> int:
    if not root:
      return 0
    if not root.children:
      return 1
    return 1 + max(self.maxDepth(child) for child in root.children)
```


```
new Solution().maxDepth()
```


---
**Score: 5**