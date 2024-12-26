---
title: 19-Remove-Nth-Node-From-End-Of-List
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/remove-nth-node-from-end-of-list


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
  def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    slow = head
    fast = head

    for _ in range(n):
      fast = fast.next
    if not fast:
      return head.next

    while fast.next:
      slow = slow.next
      fast = fast.next
    slow.next = slow.next.next

    return head
```


```
new Solution().removeNthFromEnd()
```


---
**Score: 5**