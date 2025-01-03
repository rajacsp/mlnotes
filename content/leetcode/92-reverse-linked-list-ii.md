---
title: 92-Reverse-Linked-List-Ii
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/reverse-linked-list-ii


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
  def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    if left == 1:
      return self.reverseN(head, right)

    head.next = self.reverseBetween(head.next, left - 1, right - 1)
    return head

  def reverseN(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    if n == 1:
      return head

    newHead = self.reverseN(head.next, n - 1)
    headNext = head.next
    head.next = headNext.next
    headNext.next = head
    return newHead
```


```
new Solution().reverseBetween()
```


---
**Score: 5**