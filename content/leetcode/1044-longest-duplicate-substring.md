---
title: 1044-Longest-Duplicate-Substring
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/longest-duplicate-substring


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
  def longestDupSubstring(self, s: str) -> str:
    kMod = 1_000_000_007
    bestStart = -1
    l = 1
    r = len(s)

    def val(c: str) -> int:
      return ord(c) - ord('a')

    # K := length of hashed substring
    def getStart(k: int) -> Optional[int]:
      maxPow = pow(26, k - 1, kMod)
      hashedToStart = defaultdict(list)
      h = 0

      # Compute hash value of s[:k]
      for i in range(k):
        h = (h * 26 + val(s[i])) % kMod
      hashedToStart[h].append(0)

      # Compute rolling hash by Rabin Karp
      for i in range(k, len(s)):
        startIndex = i - k + 1
        h = (h - maxPow * val(s[i - k])) % kMod
        h = (h * 26 + val(s[i])) % kMod
        if h in hashedToStart:
          currSub = s[startIndex:startIndex + k]
          for start in hashedToStart[h]:
            if s[start:start + k] == currSub:
              return startIndex
        hashedToStart[h].append(startIndex)

    while l < r:
      m = (l + r) // 2
      start: Optional[int] = getStart(m)
      if start:
        bestStart = start
        l = m + 1
      else:
        r = m

    if bestStart == -1:
      return ''
    if getStart(l):
      return s[bestStart:bestStart + l]
    return s[bestStart:bestStart + l - 1]
```


```
new Solution().longestDupSubstring()
```


---
**Score: 5**