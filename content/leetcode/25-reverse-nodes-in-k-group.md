---
title: 25-Reverse-Nodes-In-K-Group
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/reverse-nodes-in-k-group


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
  def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if not head:
      return None

    tail = head

    for _ in range(k):
      if not tail:  # Less than k nodes, do nothing
        return head
      tail = tail.next

    newHead = self._reverse(head, tail)
    head.next = self.reverseKGroup(tail, k)
    return newHead

  # Reverses [head, tail)
  def _reverse(self, head: Optional[ListNode], tail: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    curr = head

    while curr != tail:
      next = curr.next
      curr.next = prev
      prev = curr
      curr = next

    return prev
```


```
new Solution().reverseKGroup()
```


---
**Score: 5**