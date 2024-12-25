---
title: Yb-Bikeshare
date: 2024-12-25
author: Your Name
cell_count: 7
score: 5
---

---
title: "YB Bikeshare Visualizer"
author: "Raja CSP Raman"
date: 2019-04-20
description: "-"
type: technical_note
draft: false
---

```python
import pandas as pd
from yellowbrick.features import Rank2D
```


```python
def load_yb_data(name = 'bikeshare'):
    folder_path = name+'/'+name
    return pd.read_csv('/Users/rajacsp/datasets/yb_data/'+(folder_path)+'.csv')
```


```python
data = load_yb_data('bikeshare')
```


```python
X = data[[
    "season", "month", "hour", "holiday", "weekday", "workingday",
    "weather", "temp", "feelslike", "humidity", "windspeed"
]]
y = data["riders"]
```


```python
visualizer = Rank2D(algorithm="pearson")
visualizer.fit_transform(X)
visualizer.poof()
```

    /Users/rajacsp/anaconda3/envs/py36/lib/python3.6/site-packages/yellowbrick/features/rankd.py:262: FutureWarning: Method .as_matrix will be removed in a future version. Use .values instead.
      X = X.as_matrix()



    
![png](/mlnotes/images/yb-bikeshare_5_1.png)
    


Note:

A Pearson correlation of 1.0 means that there is a strong positive, 
linear relationship between the pairs of variables and a value of -1.0 indicates a strong negative, 
linear relationship (a value of zero indicates no relationship). 
Therefore we are looking for dark red and dark blue boxes to identify further.

Dark red = positive (related) - strong correlation
Dark blue = negative (inversely related) - 


---
**Score: 5**