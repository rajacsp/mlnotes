---
title: Sort-Map-By-Value
date: 2024-11-25
author: Your Name
cell_count: 6
score: 5
---

---
title: "Sort Map by Value"
author: "Rj"
date: 2019-04-20
description: "List Test"
type: technical_note
draft: false
---

```python
def sort_by_value(dict):
    '''
        
    '''
    
    age_sorted = sorted(dict.items(), key=lambda x:x[1])
   
    #print(age_sorted)
       
    return age_sorted
```


```python
age = {
        'carl':40,
        'alan':2,
        'bob':1,
        'danny':3
    }
```


```python
age_sorted = sort_by_value(age)
```


```python
age_sorted
```




    [('bob', 1), ('alan', 2), ('danny', 3), ('carl', 40)]




```python

```


---
**Score: 5**