---
title: Data Array Simple
date: 2024-12-06
author: Your Name
cell_count: 6
score: 5
---

---
title: "Data Array Simple"
author: "Rj"
date: 2019-04-20
description: "-"
type: technical_note
draft: false
---

```python
import xarray as xr
import numpy as np
import pandas as pd
```


```python
data = np.random.rand(4, 3)

locs = ['TO', 'ML', 'WL']

times = pd.date_range('2000-01-01', periods=4)
```


```python
abc = xr.DataArray(data, coords=[times, locs], dims=['time', 'space'])
```


```python
abc
```




    <xarray.DataArray (time: 4, space: 3)>
    array([[0.88587 , 0.828511, 0.122515],
           [0.815572, 0.524299, 0.717162],
           [0.494704, 0.319359, 0.658114],
           [0.841205, 0.371321, 0.276608]])
    Coordinates:
      * time     (time) datetime64[ns] 2000-01-01 2000-01-02 2000-01-03 2000-01-04
      * space    (space) <U2 'TO' 'ML' 'WL'




```python

```


---
**Score: 5**