---
title: Pass By Ref Test
date: 2024-12-03
author: Your Name
cell_count: 7
score: 5
---

---
title: "Pass by Ref Test"
author: "Rj"
date: 2019-04-20
description: "List Test"
type: technical_note
draft: false
---

```python
def add_to_list(list):
    list.append('three')
```


```python
list = ['one', 'two']
```


```python
add_to_list(list)
```


```python
print(list)
```

    ['one', 'two', 'three']


Key takeaway:

1- You can use the reference that a function receives as its arguments, to modify the 'outside' value of a variable, as long as you don't reassign the parameter to refer to a new object. 
        
        
2- Assigning to an immutable type will always create a new object, which breaks the reference that you had to the outside variable.

https://docs.python.org/3/faq/programming.html#how-do-i-write-a-function-with-output-parameters-call-by-reference

https://stackoverflow.com/questions/986006/how-do-i-pass-a-variable-by-reference


```python

```


---
**Score: 5**