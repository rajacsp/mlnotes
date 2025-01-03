---
title: Geo Distance
date: 2025-01-03
author: Your Name
cell_count: 29
score: 25
---

---
title: "Geo Distance"
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
l_spadina = geolocator.geocode("28 Spadina Road")
```


```python
l_spadina_latlong = l_spadina.latitude, l_spadina.longitude
```


```python
l_spadina_latlong
```




    (43.6966329769175, -79.7940236288173)




```python
l_north_york = geolocator.geocode("5000 Yonge Street")
```


```python
l_north_york_latlong = l_north_york.latitude, l_north_york.longitude
```


```python
l_north_york_latlong
```




    (43.6490951, -79.3778661)




```python
c_distance = distance.distance(l_spadina_latlong, l_north_york_latlong)
```


```python
c_distance
```




    Distance(33.974290494387375)




```python
c_distance.km
```




    33.974290494387375




```python
# The above information is wrong. It can't be 31 KM between 20 and 286 Spadina Road

# Let's do in another way
```


```python
geolocator = Nominatim(user_agent="rajarcsp", format_string="%s, Toronto ON")
from geopy import distance
```


```python
l_spadina = geolocator.geocode("28 Spadina Road")
```


```python
l_spadina_latlong = l_spadina.latitude, l_spadina.longitude
```


```python
l_north_york = geolocator.geocode("225 Davenport Rd")
```


```python
l_north_york_latlong = l_north_york.latitude, l_north_york.longitude
```


```python
c_distance = distance.distance(l_spadina_latlong, l_north_york_latlong).km
```


```python
c_distance
```




    0.8538498245022255




```python
# Though it is little bit close, it is not exactly right
```


```python
# Let's try between Cities
```


```python
geolocator = Nominatim(user_agent="rajarcsp")
```


```python
to = geolocator.geocode("Toronto")
```


```python
wl = geolocator.geocode("Waterloo")
```


```python
to_latlong = to.latitude, to.longitude
```


```python
wl_latlong = wl.latitude, wl.longitude
```


```python
c_distance = distance.distance(to_latlong, wl_latlong).km
```


```python
c_distance
```




    94.22021710762372




```python
# It google maps, it says 113KM which is 20 km longer than our distance
```


---
**Score: 25**