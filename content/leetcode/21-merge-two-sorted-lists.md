---
title: 21-Merge-Two-Sorted-Lists
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/merge-two-sorted-lists


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
  def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if not list1 or not list2:
      return list1 if list1 else list2
    if list1.val > list2.val:
      list1, list2 = list2, list1
    list1.next = self.mergeTwoLists(list1.next, list2)
    return list1
```


```
new Solution().mergeTwoLists()
```


---
**Score: 5**