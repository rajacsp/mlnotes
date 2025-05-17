---
title: 86-Partition-List
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/partition-list


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
  def partition(self, head: ListNode, x: int) -> ListNode:
    beforeHead = ListNode(0)
    afterHead = ListNode(0)
    before = beforeHead
    after = afterHead

    while head:
      if head.val < x:
        before.next = head
        before = head
      else:
        after.next = head
        after = head
      head = head.next

    after.next = None
    before.next = afterHead.next

    return beforeHead.next
```


```
new Solution().partition()
```


---
**Score: 5**