---
title: List-With-Diff-Datatype
date: 2025-05-17
author: Your Name
cell_count: 8
score: 5
---

```python

```


```python
import pyutil as pyu
pyu.get_local_pyinfo()
```




    'conda env: ml311; pyv: 3.11.10 (main, Oct  3 2024, 07:29:13) [GCC 11.2.0]'




```python
print(pyu.ps2("haystack-ai ollama-haystack python-dotenv"))
```

    haystack-ai==2.8.0
    ollama-haystack is not installed in the current environment.
    python-dotenv==1.0.1
    



```python

```


```python
lista = ["one", 2, "three", 4]
```


```python
type(lista)
```




    list




```python
for item in lista:
    print(f"{item}, {type(item)}")
```

    one, <class 'str'>
    2, <class 'int'>
    three, <class 'str'>
    4, <class 'int'>



```python

```


---
**Score: 5**