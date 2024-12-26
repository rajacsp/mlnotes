---
title: 328-Odd-Even-Linked-List
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/odd-even-linked-list


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
  def oddEvenList(self, head: ListNode) -> ListNode:
    oddHead = ListNode(0)
    evenHead = ListNode(0)
    odd = oddHead
    even = evenHead
    isOdd = True

    while head:
      if isOdd:
        odd.next = head
        odd = head
      else:
        even.next = head
        even = head
      head = head.next
      isOdd = not isOdd

    even.next = None
    odd.next = evenHead.next
    return oddHead.next
```


```
new Solution().oddEvenList()
```


---
**Score: 5**