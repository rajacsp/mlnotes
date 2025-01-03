---
title: Data-2-Csv-Xlsx
date: 2025-01-03
author: Your Name
cell_count: 14
score: 10
---

```python

```


```python
import pyutil as pyu
pyu.get_local_pyinfo()
```




    'conda env: ml312-2024; pyv: 3.12.7 | packaged by Anaconda, Inc. | (main, Oct  4 2024, 13:27:36) [GCC 11.2.0]'




```python
print(pyu.ps2("pandas faker"))
```

    pandas==2.2.3
    faker==33.1.0
    



```python

```


```python
from faker import Faker
import pandas as pd
```


```python
fake = Faker()
```


```python
rows_count = 10
```


```python
data = {
    "Name": [fake.name() for _ in range(rows_count)],
    "Email": [fake.email() for _ in range(rows_count)],
    "City": [fake.city() for _ in range(rows_count)],
    "Country": [fake.country() for _ in range(rows_count)]
}
```


```python
# data
```


```python
df = pd.DataFrame(data)
```


```python
df.index = df.index + 1
```


```python
df.index.name = 'Index'
```


```python
df.to_csv('fake_data_1.csv', index=True)
```


```python

```


---
**Score: 10**