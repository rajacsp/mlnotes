---
title: 147-Insertion-Sort-List
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/insertion-sort-list


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
  def insertionSortList(self, head: ListNode) -> ListNode:
    dummy = ListNode(0)
    curr = head

    while curr:
      prev = dummy
      while prev.next and prev.next.val < curr.val:
        prev = prev.next
      next = curr.next
      curr.next = prev.next
      prev.next = curr
      curr = next

    return dummy.next
```


```
new Solution().insertionSortList()
```


---
**Score: 5**