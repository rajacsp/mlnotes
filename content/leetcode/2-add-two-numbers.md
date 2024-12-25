---
title: 2-Add-Two-Numbers
date: 2024-12-25
author: Your Name
cell_count: 9
score: 5
---

```python
# https://leetcode.com/problems/add-two-numbers/description/
```


```python
import pyutil as pyu
pyu.get_local_pyinfo()
```




    'conda env: ml311; pyv: 3.11.10 (main, Oct  3 2024, 07:29:13) [GCC 11.2.0]'




```python
print(pyu.ps2("haystack-ai ollama-haystack python-dotenv"))
```

    haystack-ai==2.8.0
    ollama-haystack is not installed in the current environment.
    python-dotenv==0.21.0
    


You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.


```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```


```python
class Solution:
  def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode(0)
    curr = dummy
    carry = 0

    while carry or l1 or l2:
      if l1:
        carry += l1.val
        l1 = l1.next
      if l2:
        carry += l2.val
        l2 = l2.next
      curr.next = ListNode(carry % 10)
      carry //= 10
      curr = curr.next

    return dummy.next
```


```python

```


```python
def create_linked_list(numbers):
    """Helper function to create a linked list from a list of numbers."""
    dummy = ListNode(0)
    current = dummy
    for num in numbers:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

def print_linked_list(node):
    """Helper function to print a linked list."""
    result = []
    while node:
        result.append(node.val)
        node = node.next
    print(" -> ".join(map(str, result)))

# Test inputs
l1_numbers = [2, 4, 3]  # Represents the number 342
l2_numbers = [5, 6, 4]  # Represents the number 465

# Create linked lists from the test inputs
l1 = create_linked_list(l1_numbers)
l2 = create_linked_list(l2_numbers)

# Solve the problem
solution = Solution()
result = solution.addTwoNumbers(l1, l2)

# Print the result
print("Input List 1:")
print_linked_list(l1)
print("Input List 2:")
print_linked_list(l2)
print("Result:")
print_linked_list(result)
```

    Input List 1:
    2 -> 4 -> 3
    Input List 2:
    5 -> 6 -> 4
    Result:
    7 -> 0 -> 8



```python

```


---
**Score: 5**