---
title: Enumerate-Sample
date: 2024-11-24
author: Your Name
cell_count: 6
score: 5
---

---
title: "Enumerate"
author: "Rj"
date: 2019-04-20
description: "List Test"
type: technical_note
draft: false
---

```python
data = ['Toronto', 'Montreal', 'Waterloo', 'Chennai', 'Bangalore', 123, ['One', 'Two', 'Three']]
```


```python
for x in enumerate(data):
    print(x)
```

    (0, 'Toronto')
    (1, 'Montreal')
    (2, 'Waterloo')
    (3, 'Chennai')
    (4, 'Bangalore')
    (5, 123)
    (6, ['One', 'Two', 'Three'])



```python
for i, x in enumerate(data):
    print(i, "==>", x)
```

    0 ==> Toronto
    1 ==> Montreal
    2 ==> Waterloo
    3 ==> Chennai
    4 ==> Bangalore
    5 ==> 123
    6 ==> ['One', 'Two', 'Three']



```python
# start the index from 200
for i, x in enumerate(data, 200):
    print(i, "==>", x)
```

    200 ==> Toronto
    201 ==> Montreal
    202 ==> Waterloo
    203 ==> Chennai
    204 ==> Bangalore
    205 ==> 123
    206 ==> ['One', 'Two', 'Three']



```python

```


---
**Score: 5**