---
title: 606-Construct-String-From-Binary-Tree
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/construct-string-from-binary-tree


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
  def tree2str(self, t: Optional[TreeNode]) -> str:
    def dfs(root: Optional[TreeNode]) -> str:
      if not root:
        return ''
      if root.right:
        return str(root.val) + '(' + dfs(root.left) + ')(' + dfs(root.right) + ')'
      if root.left:
        return str(root.val) + '(' + dfs(root.left) + ')'
      return str(root.val)
    return dfs(t)
```


```
new Solution().tree2str()
```


---
**Score: 5**