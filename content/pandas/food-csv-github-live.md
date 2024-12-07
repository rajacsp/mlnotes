---
title: Food-Csv-Github-Live
date: 2024-12-07
author: Your Name
cell_count: 13
score: 10
---

```python

```


```python
# https://github.com/rajacsp/public-dataset/blob/master/food.csv
```


```python
from io import BytesIO
```


```python
import requests
import pandas as pd
```


```python
FILEPATH = 'https://raw.githubusercontent.com/rajacsp/public-dataset/master/food.csv'
```


```python
r = requests.get(FILEPATH)
```


```python
data = r.content
```


```python
data
```




    b'Food_ID,Food_Name,Category,Price,Calories,Available\n1,Pizza,Fast Food,8.99,300,Yes\n2,Burger,Fast Food,5.49,450,Yes\n3,Pasta,Italian,7.99,400,No\n4,Sushi,Japanese,12.99,250,Yes\n5,Tacos,Mexican,6.99,200,No\n6,Salad,Healthy,4.99,150,Yes\n7,Fried Rice,Asian,5.99,350,Yes\n8,Ice Cream,Dessert,3.99,200,Yes\n9,Steak,Grill,14.99,700,No\n10,Soup,Healthy,3.49,100,Yes\n'




```python

```


```python
onlinedata = BytesIO(data)
```


```python
df = pd.read_csv(onlinedata, index_col=0)
```


```python
df.head(2)
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
      <th>Food_Name</th>
      <th>Category</th>
      <th>Price</th>
      <th>Calories</th>
      <th>Available</th>
    </tr>
    <tr>
      <th>Food_ID</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Pizza</td>
      <td>Fast Food</td>
      <td>8.99</td>
      <td>300</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Burger</td>
      <td>Fast Food</td>
      <td>5.49</td>
      <td>450</td>
      <td>Yes</td>
    </tr>
  </tbody>
</table>
</div>




```python

```


---
**Score: 10**