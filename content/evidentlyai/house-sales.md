---
title: House-Sales
date: 2024-12-25
author: Your Name
cell_count: 28
score: 25
---

```python
# !pip install kaggle
# https://medium.com/@pumaline/easy-analysis-of-your-data-and-ml-model-using-evidently-ai-830ef0c1c4fd
# https://xgboost.readthedocs.io/en/latest/python/python_api.html
```


```python
import pandas as pd
```


```python
df = pd.read_csv('~/datasets/kaggle/kc_house_data.csv')
```


```python
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>date</th>
      <th>price</th>
      <th>bedrooms</th>
      <th>bathrooms</th>
      <th>sqft_living</th>
      <th>sqft_lot</th>
      <th>floors</th>
      <th>waterfront</th>
      <th>view</th>
      <th>...</th>
      <th>grade</th>
      <th>sqft_above</th>
      <th>sqft_basement</th>
      <th>yr_built</th>
      <th>yr_renovated</th>
      <th>zipcode</th>
      <th>lat</th>
      <th>long</th>
      <th>sqft_living15</th>
      <th>sqft_lot15</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>7129300520</td>
      <td>20141013T000000</td>
      <td>221900.0</td>
      <td>3</td>
      <td>1.00</td>
      <td>1180</td>
      <td>5650</td>
      <td>1.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>7</td>
      <td>1180</td>
      <td>0</td>
      <td>1955</td>
      <td>0</td>
      <td>98178</td>
      <td>47.5112</td>
      <td>-122.257</td>
      <td>1340</td>
      <td>5650</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6414100192</td>
      <td>20141209T000000</td>
      <td>538000.0</td>
      <td>3</td>
      <td>2.25</td>
      <td>2570</td>
      <td>7242</td>
      <td>2.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>7</td>
      <td>2170</td>
      <td>400</td>
      <td>1951</td>
      <td>1991</td>
      <td>98125</td>
      <td>47.7210</td>
      <td>-122.319</td>
      <td>1690</td>
      <td>7639</td>
    </tr>
    <tr>
      <th>2</th>
      <td>5631500400</td>
      <td>20150225T000000</td>
      <td>180000.0</td>
      <td>2</td>
      <td>1.00</td>
      <td>770</td>
      <td>10000</td>
      <td>1.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>6</td>
      <td>770</td>
      <td>0</td>
      <td>1933</td>
      <td>0</td>
      <td>98028</td>
      <td>47.7379</td>
      <td>-122.233</td>
      <td>2720</td>
      <td>8062</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2487200875</td>
      <td>20141209T000000</td>
      <td>604000.0</td>
      <td>4</td>
      <td>3.00</td>
      <td>1960</td>
      <td>5000</td>
      <td>1.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>7</td>
      <td>1050</td>
      <td>910</td>
      <td>1965</td>
      <td>0</td>
      <td>98136</td>
      <td>47.5208</td>
      <td>-122.393</td>
      <td>1360</td>
      <td>5000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1954400510</td>
      <td>20150218T000000</td>
      <td>510000.0</td>
      <td>3</td>
      <td>2.00</td>
      <td>1680</td>
      <td>8080</td>
      <td>1.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>8</td>
      <td>1680</td>
      <td>0</td>
      <td>1987</td>
      <td>0</td>
      <td>98074</td>
      <td>47.6168</td>
      <td>-122.045</td>
      <td>1800</td>
      <td>7503</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 21 columns</p>
</div>




```python
df[['grade','view','waterfront']] = df[['grade', 'view', 'waterfront']].astype('object')
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>date</th>
      <th>price</th>
      <th>bedrooms</th>
      <th>bathrooms</th>
      <th>sqft_living</th>
      <th>sqft_lot</th>
      <th>floors</th>
      <th>waterfront</th>
      <th>view</th>
      <th>...</th>
      <th>grade</th>
      <th>sqft_above</th>
      <th>sqft_basement</th>
      <th>yr_built</th>
      <th>yr_renovated</th>
      <th>zipcode</th>
      <th>lat</th>
      <th>long</th>
      <th>sqft_living15</th>
      <th>sqft_lot15</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>7129300520</td>
      <td>20141013T000000</td>
      <td>221900.0</td>
      <td>3</td>
      <td>1.00</td>
      <td>1180</td>
      <td>5650</td>
      <td>1.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>7</td>
      <td>1180</td>
      <td>0</td>
      <td>1955</td>
      <td>0</td>
      <td>98178</td>
      <td>47.5112</td>
      <td>-122.257</td>
      <td>1340</td>
      <td>5650</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6414100192</td>
      <td>20141209T000000</td>
      <td>538000.0</td>
      <td>3</td>
      <td>2.25</td>
      <td>2570</td>
      <td>7242</td>
      <td>2.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>7</td>
      <td>2170</td>
      <td>400</td>
      <td>1951</td>
      <td>1991</td>
      <td>98125</td>
      <td>47.7210</td>
      <td>-122.319</td>
      <td>1690</td>
      <td>7639</td>
    </tr>
    <tr>
      <th>2</th>
      <td>5631500400</td>
      <td>20150225T000000</td>
      <td>180000.0</td>
      <td>2</td>
      <td>1.00</td>
      <td>770</td>
      <td>10000</td>
      <td>1.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>6</td>
      <td>770</td>
      <td>0</td>
      <td>1933</td>
      <td>0</td>
      <td>98028</td>
      <td>47.7379</td>
      <td>-122.233</td>
      <td>2720</td>
      <td>8062</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2487200875</td>
      <td>20141209T000000</td>
      <td>604000.0</td>
      <td>4</td>
      <td>3.00</td>
      <td>1960</td>
      <td>5000</td>
      <td>1.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>7</td>
      <td>1050</td>
      <td>910</td>
      <td>1965</td>
      <td>0</td>
      <td>98136</td>
      <td>47.5208</td>
      <td>-122.393</td>
      <td>1360</td>
      <td>5000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1954400510</td>
      <td>20150218T000000</td>
      <td>510000.0</td>
      <td>3</td>
      <td>2.00</td>
      <td>1680</td>
      <td>8080</td>
      <td>1.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>8</td>
      <td>1680</td>
      <td>0</td>
      <td>1987</td>
      <td>0</td>
      <td>98074</td>
      <td>47.6168</td>
      <td>-122.045</td>
      <td>1800</td>
      <td>7503</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 21 columns</p>
