---
title: Astype-2
date: 2024-11-21
author: Your Name
cell_count: 12
score: 10
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

    IntCastingNaNError                        Traceback (most recent call last)

    Cell In[10], line 1
    ----> 1 df = df.astype('int') # this will throw error


    File ~/miniconda3/envs/ml312/lib/python3.12/site-packages/pandas/core/generic.py:6640, in NDFrame.astype(self, dtype, copy, errors)
       6634     results = [
       6635         ser.astype(dtype, copy=copy, errors=errors) for _, ser in self.items()
       6636     ]
       6638 else:
       6639     # else, only a single dtype is given
    -> 6640     new_data = self._mgr.astype(dtype=dtype, copy=copy, errors=errors)
       6641     res = self._constructor_from_mgr(new_data, axes=new_data.axes)
       6642     return res.__finalize__(self, method="astype")


    File ~/miniconda3/envs/ml312/lib/python3.12/site-packages/pandas/core/internals/managers.py:430, in BaseBlockManager.astype(self, dtype, copy, errors)
        427 elif using_copy_on_write():
        428     copy = False
    --> 430 return self.apply(
        431     "astype",
        432     dtype=dtype,
        433     copy=copy,
        434     errors=errors,
        435     using_cow=using_copy_on_write(),
        436 )


    File ~/miniconda3/envs/ml312/lib/python3.12/site-packages/pandas/core/internals/managers.py:363, in BaseBlockManager.apply(self, f, align_keys, **kwargs)
        361         applied = b.apply(f, **kwargs)
        362     else:
    --> 363         applied = getattr(b, f)(**kwargs)
        364     result_blocks = extend_blocks(applied, result_blocks)
        366 out = type(self).from_blocks(result_blocks, self.axes)


    File ~/miniconda3/envs/ml312/lib/python3.12/site-packages/pandas/core/internals/blocks.py:758, in Block.astype(self, dtype, copy, errors, using_cow, squeeze)
        755         raise ValueError("Can not squeeze with more than one column.")
        756     values = values[0, :]  # type: ignore[call-overload]
    --> 758 new_values = astype_array_safe(values, dtype, copy=copy, errors=errors)
        760 new_values = maybe_coerce_values(new_values)
        762 refs = None


    File ~/miniconda3/envs/ml312/lib/python3.12/site-packages/pandas/core/dtypes/astype.py:237, in astype_array_safe(values, dtype, copy, errors)
        234     dtype = dtype.numpy_dtype
        236 try:
    --> 237     new_values = astype_array(values, dtype, copy=copy)
        238 except (ValueError, TypeError):
        239     # e.g. _astype_nansafe can fail on object-dtype of strings
        240     #  trying to convert to float
        241     if errors == "ignore":


    File ~/miniconda3/envs/ml312/lib/python3.12/site-packages/pandas/core/dtypes/astype.py:182, in astype_array(values, dtype, copy)
        179     values = values.astype(dtype, copy=copy)
        181 else:
    --> 182     values = _astype_nansafe(values, dtype, copy=copy)
        184 # in pandas we don't store numpy str dtypes, so convert to object
        185 if isinstance(dtype, np.dtype) and issubclass(values.dtype.type, str):


    File ~/miniconda3/envs/ml312/lib/python3.12/site-packages/pandas/core/dtypes/astype.py:101, in _astype_nansafe(arr, dtype, copy, skipna)
         96     return lib.ensure_string_array(
         97         arr, skipna=skipna, convert_na_value=False
         98     ).reshape(shape)
        100 elif np.issubdtype(arr.dtype, np.floating) and dtype.kind in "iu":
    --> 101     return _astype_float_to_int_nansafe(arr, dtype, copy)
        103 elif arr.dtype == object:
        104     # if we have a datetime/timedelta array of objects
        105     # then coerce to datetime64[ns] and use DatetimeArray.astype
        107     if lib.is_np_dtype(dtype, "M"):


    File ~/miniconda3/envs/ml312/lib/python3.12/site-packages/pandas/core/dtypes/astype.py:145, in _astype_float_to_int_nansafe(values, dtype, copy)
        141 """
        142 astype with a check preventing converting NaN to an meaningless integer value.
        143 """
        144 if not np.isfinite(values).all():
    --> 145     raise IntCastingNaNError(
        146         "Cannot convert non-finite values (NA or inf) to integer"
        147     )
        148 if dtype.kind == "u":
        149     # GH#45151
        150     if not (values >= 0).all():


    IntCastingNaNError: Cannot convert non-finite values (NA or inf) to integer



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