---
title: 14-Longest-Common-Prefix
date: 2024-12-25
author: Your Name
cell_count: 6
score: 5
---

```python
# https://leetcode.com/problems/longest-common-prefix/description/
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
  def longestCommonPrefix(self, strs: List[str]) -> str:
    if not strs:
      return ''

    for i in range(len(strs[0])):
      for j in range(1, len(strs)):
        if i == len(strs[j]) or strs[j][i] != strs[0][i]:
          return strs[0][:i]

    return strs[0]
```


```python
Solution().longestCommonPrefix()
```


---
**Score: 5**