</div>




```python
features = ['sqft_living','grade', 'sqft_above', 'sqft_living15', 'bathrooms','view','sqft_basement','lat','long','waterfront', 'yr_built','bedrooms']
```


```python
ref_data = df[:15000]
prod_data = df[15000:]
```


```python
from sklearn import model_selection
```


```python
# Delete entry with 33 bedrooms
df = df[df["bedrooms"] != 33]

# Create training and validation set
X_train, X_val, y_train, y_val = model_selection.train_test_split(ref_data[features], ref_data['price'],
                 test_size=0.2, shuffle=True, random_state=42)
```


```python
from sklearn.preprocessing import StandardScaler, OneHotEncoder
```


```python
# one-hot encode categorical variables
categorical = ['grade', 'view', 'waterfront']
ohe = OneHotEncoder(handle_unknown = 'ignore')
ohe = ohe.fit(X_train[categorical])
```


```python
def preprocessing(X, y, ohe):
    
    # Convert grade, view, waterfront to type object
    X[['grade','view','waterfront']] = X[['grade','view','waterfront']].astype('object')
    
    # log transform the target varibale 
    y = np.log1p(y)
    
    # define categorical and numerical varibales 
    categorical = ['grade', 'view', 'waterfront']
    numerical = ['sqft_living', 'sqft_above', 'sqft_living15',
           'bathrooms','sqft_basement','lat','long',
           'yr_built','bedrooms']
    
    # one-hot encode categorical variables
    X_cat = ohe.transform(X[categorical]).toarray()
    
    # define numerical columns 
    X_num = np.array(X[numerical])
    
    # concatenate numerical and categorical variables
    X = np.concatenate([X_cat, X_num], axis=1)
    
    print('Shape after one-hot encoding')
    print(f'X shape: {X.shape}')
    
    return X, y
```


```python
import numpy as np
```


```python
X_train, y_train = preprocessing(X_train, y_train, ohe)
X_val, y_val = preprocessing(X_val, y_val, ohe)
X_prod, y_prod = preprocessing(prod_data[features],  prod_data['price'], ohe)
```

    Shape after one-hot encoding
    X shape: (12000, 27)
    Shape after one-hot encoding
    X shape: (3000, 27)
    Shape after one-hot encoding
    X shape: (6613, 27)


    /tmp/ipykernel_993006/2150309139.py:4: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
      X[['grade','view','waterfront']] = X[['grade','view','waterfront']].astype('object')



```python
# !pip install xgboost
```


```python
import xgboost as xgb
from sklearn.metrics import mean_squared_error
```


