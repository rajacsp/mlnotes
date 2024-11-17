---
title: Sample
date: 2024-11-17
author: Your Name
cell_count: 9
score: 5
---

```python
# !pip install deepchecks
```


```python
import pandas as pd
from deepchecks.tabular.checks import MixedNulls, TrainTestFeatureDrift
# from deepchecks import Suite
```


```python
!pip show pandas | grep "Version"
```

    Version: 2.1.4



```python
from deepchecks import Suite
```


```python
import deepchecks
print(deepchecks.__version__)
```

    0.18.1



```python
# Sample data
train_data = pd.DataFrame({
    'age': [25, 35, 45, None, 50],
    'salary': [50000, 60000, None, 80000, 90000],
    'city': ['New York', 'Los Angeles', 'New York', None, 'San Francisco']
})
```


```python
test_data = pd.DataFrame({
    'age': [30, 40, 50, None, 55],
    'salary': [55000, 65000, 70000, None, 95000],
    'city': ['Chicago', 'Los Angeles', 'San Francisco', 'New York', None]
})
```


```python
# Running individual checks
null_check = MixedNulls().run(train_data)
print(null_check)
```

    deepchecks - WARNING - Received a "pandas.DataFrame" instance. It is recommended to pass a "deepchecks.tabular.Dataset" instance by initializing it with the data and metadata, for example by doing "Dataset(dataframe, label=label, cat_features=cat_features)"
    deepchecks - WARNING - It is recommended to initialize Dataset with categorical features by doing "Dataset(df, cat_features=categorical_list)". No categorical features were passed, therefore heuristically inferring categorical features in the data. 3 categorical features were inferred.: age, salary, city


    Mixed Nulls: {'n_samples': 5, 'columns': {'age': {'math.nan': {'count': 1, 'percent': 0.2}}, 'salary': {'math.nan': {'count': 1, 'percent': 0.2}}, 'city': {'None': {'count': 1, 'percent': 0.2}}}, 'feature_importance': age       NaN
    salary    NaN
    city      NaN
    dtype: object}



```python

```


---
**Score: 5**