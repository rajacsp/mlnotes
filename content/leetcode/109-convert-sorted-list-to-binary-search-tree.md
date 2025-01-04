---
title: 109-Convert-Sorted-List-To-Binary-Search-Tree
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree


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
  def sortedListToBST(self, head: ListNode) -> TreeNode:
    def findMid(head: ListNode) -> ListNode:
      prev = None
      slow = head
      fast = head

      while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
      prev.next = None

      return slow

    if not head:
      return None
    if not head.next:
      return TreeNode(head.val)

    mid = findMid(head)
    root = TreeNode(mid.val)
    root.left = self.sortedListToBST(head)
    root.right = self.sortedListToBST(mid.next)

    return root
```


```
new Solution().sortedListToBST()
```


---
**Score: 5**