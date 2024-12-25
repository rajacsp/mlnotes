---
title: 12-Integer-To-Roman
date: 2024-12-25
author: Your Name
cell_count: 10
score: 10
---

```python
# https://leetcode.com/problems/integer-to-roman/description/
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
# from typing import List 
```


```python
class Solution:
  def intToRoman(self, num: int) -> str:
    valueSymbols = [(1000, 'M'), (900, 'CM'),
                    (500, 'D'), (400, 'CD'),
                    (100, 'C'), (90, 'XC'),
                    (50, 'L'), (40, 'XL'),
                    (10, 'X'), (9, 'IX'),
                    (5, 'V'), (4, 'IV'),
                    (1, 'I')]
    ans = []

    for value, symbol in valueSymbols:
      if num == 0:
        break
      count, num = divmod(num, value)
      ans.append(symbol * count)

    return ''.join(ans)

```


```python
Solution().intToRoman(3749)
```




    'MMMDCCXLIX'




```python
Solution().intToRoman(10)
```




    'X'




```python
Solution().intToRoman(2024)
```




    'MMXXIV'




```python
Solution().intToRoman(2025)
```




    'MMXXV'




```python

```


---
**Score: 10**