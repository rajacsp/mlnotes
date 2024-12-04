---
title: Linear-Regression-Simple-7477
date: 2024-12-04
author: Your Name
cell_count: 14
score: 10
---

---
title: "Linear Regression Simple"
author: "Rj"
date: 2019-04-20
description: "-"
type: technical_note
draft: false
---

```python
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
```


```python
# Load the diabetes dataset
diabetes_data = datasets.load_diabetes()
```


```python
# Print all keys and number of raw and columns
print(diabetes_data.keys, diabetes_data.data.shape)
```

    <built-in method keys of Bunch object at 0x10b789830> (442, 10)



```python
# Print all the feature_names in dataset
print(diabetes_data.feature_names)
```

    ['age', 'sex', 'bmi', 'bp', 's1', 's2', 's3', 's4', 's5', 's6']



```python
df = pd.DataFrame(diabetes_data.data)
df.columns = diabetes_data.feature_names
```


```python
df['target'] = diabetes_data.target
```


```python
x=df.drop('target',axis=1)
```


```python
# Create linear regression object
rm = linear_model.LinearRegression()
```


```python
rm.fit(x,df.target)
```




    LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None,
             normalize=False)




```python
print(rm.intercept_)
print(rm.coef_)
```

    152.1334841628965
    [ -10.01219782 -239.81908937  519.83978679  324.39042769 -792.18416163
      476.74583782  101.04457032  177.06417623  751.27932109   67.62538639]



```python
print(rm.predict(x)[:10])
```

    [206.11706979  68.07234761 176.88406035 166.91796559 128.45984241
     106.34908972  73.89417947 118.85378669 158.81033076 213.58408893]



```python
plt.scatter(df.target, rm.predict(x))
plt.xlabel('old data')
plt.ylabel('predicted data')
plt.show()
```


    
![png](/mlnotes/images/linear-regression-simple_12_0.png)
    



```python

```


---
**Score: 10**