---
title: 1-Two-Sums
date: 2024-12-26
author: Your Name
cell_count: 8
score: 5
---

```python
# https://leetcode.com/problems/two-sum
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
    



```python
from typing import List

class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    numToIndex = {}

    for i, num in enumerate(nums):
      if target - num in numToIndex:
        return numToIndex[target - num], i
      numToIndex[num] = i
```


```python
sol = Solution()
```


```python
sol.twoSum([2,7,11,15], 9)
```




    (0, 1)




```python
sol.twoSum([3,2,4], 6)
```




    (1, 2)




```python

```


---
**Score: 5**