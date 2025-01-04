---
title: Geo Location 2
date: 2025-01-04
author: Your Name
cell_count: 7
score: 5
---

---
title: "Geo Location by Geocoder"
author: "Rj"
date: 2019-04-20
description: "-"
type: technical_note
draft: false
---

```python
import geocoder
```


```python
g = geocoder.ip('me')
```


```python
print(g.latlng)
```

    [43.6909, -79.3098]



```python
test_location = geocoder.ip('151.101.1.69')
```


```python
print(test_location.latlng)
```

    [37.751, -97.822]



```python

```


---
**Score: 5**