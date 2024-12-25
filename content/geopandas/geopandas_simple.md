---
title: Geopandas Simple
date: 2024-12-25
author: Your Name
cell_count: 6
score: 5
---

---
title: "Geo Pandas Simple"
author: "Raja CSP Raman"
date: 2019-05-07
description: "-"
type: technical_note
draft: false
---

```python
import pandas as pd
import geopandas
import matplotlib.pyplot as plt
```


```python
df = pd.DataFrame(
    {'City': ['Buenos Aires', 'Brasilia', 'Santiago', 'Bogota', 'Caracas'],
     'Country': ['Argentina', 'Brazil', 'Chile', 'Colombia', 'Venezuela'],
     'Latitude': [-34.58, -15.78, -33.45, 4.60, 10.48],
     'Longitude': [-58.66, -47.91, -70.66, -74.08, -66.86]})
```


```python
gdf = geopandas.GeoDataFrame(
    df, geometry=geopandas.points_from_xy(df.Longitude, df.Latitude))
```


```python
print(gdf.head())
```

               City    Country  Latitude  Longitude               geometry
    0  Buenos Aires  Argentina    -34.58     -58.66  POINT (-58.66 -34.58)
    1      Brasilia     Brazil    -15.78     -47.91  POINT (-47.91 -15.78)
    2      Santiago      Chile    -33.45     -70.66  POINT (-70.66 -33.45)
    3        Bogota   Colombia      4.60     -74.08     POINT (-74.08 4.6)
    4       Caracas  Venezuela     10.48     -66.86   POINT (-66.86 10.48)



```python
world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))

# We restrict to South America.
ax = world[world.continent == 'South America'].plot(
    color='white', edgecolor='black')

# We can now plot our GeoDataFrame.
gdf.plot(ax=ax, color='red')

plt.show()
```


    
![png](/mlnotes/images/geopandas_simple_5_0.png)
    



---
**Score: 5**