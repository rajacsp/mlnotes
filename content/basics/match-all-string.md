---
title: Match-All-String
date: 2025-01-03
author: Your Name
cell_count: 9
score: 5
---

---
title: "Match All String"
author: "Rj"
date: 2019-04-20
description: "List Test"
type: technical_note
draft: false
---

```python
one = "Toronto is nice"
```


```python
one
```




    'Toronto is nice'




```python
one_array = one.split(" ")
```


```python
two = "It is nice to be in Toronto"
```


```python
two_array = two.split(" ")
```


```python
two_array
```




    ['It', 'is', 'nice', 'to', 'be', 'in', 'Toronto']




```python
all(x in two for x in one_array)
```




    True



More:

https://stackoverflow.com/questions/56165622/shortest-way-to-check-wether-a-list-of-strings-occur-in-a-string


---
**Score: 5**