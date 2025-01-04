---
title: Slice Array
date: 2025-01-04
author: Your Name
cell_count: 22
score: 20
---

---
title: "Slice Array"
author: "Rj"
date: 2019-04-20
description: "List Test"
type: technical_note
draft: false
---

```python
a = [
    10, 20, 30, 40, 50, 60, 70, 80, 90
]
```


```python
a
```




    [10, 20, 30, 40, 50, 60, 70, 80, 90]




```python
type(a)
```




    list




```python
a[4:8]
```




    [50, 60, 70, 80]




```python
a[:4]
```




    [10, 20, 30, 40]




```python
a[4:]
```




    [50, 60, 70, 80, 90]




```python
a[:]
```




    [10, 20, 30, 40, 50, 60, 70, 80, 90]




```python
a[-1]
```




    90




```python
a[-2]
```




    80




```python
# get last 2 items
a[-2:]
```




    [80, 90]




```python
# every except last 2 iteme
a[:-2]
```




    [10, 20, 30, 40, 50, 60, 70]




```python
# all items reverse
a[::-1]
```




    [90, 80, 70, 60, 50, 40, 30, 20, 10]




```python
a[1::-1]
```




    [20, 10]




```python
a[1::-2]
```




    [20]




```python
# get the first three items reversed
a[2::-1]
```




    [30, 20, 10]




```python
# all items eversed and ignore the last item
a[-2::-1]
```




    [80, 70, 60, 50, 40, 30, 20, 10]




```python
# Remove last 2 items, reverse all the rest of the items
a[-3::-1]
```




    [70, 60, 50, 40, 30, 20, 10]




```python
# last two items reversed
a[:-3:-1]
```




    [90, 80]




```python
a[:-4:-1]
```




    [90, 80, 70]




```python
# Everything except the last 3 items, reversed
a[-4::-1]
```




    [60, 50, 40, 30, 20, 10]




```python

```


---
**Score: 20**