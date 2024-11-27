---
title: Astype 2
date: 2024-11-27
author: Your Name
cell_count: 13
score: 10
---

---
title: "Astype 2"
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
marks = [
    [90, 87],
    [90, 95],
    [92, 95]
]
```


```python
marks
```




    [[90, 87], [90, 95], [92, 95]]




```python
df = pd.DataFrame(marks, columns=['maths', 'science'])
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
      <th>maths</th>
      <th>science</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>90</td>
      <td>87</td>
    </tr>
    <tr>
      <th>1</th>
      <td>90</td>
      <td>95</td>
    </tr>
    <tr>
      <th>2</th>
      <td>92</td>
      <td>95</td>
    </tr>
  </tbody>
</table>
</div>




```python
# reassign some values to nan

df['maths']
```




    0    90
    1    90
    2    92
    Name: maths, dtype: int64




```python
df['maths'][0] = np.nan
```


```python
df['maths']
```




    0     NaN
    1    90.0
    2    92.0
    Name: maths, dtype: float64




```python
df = df.astype('int') # this will throw error
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-27-b2504c49b1a1> in <module>()
    ----> 1 df = df.astype('int') # this will throw error
    

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
df = df.fillna(0).astype('int') # this will throw error
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
      <th>maths</th>
      <th>science</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>87</td>
    </tr>
    <tr>
      <th>1</th>
      <td>90</td>
      <td>95</td>
    </tr>
    <tr>
      <th>2</th>
      <td>92</td>
      <td>95</td>
    </tr>
  </tbody>
</table>
</div>




```python

```


---
**Score: 10**