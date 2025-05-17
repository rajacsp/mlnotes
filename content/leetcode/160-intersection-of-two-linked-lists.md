---
title: 160-Intersection-Of-Two-Linked-Lists
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/intersection-of-two-linked-lists


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
  def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    a = headA
    b = headB

    while a != b:
      a = a.next if a else headB
      b = b.next if b else headA

    return a
```


```
new Solution().getIntersectionNode()
```


---
**Score: 5**