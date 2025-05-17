---
title: 508-Most-Frequent-Subtree-Sum
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/most-frequent-subtree-sum


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
  def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
    if not root:
      return []

    count = Counter()

    def dfs(root: Optional[TreeNode]) -> int:
      if not root:
        return 0

      summ = root.val + dfs(root.left) + dfs(root.right)
      count[summ] += 1
      return summ

    dfs(root)
    maxFreq = max(count.values())
    return [summ for summ in count if count[summ] == maxFreq]
```


```
new Solution().findFrequentTreeSum()
```


---
**Score: 5**