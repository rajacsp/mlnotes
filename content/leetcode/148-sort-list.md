---
title: 148-Sort-List
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/sort-list


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
  def sortList(self, head: ListNode) -> ListNode:
    def split(head: ListNode, k: int) -> ListNode:
      while k > 1 and head:
        head = head.next
        k -= 1
      rest = head.next if head else None
      if head:
        head.next = None
      return rest

    def merge(l1: ListNode, l2: ListNode) -> tuple:
      dummy = ListNode(0)
      tail = dummy

      while l1 and l2:
        if l1.val > l2.val:
          l1, l2 = l2, l1
        tail.next = l1
        l1 = l1.next
        tail = tail.next
      tail.next = l1 if l1 else l2
      while tail.next:
        tail = tail.next

      return dummy.next, tail

    length = 0
    curr = head
    while curr:
      length += 1
      curr = curr.next

    dummy = ListNode(0, head)

    k = 1
    while k < length:
      curr = dummy.next
      tail = dummy
      while curr:
        l = curr
        r = split(l, k)
        curr = split(r, k)
        mergedHead, mergedTail = merge(l, r)
        tail.next = mergedHead
        tail = mergedTail
      k *= 2

    return dummy.next
```


```
new Solution().sortList()
```


---
**Score: 5**