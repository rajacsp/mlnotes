---
title: 13-Roman-To-Integer
date: 2024-12-25
author: Your Name
cell_count: 10
score: 10
---

```python
# https://leetcode.com/problems/roman-to-integer/description/
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
  def romanToInt(self, s: str) -> int:
    ans = 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
             'C': 100, 'D': 500, 'M': 1000}

    for a, b in zip(s, s[1:]):
      if roman[a] < roman[b]:
        ans -= roman[a]
      else:
        ans += roman[a]

    return ans + roman[s[-1]]
```


```python
Solution().romanToInt("X")
```




    10




```python
Solution().romanToInt("III")
```




    3




```python
Solution().romanToInt("LVIII")
```




    58




```python
Solution().romanToInt("MCMXCIV")
```




    1994




```python

```


---
**Score: 10**