---
title: Int And Nan
date: 2024-12-03
author: Your Name
cell_count: 14
score: 10
---

---
title: "Int and NaN"
author: "Rj"
date: 2019-04-24
description: "-"
type: technical_note
draft: false
---

```python
import numpy as np
import pandas as pd
```


```python
df = pd.DataFrame({
    'one': [4, 5],
    'two': [10, 20]
})
```


```python
df
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
      <th>one</th>
      <th>two</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4</td>
      <td>10</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>20</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['one']+2
```




    0    6
    1    7
    Name: one, dtype: int64




```python
df['one'][0]
```




    4




```python
df['one'][0] = np.nan
```


```python
df['one'][0]
```




    nan




```python
df
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
      <th>one</th>
      <th>two</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>NaN</td>
      <td>10</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5.0</td>
      <td>20</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['one']+3
```




    0    NaN
    1    8.0
    Name: one, dtype: float64




```python
df['two'].astype('int')
```




    0    10
    1    20
    Name: two, dtype: int64




```python
df['one'].astype('int')
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-34-aa6d74a5a8d7> in <module>()
    ----> 1 df['one'].astype('int')
    

    ~/anaconda3/envs/py36/lib/python3.6/site-packages/pandas/core/generic.py in astype(self, dtype, copy, errors, **kwargs)
       5689             # else, only a single dtype is given
       5690             new_data = self._data.astype(dtype=dtype, copy=copy, errors=errors,
    -> 5691                                          **kwargs)
       5692             return self._constructor(new_data).__finalize__(self)
       5693 


    ~/anaconda3/envs/py36/lib/python3.6/site-packages/pandas/core/internals/managers.py in astype(self, dtype, **kwargs)
        529 
        530     def astype(self, dtype, **kwargs):
    --> 531         return self.apply('astype', dtype=dtype, **kwargs)
        532 
        533     def convert(self, **kwargs):


    ~/anaconda3/envs/py36/lib/python3.6/site-packages/pandas/core/internals/managers.py in apply(self, f, axes, filter, do_integrity_check, consolidate, **kwargs)
        393                                             copy=align_copy)
        394 
    --> 395             applied = getattr(b, f)(**kwargs)
        396             result_blocks = _extend_blocks(applied, result_blocks)
        397 


    ~/anaconda3/envs/py36/lib/python3.6/site-packages/pandas/core/internals/blocks.py in astype(self, dtype, copy, errors, values, **kwargs)
        532     def astype(self, dtype, copy=False, errors='raise', values=None, **kwargs):
        533         return self._astype(dtype, copy=copy, errors=errors, values=values,
    --> 534                             **kwargs)
        535 
        536     def _astype(self, dtype, copy=False, errors='raise', values=None,


    ~/anaconda3/envs/py36/lib/python3.6/site-packages/pandas/core/internals/blocks.py in _astype(self, dtype, copy, errors, values, **kwargs)
        631 
        632                     # _astype_nansafe works fine with 1-d only
    --> 633                     values = astype_nansafe(values.ravel(), dtype, copy=True)
        634 
        635                 # TODO(extension)


    ~/anaconda3/envs/py36/lib/python3.6/site-packages/pandas/core/dtypes/cast.py in astype_nansafe(arr, dtype, copy, skipna)
        674 
        675         if not np.isfinite(arr).all():
    --> 676             raise ValueError('Cannot convert non-finite values (NA or inf) to '
        677                              'integer')
        678 


    ValueError: Cannot convert non-finite values (NA or inf) to integer



```python
print (type(np.nan))
```

    <class 'float'>



```python

```


---
**Score: 10**