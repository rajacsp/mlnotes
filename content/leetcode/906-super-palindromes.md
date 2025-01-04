---
title: 906-Super-Palindromes
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/super-palindromes


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
  def superpalindromesInRange(self, left: str, right: str) -> int:
    def nextPalindrome(num: int) -> int:
      s = str(num)
      n = len(s)

      half = s[0:(n + 1) // 2]
      reversedHalf = half[:n // 2][::-1]
      candidate = int(half + reversedHalf)
      if candidate >= num:
        return candidate

      half = str(int(half) + 1)
      reversedHalf = half[:n // 2][::-1]
      return int(half + reversedHalf)

    def isPalindrome(num: int) -> bool:
      s = str(num)
      l = 0
      r = len(s) - 1

      while l < r:
        if s[l] != s[r]:
          return False
        l += 1
        r -= 1

      return True

    ans = 0
    l = int(left)
    r = int(right)
    i = int(sqrt(l))

    while i * i <= r:
      palindrome = nextPalindrome(i)
      squared = palindrome**2
      if squared <= r and isPalindrome(squared):
        ans += 1
      i = palindrome + 1

    return ans
```


```
new Solution().superpalindromesInRange()
```


---
**Score: 5**