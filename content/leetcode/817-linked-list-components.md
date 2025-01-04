---
title: 817-Linked-List-Components
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/linked-list-components


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
  def numComponents(self, head: ListNode, G: List[int]) -> int:
    ans = 0
    G = set(G)

    while head:
      if head.val in G and (head.next == None or head.next.val not in G):
        ans += 1
      head = head.next

    return ans
```


```
new Solution().numComponents()
```


---
**Score: 5**