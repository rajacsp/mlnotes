---
title: Col Match
date: 2025-01-04
author: Your Name
cell_count: 9
score: 5
---

```python

```


```python
import pyutil as pyu
pyu.get_local_pyinfo()
```




    'conda env: ml311; pyv: 3.11.10 (main, Oct  3 2024, 07:29:13) [GCC 11.2.0]'




```python
print(pyu.ps2("haystack-ai ollama-haystack python-dotenv"))
```

    haystack-ai==2.8.0
    ollama-haystack is not installed in the current environment.
    python-dotenv==0.21.0
    



```python

```


```python
import pandas as pd

# Sample DataFrame
data = {
    'Column1': [1, 2, 3, 4],
    'Column2': ['A', 'B', 'C', 'D']
}
df = pd.DataFrame(data)

# Value to match
value_to_match = 'E'

# Filter rows where the value in 'Column1' matches
matching_rows = df[df['Column2'] == value_to_match]

# Display the matching rows
print(matching_rows['Column1'].values)
```

    []



```python
def get_matched_index(df1, key):

    matching_rows = df1[df1['Column2'] == key]

    return matching_rows['Column1'].values[0] if len(matching_rows['Column1'].values) > 0 else -1
```


```python
get_matched_index(df, 'E')
```




    -1




```python

```


```python

```


---
**Score: 5**