---
title: Plotine-1
date: 2024-12-13
author: Your Name
cell_count: 7
score: 5
---

---
title: "Plotline Simple"
author: "Rj"
date: 2019-05-06
description: "List Test"
type: technical_note
draft: false
---

```python
import pandas as pd
import numpy as np

from plotnine import *

%matplotlib inline
```


```python
df = pd.DataFrame({
    'variable': ['gender', 'gender', 'age', 'age', 'age', 'income', 'income', 'income', 'income'],
    'category': ['Female', 'Male', '1-24', '25-54', '55+', 'Lo', 'Lo-Med', 'Med', 'High'],
    'value': [60, 40, 50, 30, 20, 10, 25, 25, 40],
})
df['variable'] = pd.Categorical(df['variable'], categories=['gender', 'age', 'income'])

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
      <th>variable</th>
      <th>category</th>
      <th>value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>gender</td>
      <td>Female</td>
      <td>60</td>
    </tr>
    <tr>
      <th>1</th>
      <td>gender</td>
      <td>Male</td>
      <td>40</td>
    </tr>
    <tr>
      <th>2</th>
      <td>age</td>
      <td>1-24</td>
      <td>50</td>
    </tr>
    <tr>
      <th>3</th>
      <td>age</td>
      <td>25-54</td>
      <td>30</td>
    </tr>
    <tr>
      <th>4</th>
      <td>age</td>
      <td>55+</td>
      <td>20</td>
    </tr>
    <tr>
      <th>5</th>
      <td>income</td>
      <td>Lo</td>
      <td>10</td>
    </tr>
    <tr>
      <th>6</th>
      <td>income</td>
      <td>Lo-Med</td>
      <td>25</td>
    </tr>
    <tr>
      <th>7</th>
      <td>income</td>
      <td>Med</td>
      <td>25</td>
    </tr>
    <tr>
      <th>8</th>
      <td>income</td>
      <td>High</td>
      <td>40</td>
    </tr>
  </tbody>
</table>
</div>




```python
(ggplot(df, aes(x='variable', y='value', fill='category'))
 + geom_col()
)
```


    
![png](/mlnotes/images/plotine-1_3_0.png)
    





    <ggplot: (-9223372036571546280)>




```python
(ggplot(df, aes(x='variable', y='value', fill='category'))
 + geom_bar(stat='identity', position='dodge'))    
```


    
![png](/mlnotes/images/plotine-1_4_0.png)
    





    <ggplot: (316768548)>




```python
dodge_text = position_dodge(width=0.9)                              # new

(ggplot(df, aes(x='variable', y='value', fill='category'))
 + geom_bar(stat='identity', position='dodge', show_legend=False)   # modified
 + geom_text(aes(y=-.5, label='category'),                          # new
             position=dodge_text,
             color='gray', size=8, angle=45, va='top')
 + lims(y=(-5, 60))                                                 # new
)
```

    /Users/rajacsp/anaconda3/envs/py36/lib/python3.6/site-packages/plotnine/layer.py:517: MatplotlibDeprecationWarning: isinstance(..., numbers.Number)
      return not cbook.iterable(value) and (cbook.is_numlike(value) or



    
![png](/mlnotes/images/plotine-1_5_1.png)
    





    <ggplot: (316729208)>




```python

```


---
**Score: 5**