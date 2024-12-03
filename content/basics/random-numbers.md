---
title: Random-Numbers
date: 2024-12-04
author: Your Name
cell_count: 11
score: 10
---

---
title: "Random Numbers"
author: "Rj"
date: 2019-04-20
description: "-"
type: technical_note
draft: false
---

```python
import random as rd
```


```python
def get_random():
    return rd.randint(0, 100)
```


```python
get_random()
```




    61




```python
def get_random_year_duration():
    return round(rd.uniform(1,2), 1)
```


```python
get_random_year_duration()
```




    1.6




```python
def get_random_price():
    return round(rd.uniform(1, 100), 2)
```


```python
get_random_price()
```




    43.21




```python
def get_random_double():
    return (rd.uniform(1, 100))
```


```python
get_random_double()
```




    45.42541472652959




```python

```


---
**Score: 10**