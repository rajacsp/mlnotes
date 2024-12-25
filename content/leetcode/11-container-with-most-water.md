---
title: 11-Container-With-Most-Water
date: 2024-12-25
author: Your Name
cell_count: 7
score: 5
---

```python
# https://leetcode.com/problems/container-with-most-water/description/
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
from typing import List
```


```python
class Solution:
  def maxArea(self, height: List[int]) -> int:
    ans = 0
    l = 0
    r = len(height) - 1

    while l < r:
      minHeight = min(height[l], height[r])
      ans = max(ans, minHeight * (r - l))
      if height[l] < height[r]:
        l += 1
      else:
        r -= 1

    return ans
```


```python
Solution().maxArea([1,1])
```




    1




```python

```


---
**Score: 5**