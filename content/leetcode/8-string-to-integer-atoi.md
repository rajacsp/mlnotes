---
title: 8-String-To-Integer-Atoi
date: 2024-12-25
author: Your Name
cell_count: 11
score: 10
---

```python

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
  def myAtoi(self, s: str) -> int:
    s = s.strip()
    if not s:
      return 0

    sign = -1 if s[0] == '-' else 1
    if s[0] in {'-', '+'}:
      s = s[1:]

    num = 0

    for c in s:
      if not c.isdigit():
        break
      num = num * 10 + ord(c) - ord('0')
      if sign * num <= -2**31:
        return -2**31
      if sign * num >= 2**31 - 1:
        return 2**31 - 1

    return sign * num
```


```python
Solution().myAtoi("42")
```




    42




```python
Solution().myAtoi("-042")
```




    -42




```python
Solution().myAtoi("1337c0d3")
```




    1337




```python
Solution().myAtoi("0-1")
```




    0




```python
Solution().myAtoi("words and 987")
```




    0




```python

```


---
**Score: 10**