---
title: 876-Middle-Of-The-Linked-List
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/middle-of-the-linked-list


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
  def middleNode(self, head: ListNode) -> ListNode:
    slow = head
    fast = head

    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next

    return slow
```


```
new Solution().middleNode()
```


---
**Score: 5**