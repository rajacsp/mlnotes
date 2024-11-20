---
title: California-Xgb-Sns
date: 2024-11-20
author: Your Name
cell_count: 7
score: 5
---

```python
!python --version
```

    Python 3.10.5



```python
import xgboost as xgb
import pandas as pd
import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import seaborn as sns
import matplotlib.pyplot as plt
```


```python
# Load the California housing dataset
data = fetch_california_housing()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target)
```


```python
# Add target to the DataFrame for visualization
X['Target'] = y
```


```python
# Add latitude and longitude for mapping
# Note: These columns already exist in the California housing dataset
X['Latitude'] = data.data[:, -1]  # Latitude is the last column in the dataset
X['Longitude'] = data.data[:, -2]  # Longitude is the second-last column
```


```python
# Plot the geographic distribution of the housing data
plt.figure(figsize=(10, 8))
sns.scatterplot(
    x='Longitude', 
    y='Latitude', 
    hue='Target', 
    size='Target', 
    sizes=(20, 200), 
    palette='viridis', 
    data=X, 
    alpha=0.7
)
plt.title('California Housing Prices')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.legend(title="Price", loc='upper right')
plt.show()
```


    
![png](/mlnotes/images/california-xgb-sns_5_0.png)
    



```python

```


---
**Score: 5**