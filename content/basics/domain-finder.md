---
title: Domain-Finder
date: 2024-11-24
author: Your Name
cell_count: 6
score: 5
---

---
title: "Find Domain"
author: "Rj"
date: 2019-04-20
description: "List Test"
type: technical_note
draft: false
---

```python
def get_domain(url):
    spltAr = url.split("://")
    i = (0,1)[len(spltAr)>1]
    dm = spltAr[i].split("?")[0].split('/')[0].split(':')[0].lower()
    #print(dm)
    return dm
```


```python
def get_domain_without_prefix(url):
    spltAr = url.split("://")
    i = (0,1)[len(spltAr)>1]
    dm = spltAr[i].split("?")[0].split('/')[0].split(':')[0].lower()
    
    if("www." in dm):
        dm = dm.replace("www.", "")
    
    #print(dm)
    return dm
```


```python
urls = [
    "http://www.oreilly.com/people/adam-michael-wood",
    "https://javabeat.net/introduction-to-hibernate-caching/",
]
```


```python
for url in urls:
    domain = get_domain_without_prefix(url)
    print(domain)
```

    oreilly.com
    javabeat.net



```python

```


---
**Score: 5**