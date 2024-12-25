---
title: 7-Reverse-Integer
date: 2024-12-25
author: Your Name
cell_count: 9
score: 5
---

```python
# https://leetcode.com/problems/reverse-integer/description/
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
  def reverse(self, x: int) -> int:
    ans = 0
    sign = -1 if x < 0 else 1
    x *= sign

    while x:
      ans = ans * 10 + x % 10
      x //= 10

    return 0 if ans < -2**31 or ans > 2**31 - 1 else sign * ans
```


```python
Solution().reverse(123)
```




    321




```python
Solution().reverse(-123)
```




    -321




```python
Solution().reverse(120)
```




    21




```python

```


---
**Score: 5**