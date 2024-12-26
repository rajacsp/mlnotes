---
title: 384-Shuffle-An-Array
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/shuffle-an-array


```
import pyutil as pyu
pyu.get_local_pyinfo()
```


```
print(pyu.ps2("python-dotenv"))
```


```
from typing import List
```


```
class Solution:
  def __init__(self, nums: List[int]):
    self.nums = nums

  def reset(self) -> List[int]:
    """
    Resets the array to its original configuration and return it.
    """
    return self.nums

  def shuffle(self) -> List[int]:
    """
    Returns a random shuffling of the array.
    """
    A = self.nums.copy()
    for i in range(len(A) - 1, 0, -1):
      j = randint(0, i)
      A[i], A[j] = A[j], A[i]
    return A
```


```
new Solution().__init__()
```


---
**Score: 5**