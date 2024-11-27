---
title: City Location
date: 2024-11-27
author: Your Name
cell_count: 5
score: 5
---

---
title: "City Location"
author: "Raja CSP Raman"
date: 2019-05-07
description: "-"
type: technical_note
draft: false
---

```python
from geopy.geocoders import Nominatim
geoloc = Nominatim(user_agent="rajarcsp", format_string="%s, Toronto ON")
```


```python
address, (lat, long) = geoloc.geocode("26, Spadina Road")
```


```python
address
```




    'Spadina Road, The Annex, University—Rosedale, Old Toronto, Toronto, Ontario, M5R 2X3, Canada'




```python

```


---
**Score: 5**