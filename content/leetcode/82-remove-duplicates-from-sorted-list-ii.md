---
title: 82-Remove-Duplicates-From-Sorted-List-Ii
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii


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
  def deleteDuplicates(self, head: ListNode) -> ListNode:
    dummy = ListNode(0, head)
    prev = dummy

    while head:
      while head.next and head.val == head.next.val:
        head = head.next
      if prev.next == head:
        prev = prev.next
      else:
        prev.next = head.next
      head = head.next

    return dummy.next
```


```
new Solution().deleteDuplicates()
```


---
**Score: 5**