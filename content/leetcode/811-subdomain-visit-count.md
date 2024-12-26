---
title: 811-Subdomain-Visit-Count
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/subdomain-visit-count


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
  def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
    ans = []
    count = Counter()

    for cpdomain in cpdomains:
      num, domains = cpdomain.split()
      num, domains = int(num), domains.split('.')
      for i in reversed(range(len(domains))):
        count['.'.join(domains[i:])] += num

    return [str(freq) + ' ' + domain for domain, freq in count.items()]
```


```
new Solution().subdomainVisits()
```


---
**Score: 5**