---
title: Lambda-Custom
date: 2024-12-14
author: Your Name
cell_count: 7
score: 5
---

---
title: "Lambda Custom"
author: "Raja CSP Raman"
date: 2019-04-20
description: "-"
type: technical_note
draft: false
---

```python
cities = [
    'chennai', 'delhi', 'madurai', 'pune', 'bengaluru'
    ]
```


```python
cities
```




    ['chennai', 'delhi', 'madurai', 'pune', 'bengaluru']




```python
def is_south_indian_city(city):
    if city == 'chennai' or city == 'madurai' or city == 'bengaluru':
        return True
    
    return False
```


```python
new_list = list(filter(lambda x: is_south_indian_city(x) , cities))
```


```python
new_list
```




    ['chennai', 'madurai', 'bengaluru']




```python

```


---
**Score: 5**