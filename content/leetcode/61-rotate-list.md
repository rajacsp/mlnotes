---
title: 61-Rotate-List
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/rotate-list


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
  def rotateRight(self, head: ListNode, k: int) -> ListNode:
    if not head or not head.next or k == 0:
      return head

    tail = head
    length = 1
    while tail.next:
      tail = tail.next
      length += 1
    tail.next = head  # Circle the list

    t = length - k % length
    for _ in range(t):
      tail = tail.next
    newHead = tail.next
    tail.next = None

    return newHead
```


```
new Solution().rotateRight()
```


---
**Score: 5**