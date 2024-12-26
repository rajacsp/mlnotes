---
title: 599-Minimum-Index-Sum-Of-Two-Lists
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/minimum-index-sum-of-two-lists


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
  def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
    ans = []
    restaurantToIndex = {restaurant: i for i,
                         restaurant in enumerate(list1)}
    minSum = math.inf

    for i, restaurant in enumerate(list2):
      if restaurant in restaurantToIndex:
        summ = restaurantToIndex[restaurant] + i
        if summ < minSum:
          ans.clear()
        if summ <= minSum:
          ans.append(restaurant)
          minSum = summ

    return ans
```


```
new Solution().findRestaurant()
```


---
**Score: 5**