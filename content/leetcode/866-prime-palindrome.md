---
title: 866-Prime-Palindrome
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/prime-palindrome


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
  def primePalindrome(self, N: int) -> int:
    def getPalindromes(n: int) -> int:
      length = n // 2
      for i in range(10**(length - 1), 10**length):
        s = str(i)
        for j in range(10):
          yield int(s + str(j) + s[::-1])

    def isPrime(num: int) -> bool:
      return not any(num % i == 0 for i in range(2, int(num**0.5 + 1)))

    if N <= 2:
      return 2
    if N == 3:
      return 3
    if N <= 5:
      return 5
    if N <= 7:
      return 7
    if N <= 11:
      return 11

    n = len(str(N))

    while True:
      for num in getPalindromes(n):
        if num >= N and isPrime(num):
          return num
      n += 1
```


```
new Solution().primePalindrome()
```


---
**Score: 5**