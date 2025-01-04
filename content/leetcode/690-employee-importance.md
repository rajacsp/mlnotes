---
title: 690-Employee-Importance
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/employee-importance


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
  def getImportance(self, employees: List['Employee'], id: int) -> int:
    idToEmployee = {employee.id: employee for employee in employees}

    def dfs(id: int) -> int:
      values = idToEmployee[id].importance
      for subId in idToEmployee[id].subordinates:
        values += dfs(subId)
      return values

    return dfs(id)
```


```
new Solution().getImportance()
```


---
**Score: 5**