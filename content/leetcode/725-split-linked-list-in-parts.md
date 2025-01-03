---
title: 725-Split-Linked-List-In-Parts
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/split-linked-list-in-parts


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
  def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
    ans = [[] for _ in range(k)]
    length = 0
    curr = root
    while curr:
      length += 1
      curr = curr.next
    subLength = length // k
    remainder = length % k

    prev = None
    head = root

    for i in range(k):
      ans[i] = head
      for j in range(subLength + (1 if remainder > 0 else 0)):
        prev = head
        head = head.next
      if prev:
        prev.next = None
      remainder -= 1

    return ans
```


```
new Solution().splitListToParts()
```


---
**Score: 5**