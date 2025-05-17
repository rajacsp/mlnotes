---
title: 83-Remove-Duplicates-From-Sorted-List
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/remove-duplicates-from-sorted-list


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
    curr = head

    while curr:
      while curr.next and curr.val == curr.next.val:
        curr.next = curr.next.next
      curr = curr.next

    return head
```


```
new Solution().deleteDuplicates()
```


---
**Score: 5**