---
title: Advanced-Custom-Lambda
date: 2024-12-14
author: Your Name
cell_count: 9
score: 5
---

---
title: "Advanced Custom Lambda"
author: "Rj"
date: 2019-04-22
description: "-"
type: technical_note
draft: false
---

```python
import numpy as np
import pandas as pd
```


```python
# Check the student passed either math or passed at least in 2 subjects. If no condidition matched, consider them as failed
def pass_math_or_two_subjects(row):
    if(row.maths > 34):
        return 'Pass'
    if(row.language > 34 and row.science > 34):
        return 'Pass'
    return 'Fail'
```


```python
df = pd.read_csv('abc.csv')
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
      <th>student</th>
      <th>language</th>
      <th>science</th>
      <th>maths</th>
      <th>history</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>kumar</td>
      <td>90</td>
      <td>56</td>
      <td>34</td>
      <td>34</td>
    </tr>
    <tr>
      <th>1</th>
      <td>kevin</td>
      <td>10</td>
      <td>34</td>
      <td>32</td>
      <td>67</td>
    </tr>
    <tr>
      <th>2</th>
      <td>sammy</td>
      <td>90</td>
      <td>23</td>
      <td>12</td>
      <td>32</td>
    </tr>
    <tr>
      <th>3</th>
      <td>janice</td>
      <td>20</td>
      <td>67</td>
      <td>90</td>
      <td>45</td>
    </tr>
    <tr>
      <th>4</th>
      <td>peter</td>
      <td>30</td>
      <td>56</td>
      <td>45</td>
      <td>65</td>
    </tr>
    <tr>
      <th>5</th>
      <td>prem</td>
      <td>90</td>
      <td>45</td>
      <td>45</td>
      <td>34</td>
    </tr>
    <tr>
      <th>6</th>
      <td>carrol</td>
      <td>50</td>
      <td>90</td>
      <td>45</td>
      <td>23</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['special_result'] = df.apply(pass_math_or_two_subjects, axis=1)
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
      <th>student</th>
      <th>language</th>
      <th>science</th>
      <th>maths</th>
      <th>history</th>
      <th>special_result</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>kumar</td>
      <td>90</td>
      <td>56</td>
      <td>34</td>
      <td>34</td>
      <td>Pass</td>
    </tr>
    <tr>
      <th>1</th>
      <td>kevin</td>
      <td>10</td>
      <td>34</td>
      <td>32</td>
      <td>67</td>
      <td>Fail</td>
    </tr>
    <tr>
      <th>2</th>
      <td>sammy</td>
      <td>90</td>
      <td>23</td>
      <td>12</td>
      <td>32</td>
      <td>Fail</td>
    </tr>
    <tr>
      <th>3</th>
      <td>janice</td>
      <td>20</td>
      <td>67</td>
      <td>90</td>
      <td>45</td>
      <td>Pass</td>
    </tr>
    <tr>
      <th>4</th>
      <td>peter</td>
      <td>30</td>
      <td>56</td>
      <td>45</td>
      <td>65</td>
      <td>Pass</td>
    </tr>
    <tr>
      <th>5</th>
      <td>prem</td>
      <td>90</td>
      <td>45</td>
      <td>45</td>
      <td>34</td>
      <td>Pass</td>
    </tr>
    <tr>
      <th>6</th>
      <td>carrol</td>
      <td>50</td>
      <td>90</td>
      <td>45</td>
      <td>23</td>
      <td>Pass</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Filter those candidates whoever passed the given criteria
df_passed = df[df.apply(pass_math_or_two_subjects, axis=1) == 'Pass']
```


```python
df_passed
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
      <th>student</th>
      <th>language</th>
      <th>science</th>
      <th>maths</th>
      <th>history</th>
      <th>special_result</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>kumar</td>
      <td>90</td>
      <td>56</td>
      <td>34</td>
      <td>34</td>
      <td>Pass</td>
    </tr>
    <tr>
      <th>3</th>
      <td>janice</td>
      <td>20</td>
      <td>67</td>
      <td>90</td>
      <td>45</td>
      <td>Pass</td>
    </tr>
    <tr>
      <th>4</th>
      <td>peter</td>
      <td>30</td>
      <td>56</td>
      <td>45</td>
      <td>65</td>
      <td>Pass</td>
    </tr>
    <tr>
      <th>5</th>
      <td>prem</td>
      <td>90</td>
      <td>45</td>
      <td>45</td>
      <td>34</td>
      <td>Pass</td>
    </tr>
    <tr>
      <th>6</th>
      <td>carrol</td>
      <td>50</td>
      <td>90</td>
      <td>45</td>
      <td>23</td>
      <td>Pass</td>
    </tr>
  </tbody>
</table>
</div>




---
**Score: 5**