---
title: 166-Fraction-To-Recurring-Decimal
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/fraction-to-recurring-decimal


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
  def fractionToDecimal(self, numerator: int, denominator: int) -> str:
    if numerator == 0:
      return '0'

    ans = ''

    if (numerator < 0) ^ (denominator < 0):
      ans += '-'

    numerator = abs(numerator)
    denominator = abs(denominator)
    ans += str(numerator // denominator)

    if numerator % denominator == 0:
      return ans

    ans += '.'
    dict = {}

    remainder = numerator % denominator
    while remainder:
      if remainder in dict:
        ans = ans[:dict[remainder]] + '(' + ans[dict[remainder]:] + ')'
        break
      dict[remainder] = len(ans)
      remainder *= 10
      ans += str(remainder // denominator)
      remainder %= denominator

    return ans
```


```
new Solution().fractionToDecimal()
```


---
**Score: 5**