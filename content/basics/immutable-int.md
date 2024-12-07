---
title: Immutable-Int
date: 2024-12-07
author: Your Name
cell_count: 8
score: 5
---

---
title: "Immutable Int"
author: "Rj"
date: 2019-04-20
description: "List Test"
type: technical_note
draft: false
---

```python
a = 12

dictionary = {
  "one": a
}
```


```python
a
```




    12




```python
dictionary
```




    {'one': 12}




```python
a += 9
```


```python
a
```




    21




```python
dictionary
```




    {'one': 12}



int is immutable, that's why you can't see the dictionary value changed

Here you are assigning to key 'a' same reference as one. 

So now dictionary['one'] and a points to the same object 12. 

Now when you write: a += 9 it creates a new object 21 and assigns var to this object.


---
**Score: 5**