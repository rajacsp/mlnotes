---
title: 164-Maximum-Gap
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/maximum-gap


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
class Bucket:
  def __init__(self, mini: int, maxi: int):
    self.mini = mini
    self.maxi = maxi


class Solution:
  def maximumGap(self, nums: List[int]) -> int:
    if len(nums) < 2:
      return 0

    mini = min(nums)
    maxi = max(nums)
    if mini == maxi:
      return 0

    gap = ceil((maxi - mini) / (len(nums) - 1))
    bucketSize = (maxi - mini) // gap + 1
    buckets = [Bucket(math.inf, -math.inf) for _ in range(bucketSize)]

    for num in nums:
      i = (num - mini) // gap
      buckets[i].mini = min(buckets[i].mini, num)
      buckets[i].maxi = max(buckets[i].maxi, num)

    ans = 0
    prevMax = mini

    for bucket in buckets:
      if bucket.mini == math.inf:
        continue  # Empty bucket
      ans = max(ans, bucket.mini - prevMax)
      prevMax = bucket.maxi

    return ans
```


```
new Solution().maximumGap()
```


---
**Score: 5**