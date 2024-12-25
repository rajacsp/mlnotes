---
title: Geo Location 1
date: 2024-12-25
author: Your Name
cell_count: 6
score: 5
---

---
title: "Geo Location 1"
author: "Rj"
date: 2019-04-20
description: "-"
type: technical_note
draft: false
---

```python
import requests
import json 
```


```python
send_url = 'http://api.ipstack.com/50.100.30.136?access_key=49ad529d309a09477749245782d260b8&format=1'
```


```python
r = requests.get(send_url)
j = json.loads(r.text)

lat = j['latitude']
lon = j['longitude']
```


```python
print(lat)
print(lon)
```

    43.6909
    -79.3098



```python

```


---
**Score: 5**