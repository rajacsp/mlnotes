---
title: Name Meter
date: 2024-12-26
author: Your Name
cell_count: 7
score: 5
---

---
title: "Get Name Meter"
author: "Rj"
date: 2019-04-20
description: "List Test"
type: technical_note
draft: false
---

```python
def get_int(c):
    if(c == 'a'):
        return (200 + ord(c))
    
    if(c == 'e'):
        return (250 + ord(c))
    
    if(c == 'i'):
        return (300 + ord(c))
    
    if(c == 'o'):
        return (350 + ord(c))
    
    if(c == 'u'):
        return (400 + ord(c))
    
    return ord(c)

def get_name_meter(name,  cache={}):
    
    if name in cache: 
        return cache[name]
    
    print('getting from expensive calculation')
    
    chars = list(name) # name.split won't return chars
    
    meter = 0
    for c in chars:
        
        meter += get_int(c)
    
    cache[name] = result = meter
    return result
```


```python
get_name_meter('Toronto')
```

    getting from expensive calculation





    1807




```python
get_name_meter('Canada')
```

    getting from expensive calculation





    1168




```python
get_name_meter('Montreal')
```

    getting from expensive calculation





    1634




```python
get_name_meter('Montreal')
```




    1634




```python

```


---
**Score: 5**