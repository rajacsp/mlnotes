---
title: Seaborn-Pynotes-Growth
date: 2024-12-25
author: Your Name
cell_count: 20
score: 20
---

```python

```


```python

```


```python
# https://seaborn.pydata.org/installing.html
# https://stackabuse.com/seaborn-line-plot-tutorial-and-examples/
```


```python
!pip show seaborn | grep "Version:"
```

    Version: 0.13.2



```python
# !pip install seaborn
```


```python
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="darkgrid")

x = [
    0,
    220,
    380,
    500,
    540,
    540,
    590
]

sns.lineplot(x)
plt.show()
```


    
![png](/mlnotes/images/seaborn-pynotes-growth_5_0.png)
    



```python

```


```python

```


```python
import pandas as pd
```


```python
days_list = [
    1, 1, 1, 
    2, 2, 2,
    3, 3, 3
]
```


```python
learners_list = [
    'raja', 'hari', 'steve', 
    'raja', 'hari', 'steve',
    'raja', 'hari', 'steve'
]
```


```python
score_list = [
    0, 0, 0, 
    50, 40, 60,
    60, 45, 60
]
```


```python
data = {
    'days' : days_list,
    'learners' : learners_list,
    'score' : score_list
}

# 1949 Jan 112
# day:1 hari 0
# day:1 steve 0
```


```python
df = pd.DataFrame(data)
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
      <th>days</th>
      <th>learners</th>
      <th>score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>raja</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>hari</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>steve</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>raja</td>
      <td>50</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2</td>
      <td>hari</td>
      <td>40</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2</td>
      <td>steve</td>
      <td>60</td>
    </tr>
    <tr>
      <th>6</th>
      <td>3</td>
      <td>raja</td>
      <td>60</td>
    </tr>
    <tr>
      <th>7</th>
      <td>3</td>
      <td>hari</td>
      <td>45</td>
    </tr>
    <tr>
      <th>8</th>
      <td>3</td>
      <td>steve</td>
      <td>60</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_wide = df.pivot(index="days", columns="learners", values="score")
df_wide.head()
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
      <th>learners</th>
      <th>hari</th>
      <th>raja</th>
      <th>steve</th>
    </tr>
    <tr>
      <th>days</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>40</td>
      <td>50</td>
      <td>60</td>
    </tr>
    <tr>
      <th>3</th>
      <td>45</td>
      <td>60</td>
      <td>60</td>
    </tr>
  </tbody>
</table>
</div>




```python
import seaborn as sns
```


```python
sns.lineplot(data=df_wide)
```




    <Axes: xlabel='days'>




    
![png](/mlnotes/images/seaborn-pynotes-growth_17_1.png)
    



```python

```


```python

```


---
**Score: 20**