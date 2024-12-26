---
title: 445-Add-Two-Numbers-Ii
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/add-two-numbers-ii


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
  def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    stack1 = []
    stack2 = []

    while l1:
      stack1.append(l1)
      l1 = l1.next

    while l2:
      stack2.append(l2)
      l2 = l2.next

    head = None
    carry = 0

    while carry or stack1 or stack2:
      if stack1:
        carry += stack1.pop().val
      if stack2:
        carry += stack2.pop().val
      node = ListNode(carry % 10)
      node.next = head
      head = node
      carry //= 10

    return head
```


```
new Solution().addTwoNumbers()
```


---
**Score: 5**