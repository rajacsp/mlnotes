---
title: Default-Dict
date: 2024-11-25
author: Your Name
cell_count: 11
score: 10
---

---
title: "Default Dict"
author: "Rj"
date: 2019-04-20
description: "List Test"
type: technical_note
draft: false
source: https://www.accelebrate.com/blog/using-defaultdict-python/
---

```python
from collections import defaultdict
```


```python
user = defaultdict(lambda: 'Kevin')
```


```python
user
```




    defaultdict(<function __main__.<lambda>>, {})




```python
type(user)
```




    collections.defaultdict




```python
user['abc']
```




    'Kevin'




```python
user['country']
```




    'Kevin'




```python
user['name'] = 'Peter'
user['age'] = 21
user['city'] = 'Toronto'
```


```python
user
```




    defaultdict(<function __main__.<lambda>>,
                {'abc': 'Kevin',
                 'age': 21,
                 'city': 'Toronto',
                 'country': 'Kevin',
                 'name': 'Peter'})




```python
for k, v in user.items():
    print(k, "==>", v)
```

    abc ==> Kevin
    country ==> Kevin
    name ==> Peter
    age ==> 21
    city ==> Toronto



```python

```


---
**Score: 10**