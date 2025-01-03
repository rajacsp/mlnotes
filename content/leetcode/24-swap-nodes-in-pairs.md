---
title: 24-Swap-Nodes-In-Pairs
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/swap-nodes-in-pairs


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
  def swapPairs(self, head: ListNode) -> ListNode:
    def getLength(head: ListNode) -> int:
      length = 0
      while head:
        length += 1
        head = head.next
      return length

    length = getLength(head)
    dummy = ListNode(0, head)
    prev = dummy
    curr = head

    for _ in range(length // 2):
      next = curr.next
      curr.next = next.next
      next.next = prev.next
      prev.next = next
      prev = curr
      curr = curr.next

    return dummy.next
```


```
new Solution().swapPairs()
```


---
**Score: 5**