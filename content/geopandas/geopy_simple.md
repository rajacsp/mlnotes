---
title: Geopy Simple
date: 2024-12-05
author: Your Name
cell_count: 13
score: 10
---

---
title: "Template"
author: "Raja CSP Raman"
date: 2019-05-07
description: "-"
type: technical_note
draft: false
---

```python
from geopy.geocoders import Nominatim
```


```python
geolocator = Nominatim(user_agent="rajarcsp")
```


```python
location = geolocator.geocode("175 5th Avenue NYC")
```


```python
location
```




    Location(Flatiron Building, 175, 5th Avenue, Flatiron District, Manhattan, Manhattan Community Board 5, New York County, NYC, New York, 10010, USA, (40.7410861, -73.9896298241625, 0.0))




```python
type(location)
```




    geopy.location.Location




```python
location = geolocator.geocode("Toronto")
```


```python
location
```




    Location(Toronto, Ontario, M6K 1X9, Canada, (43.653963, -79.387207, 0.0))




```python
def get_lat_lang(city):
    location = geolocator.geocode(city)
    return location.latitude, location.longitude
```


```python
lat, long = get_lat_lang("Toronto")
```


```python
lat, long
```




    (43.653963, -79.387207)




```python

```


      File "<ipython-input-16-a60e00896a16>", line 1
        http://geopandas.org/index.html
              ^
    SyntaxError: invalid syntax




```python

```


---
**Score: 10**