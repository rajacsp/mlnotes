---
title: Geo Distance Method
date: 2025-05-17
author: Your Name
cell_count: 10
score: 10
---

---
title: "Geo Distance Method"
author: "Raja CSP Raman"
date: 2019-05-07
description: "-"
type: technical_note
draft: false
---

```python
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="rajarcsp")
from geopy import distance
```


```python
def get_distance(one, two):
    cone = geolocator.geocode(one)
    ctwo = geolocator.geocode(two)
    
    one_latlong = cone.latitude, ctwo.longitude
    two_latlong = ctwo.latitude, ctwo.longitude
    
    return distance.distance(one_latlong, two_latlong).km
```


```python
c_distance = get_distance("Montreal", "Toronto")
```


```python
c_distance
```




    204.82868885995472




```python
# Google distance is 540 km
```


```python
get_distance("Montreal", "Waterloo")
```




    225.6149620026681




```python
# Google distance is 638 km
```


```python
def get_circle_distance(one, two):
    cone = geolocator.geocode(one)
    ctwo = geolocator.geocode(two)
    
    one_latlong = cone.latitude, ctwo.longitude
    two_latlong = ctwo.latitude, ctwo.longitude
    
    return distance.great_circle(one_latlong, two_latlong).km
```


```python
get_circle_distance("Montreal", "Waterloo")
```




    225.764037559234




---
**Score: 10**