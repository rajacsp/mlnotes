---
title: 9-Palindrome-Number
date: 2024-12-25
author: Your Name
cell_count: 9
score: 5
---

```python
# https://leetcode.com/problems/palindrome-number/description/
```


```python
import pyutil as pyu
pyu.get_local_pyinfo()
```




    'conda env: ml311; pyv: 3.11.10 (main, Oct  3 2024, 07:29:13) [GCC 11.2.0]'




```python
# print(pyu.ps2("scipy"))
```


```python

```


```python
class Solution:
  def isPalindrome(self, x: int) -> bool:
    if x < 0:
      return False

    rev = 0
    y = x

    while y:
      rev = rev * 10 + y % 10
      y //= 10

    return rev == x
```


```python
Solution().isPalindrome(121)
```




    True




```python
Solution().isPalindrome(-121)
```




    False




```python
Solution().isPalindrome(10)
```




    False




```python

```


---
**Score: 5**