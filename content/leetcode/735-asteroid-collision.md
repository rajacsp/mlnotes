---
title: 735-Asteroid-Collision
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/asteroid-collision


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
  def asteroidCollision(self, asteroids: List[int]) -> List[int]:
    stack = []

    for a in asteroids:
      if a > 0:
        stack.append(a)
      else:  # A < 0
        # Destroy previous positive one(s)
        while stack and stack[-1] > 0 and stack[-1] < -a:
          stack.pop()
        if not stack or stack[-1] < 0:
          stack.append(a)
        elif stack[-1] == -a:
          stack.pop()  # Both explode
        else:  # stack[-1] > current
          pass  # Destroy current, so do nothing

    return stack
```


```
new Solution().asteroidCollision()
```


---
**Score: 5**