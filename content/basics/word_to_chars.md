---
title: Word To Chars
date: 2024-11-24
author: Your Name
cell_count: 17
score: 15
---

---
title: "Word to Chars"
author: "Rj"
date: 2019-04-20
description: "List Test"
type: technical_note
draft: false
---

```python
word = "Toronto"
```


```python
word
```




    'Toronto'




```python
type(word)
```




    str




```python
letters = word.split()
```


```python
type(letters)
```




    list




```python
for l in letters:
    print(l, type(l))
```

    Toronto <class 'str'>



```python
len(letters)
```




    1




```python
chars = list(word)
```


```python
type(chars)
```




    list




```python
for c in chars:
    print(c, type(c))
```

    T <class 'str'>
    o <class 'str'>
    r <class 'str'>
    o <class 'str'>
    n <class 'str'>
    t <class 'str'>
    o <class 'str'>



```python
len(chars)
```




    7




```python
# list(string) will get us characters, but split will get us strings
```


```python
[c for c in word]
```




    ['T', 'o', 'r', 'o', 'n', 't', 'o']




```python
[c for c in word.split()]
```




    ['Toronto']




```python
word.split()
```




    ['Toronto']




```python

```


---
**Score: 15**