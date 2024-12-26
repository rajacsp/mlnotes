---
title: 948-Bag-Of-Tokens
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/bag-of-tokens


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
  def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
    ans = 0
    score = 0
    q = deque(sorted(tokens))

    while q and (power >= q[0] or score):
      while q and power >= q[0]:
        # Play the smallest face up
        power -= q.popleft()
        score += 1
      ans = max(ans, score)
      if q and score:
        # Play the largest face down
        power += q.pop()
        score -= 1

    return ans
```


```
new Solution().bagOfTokensScore()
```


---
**Score: 5**