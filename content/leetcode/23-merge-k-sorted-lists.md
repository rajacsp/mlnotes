---
title: 23-Merge-K-Sorted-Lists
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/merge-k-sorted-lists


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
from queue import PriorityQueue


class Solution:
  def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    dummy = ListNode(0)
    curr = dummy
    pq = PriorityQueue()

    for i, lst in enumerate(lists):
      if lst:
        pq.put((lst.val, i, lst))

    while not pq.empty():
      _, i, minNode = pq.get()
      if minNode.next:
        pq.put((minNode.next.val, i, minNode.next))
      curr.next = minNode
      curr = curr.next

    return dummy.next
```


```
new Solution().mergeKLists()
```


---
**Score: 5**