```python
# Initialize XGB with objective function
parameters = {"objective": 'reg:squarederror',
              "n_estimators": 100,
              "verbosity": 0}

model = xgb.XGBRegressor(**parameters)
model.fit(X_train, y_train)
    
# generate predictions
y_pred_train = model.predict(X_train).reshape(-1,1)
y_pred = model.predict(X_val).reshape(-1,1)
    
# calculate errors
rmse_train = mean_squared_error(y_pred_train, y_train, squared=False)
rmse_val = mean_squared_error(y_pred, y_val, squared=False)
print(f"rmse training: {rmse_train:.3f}\t rmse validation: {rmse_val:.3f}")
```

    rmse training: 0.114	 rmse validation: 0.185


    /home/rajaraman/miniconda3/envs/ml3105/lib/python3.10/site-packages/sklearn/metrics/_regression.py:492: FutureWarning: 'squared' is deprecated in version 1.4 and will be removed in 1.6. To calculate the root mean squared error, use the function'root_mean_squared_error'.
      warnings.warn(
    /home/rajaraman/miniconda3/envs/ml3105/lib/python3.10/site-packages/sklearn/metrics/_regression.py:492: FutureWarning: 'squared' is deprecated in version 1.4 and will be removed in 1.6. To calculate the root mean squared error, use the function'root_mean_squared_error'.
      warnings.warn(



```python
X_train_full, y_train_full = preprocessing(ref_data[features], ref_data['price'], ohe)
ref_data['prediction'] = model.predict(X_train_full)
prod_data['prediction'] = model.predict(X_prod)
ref_data['price_log'] = np.log1p(ref_data['price'])
prod_data['price_log'] = np.log1p(prod_data['price'])
```

    Shape after one-hot encoding
    X shape: (15000, 27)


    /tmp/ipykernel_993006/2150309139.py:4: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
      X[['grade','view','waterfront']] = X[['grade','view','waterfront']].astype('object')



```python
# !pip install evidently==0.1.50.dev0
```


```python
import evidently

evidently.__version__
```




    '0.1.50.dev0'




```python
# !conda uninstall -y numpy
```


```python
# !pip install numpy==1.26.3 --force
import numpy
numpy.__version__
```




    '1.26.3'




```python

```


```python

```


```python
from evidently.dashboard import Dashboard
from evidently.pipeline.column_mapping import ColumnMapping
# packages for interactive dashboards
from evidently.dashboard.tabs import (
     DataDriftTab, 
     DataQualityTab, 
     NumTargetDriftTab, 
     RegressionPerformanceTab
    )
# packages for json-profiles
from evidently.model_profile import Profile
from evidently.model_profile.sections import (  
     DataDriftProfileSection, 
     DataQualityProfileSection, 
     NumTargetDriftProfileSection,
     RegressionPerformanceProfileSection
)
```

    /home/rajaraman/miniconda3/envs/ml3105/lib/python3.10/site-packages/evidently/utils/numpy_encoder.py:14: FutureWarning: In the future `np.bool` will be defined as the corresponding NumPy scalar.
      ((np.bool, np.bool_), bool),



    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    Cell In[23], line 1
    ----> 1 from evidently.dashboard import Dashboard
          2 from evidently.pipeline.column_mapping import ColumnMapping
          3 # packages for interactive dashboards


    File ~/miniconda3/envs/ml3105/lib/python3.10/site-packages/evidently/dashboard/__init__.py:4
          1 #!/usr/bin/env python
          2 # coding: utf-8
    ----> 4 from .dashboard import Dashboard


    File ~/miniconda3/envs/ml3105/lib/python3.10/site-packages/evidently/dashboard/dashboard.py:19
         17 from evidently.pipeline.column_mapping import ColumnMapping
         18 from evidently.dashboard.tabs.base_tab import Tab
    ---> 19 from evidently.utils import NumpyEncoder
         22 @dataclasses.dataclass()
         23 class TemplateParams:
         24     dashboard_id: str


    File ~/miniconda3/envs/ml3105/lib/python3.10/site-packages/evidently/utils/__init__.py:1
    ----> 1 from .numpy_encoder import NumpyEncoder


    File ~/miniconda3/envs/ml3105/lib/python3.10/site-packages/evidently/utils/numpy_encoder.py:14
          3 import numpy as np
          4 import pandas as pd
          7 _TYPES_MAPPING = (
          8     (
          9         (np.int_, np.intc, np.intp, np.int8, np.int16, np.int32, np.int64, np.uint8, np.uint16, np.uint32, np.uint64),
         10         int,
         11     ),
         12     ((np.float_, np.float16, np.float32, np.float64), float),
         13     ((np.ndarray,), lambda obj: obj.tolist()),
    ---> 14     ((np.bool, np.bool_), bool),
         15     ((pd.Timestamp, pd.Timedelta), str),
         16     ((np.void, type(pd.NaT)), lambda obj: None),
         17 )
         20 class NumpyEncoder(json.JSONEncoder):
         21     """Numpy and Pandas data types to JSON types encoder"""


    File ~/miniconda3/envs/ml3105/lib/python3.10/site-packages/numpy/__init__.py:324, in __getattr__(attr)
        319     warnings.warn(
        320         f"In the future `np.{attr}` will be defined as the "
        321         "corresponding NumPy scalar.", FutureWarning, stacklevel=2)
        323 if attr in __former_attrs__:
    --> 324     raise AttributeError(__former_attrs__[attr])
        326 if attr == 'testing':
        327     import numpy.testing as testing


    AttributeError: module 'numpy' has no attribute 'bool'.
    `np.bool` was a deprecated alias for the builtin `bool`. To avoid this error in existing code, use `bool` by itself. Doing this will not modify any behavior and is safe. If you specifically wanted the numpy scalar type, use `np.bool_` here.
    The aliases was originally deprecated in NumPy 1.20; for more details and guidance see the original release note at:
        https://numpy.org/devdocs/release/1.20.0-notes.html#deprecations



```python

```


```python

```


```python

```


---
**Score: 25**