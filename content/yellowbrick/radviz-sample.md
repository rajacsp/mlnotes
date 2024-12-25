---
title: Radviz-Sample
date: 2024-12-25
author: Your Name
cell_count: 7
score: 5
---

---
title: "Radviz Sample"
author: "Raja CSP Raman"
date: 2019-02-03
description: "-"
type: technical_note
draft: false
---

```python
import pandas as pd
from yellowbrick.features import RadViz
```


```python
def load_yb_data(name = 'occupancy'):
    folder_path = name+'/'+name
    return pd.read_csv('/Users/rajacsp/datasets/yb_data/'+(folder_path)+'.csv')
```


```python
# Load the classification data set
data = load_yb_data("occupancy")
```


```python
# Specify the features of interest and the classes of the target
features = ["temperature", "relative humidity", "light", "C02", "humidity"]
classes = ["unoccupied", "occupied"]
```


```python
# Extract the instances and target
X = data[features]
y = data.occupancy
```


```python
# Instantiate the visualizer
visualizer = RadViz(classes=classes, features=features)

visualizer.fit(X, y)      # Fit the data to the visualizer
visualizer.transform(X)   # Transform the data
visualizer.poof()         # Draw/show/poof the data
```


    
![png](/mlnotes/images/radviz-sample_6_0.png)
    



---
**Score: 5**