---
title: 1019-Next-Greater-Node-In-Linked-List
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/next-greater-node-in-linked-list


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
  def nextLargerNodes(self, head: ListNode) -> List[int]:
    ans = []
    stack = []

    while head:
      while stack and head.val > ans[stack[-1]]:
        index = stack.pop()
        ans[index] = head.val
      stack.append(len(ans))
      ans.append(head.val)
      head = head.next

    for i in stack:
      ans[i] = 0

    return ans
```


```
new Solution().nextLargerNodes()
```


---
**Score: 5**