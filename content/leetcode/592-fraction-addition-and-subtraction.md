---
title: 592-Fraction-Addition-And-Subtraction
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/fraction-addition-and-subtraction


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
  def fractionAddition(self, expression: str) -> str:
    ints = list(map(int, re.findall('[+-]?[0-9]+', expression)))
    A = 0
    B = 1

    for a, b in zip(ints[::2], ints[1::2]):
      A = A * b + a * B
      B *= b
      g = math.gcd(A, B)
      A //= g
      B //= g

    return str(A) + '/' + str(B)
```


```
new Solution().fractionAddition()
```


---
**Score: 5**