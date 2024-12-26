---
title: 234-Palindrome-Linked-List
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/palindrome-linked-list


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
  def isPalindrome(self, head: ListNode) -> bool:
    def reverseList(head: ListNode) -> ListNode:
      prev = None
      curr = head

      while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

      return prev

    slow = head
    fast = head

    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next

    if fast:
      slow = slow.next
    slow = reverseList(slow)

    while slow:
      if slow.val != head.val:
        return False
      slow = slow.next
      head = head.next

    return True
```


```
new Solution().isPalindrome()
```


---
**Score: 5**