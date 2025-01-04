---
title: 142-Linked-List-Cycle-Ii
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/linked-list-cycle-ii


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
  def detectCycle(self, head: ListNode) -> ListNode:
    slow = head
    fast = head

    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
      if slow == fast:
        slow = head
        while slow != fast:
          slow = slow.next
          fast = fast.next
        return slow

    return None
```


```
new Solution().detectCycle()
```


---
**Score: 5**