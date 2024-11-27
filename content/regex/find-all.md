---
title: Find-All
date: 2024-11-27
author: Your Name
cell_count: 6
score: 5
---

---
title: "Find All"
author: "Raja CSP Raman"
date: 2019-04-20
description: "-"
type: technical_note
draft: false
---

```python
content = """OSPF Process 1 with Router ID 1.1.1.1
                       Area: 0.0.0.11
               Link State Database  
               Router test 
               Maintenance
"""
```


```python
content
```




    'OSPF Process 1 with Router ID 1.1.1.1\n                       Area: 0.0.0.11\n               Link State Database  \n               Router test \n               Maintenance\n'




```python
import re

regex = "OSPF|Area|Link"

lines = content.split("\n")

print(lines)


```

    ['OSPF Process 1 with Router ID 1.1.1.1', '                       Area: 0.0.0.11', '               Link State Database  ', '               Router test ', '               Maintenance', '']



```python
for line in lines:
    print(line)
```

    OSPF Process 1 with Router ID 1.1.1.1
                           Area: 0.0.0.11
                   Link State Database  
                   Router test 
                   Maintenance
    



```python
for line in lines:
    if not re.findall(regex, line):
        print(line)
```

                   Router test 
                   Maintenance
    



---
**Score: 5**