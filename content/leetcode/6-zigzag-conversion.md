---
title: 6-Zigzag-Conversion
date: 2024-12-25
author: Your Name
cell_count: 8
score: 5
---

```python
# https://leetcode.com/problems/zigzag-conversion/description/
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
  def convert(self, s: str, numRows: int) -> str:
    rows = [''] * numRows
    k = 0
    direction = (numRows == 1) - 1

    for c in s:
      rows[k] += c
      if k == 0 or k == numRows - 1:
        direction *= -1
      k += direction

    return ''.join(rows)
```


```python
Solution().convert("PAYPALISHIRING", 3)
```




    'PAHNAPLSIIGYIR'




```python
Solution().convert("PAYPALISHIRING", 4)
```




    'PINALSIGYAHRPI'




```python

```


---
**Score: 5**