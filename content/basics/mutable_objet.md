---
title: Mutable Objet
date: 2024-12-05
author: Your Name
cell_count: 19
score: 15
---

---
title: "Mutable Object"
author: "Rj"
date: 2019-04-20
description: "List Test"
type: technical_note
draft: false
source: https://stackoverflow.com/questions/1132941/least-astonishment-and-the-mutable-default-argument
---

```python
def foo(a=[]):
    a.append(5)
    return a
```


```python
foo()
```




    [5]




```python
foo()
```




    [5, 5]




```python
foo()
```




    [5, 5, 5]



Reason:

What causes the confusion is the behaviour you get when you use a “mutable” object as a default value; that is, a value that can be modified in place, like a list or a dictionary.

The function keeps using the same object, in each call.

It is a common mistake in Python to set a mutable object as the default value of an argument in a function

more:
    
    https://stackoverflow.com/questions/1132941/least-astonishment-and-the-mutable-default-argument
        
    https://stackoverflow.com/questions/9158294/good-uses-for-mutable-function-argument-default-values
    
    http://effbot.org/zone/default-values.htm


```python
foo([14])
```




    [14, 5]




```python
foo([14])
```




    [14, 5]




```python
# Though it looks like a fundamental flaw, you can use it for caching purpose like we do in lrucache
```


```python
def add(name, cache={}):
    if name in cache: return cache[name]
    print('getting from expensive calculation')
    cache[name] = result = (name[::-1])
    return result
```


```python
add('one')
```

    getting from expensive calculation





    'eno'




```python
add('one') # This time it is coming from cache
```




    'eno'




```python
add('two')
```

    getting from expensive calculation





    'owt'



We will use it to calculate name meter


```python
def get_name_meter(name,  cache={}):
    
    if name in cache: 
        return cache[name]
    
    print('getting from expensive calculation')
    
    chars = list(name) # name.split won't return chars
    
    meter = 0
    for c in chars:
        meter += ord(c)
    
    cache[name] = result = meter
    return result
```


```python
get_name_meter('Toronto')
```

    getting from expensive calculation





    757




```python
get_name_meter('Toronto') # getting from cache
```




    757




```python
get_name_meter('Montreal')
```

    getting from expensive calculation





    834



Like above, we can use the mutable objects to take advantage of the situation


---
**Score: 15**