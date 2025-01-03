---
title: 204-Count-Primes
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/count-primes


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
  def countPrimes(self, n: int) -> int:
    if n <= 2:
      return 0

    isPrime = [False] * 2 + [True] * (n - 2)

    for i in range(2, int(n**0.5) + 1):
      if isPrime[i]:
        for j in range(i * i, n, i):
          isPrime[j] = False

    return sum(isPrime)
```


```
new Solution().countPrimes()
```


---
**Score: 5**