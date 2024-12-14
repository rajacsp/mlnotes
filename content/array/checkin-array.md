---
title: Checkin-Array
date: 2024-12-14
author: Your Name
cell_count: 3
score: 0
---

```python

```


```python
def checkInArray(list, cc):
    #print(len(list))
    for x in list:
        print(x)
        
        if(x in cc):
            print('x['+x+'] ==> '+cc)
            return True
    
    return False


domain = "springframework.guru"

if(checkInArray(["baeldung", "abcde.com", "docs.spring.io", "springframework.guru",
                     "logback.qos.ch", "javabeat.net"], domain) ):
    print("java")
```

    baeldung
    abcde.com
    docs.spring.io
    springframework.guru
    x[springframework.guru] ==> springframework.guru
    java



```python

```


---
**Score: 0**