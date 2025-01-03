---
title: 315-Count-Of-Smaller-Numbers-After-Self
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/count-of-smaller-numbers-after-self


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
class FenwickTree:
  def __init__(self, n: int):
    self.sums = [0] * (n + 1)

  def update(self, i: int, delta: int) -> None:
    while i < len(self.sums):
      self.sums[i] += delta
      i += self._lowbit(i)

  def get(self, i: int) -> int:
    summ = 0
    while i > 0:
      summ += self.sums[i]
      i -= self._lowbit(i)
    return summ

  def _lowbit(self, i) -> int:
    return i & -i


class Solution:
  def countSmaller(self, nums: List[int]) -> List[int]:
    ans = []
    ranks = Counter()
    self._getRanks(nums, ranks)
    tree = FenwickTree(len(ranks))

    for num in reversed(nums):
      ans.append(tree.get(ranks[num] - 1))
      tree.update(ranks[num], 1)

    return ans[::-1]

  def _getRanks(self, nums: List[int], ranks: Dict[int, int]) -> None:
    rank = 0
    for num in sorted(set(nums)):
      rank += 1
      ranks[num] = rank
```


```
new Solution().countSmaller()
```


---
**Score: 5**