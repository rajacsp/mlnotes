---
title: Sum-Of-All
date: 2025-01-03
author: Your Name
cell_count: 8
score: 5
---

---
title: "Sum of All on NA"
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
df = pd.DataFrame(np.random.rand(10, 5))
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
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.051358</td>
      <td>0.465768</td>
      <td>0.998450</td>
      <td>0.131171</td>
      <td>0.997680</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.237126</td>
      <td>0.703764</td>
      <td>0.055986</td>
      <td>0.120710</td>
      <td>0.489311</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.364137</td>
      <td>0.449693</td>
      <td>0.803241</td>
      <td>0.905241</td>
      <td>0.271881</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.620432</td>
      <td>0.877218</td>
      <td>0.282262</td>
      <td>0.633186</td>
      <td>0.568208</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.070414</td>
      <td>0.098475</td>
      <td>0.811134</td>
      <td>0.125991</td>
      <td>0.547385</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.227223</td>
      <td>0.293223</td>
      <td>0.299701</td>
      <td>0.216877</td>
      <td>0.109066</td>
    </tr>
    <tr>
      <th>6</th>
      <td>0.806406</td>
      <td>0.615722</td>
      <td>0.780990</td>
      <td>0.354237</td>
      <td>0.075826</td>
    </tr>
    <tr>
      <th>7</th>
      <td>0.474298</td>
      <td>0.062300</td>
      <td>0.292121</td>
      <td>0.201447</td>
      <td>0.662283</td>
    </tr>
    <tr>
      <th>8</th>
      <td>0.935634</td>
      <td>0.699771</td>
      <td>0.814459</td>
      <td>0.444021</td>
      <td>0.131643</td>
    </tr>
    <tr>
      <th>9</th>
      <td>0.601526</td>
      <td>0.696834</td>
      <td>0.386316</td>
      <td>0.795693</td>
      <td>0.012131</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Apply some NA on the existing DF

df.iloc[0:3, 0:4] = np.nan
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
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.997680</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.489311</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.271881</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.620432</td>
      <td>0.877218</td>
      <td>0.282262</td>
      <td>0.633186</td>
      <td>0.568208</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.070414</td>
      <td>0.098475</td>
      <td>0.811134</td>
      <td>0.125991</td>
      <td>0.547385</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.227223</td>
      <td>0.293223</td>
      <td>0.299701</td>
      <td>0.216877</td>
      <td>0.109066</td>
    </tr>
    <tr>
      <th>6</th>
      <td>0.806406</td>
      <td>0.615722</td>
      <td>0.780990</td>
      <td>0.354237</td>
      <td>0.075826</td>
    </tr>
    <tr>
      <th>7</th>
      <td>0.474298</td>
      <td>0.062300</td>
      <td>0.292121</td>
      <td>0.201447</td>
      <td>0.662283</td>
    </tr>
    <tr>
      <th>8</th>
      <td>0.935634</td>
      <td>0.699771</td>
      <td>0.814459</td>
      <td>0.444021</td>
      <td>0.131643</td>
    </tr>
    <tr>
      <th>9</th>
      <td>0.601526</td>
      <td>0.696834</td>
      <td>0.386316</td>
      <td>0.795693</td>
      <td>0.012131</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.loc[:, 'test'] = df.iloc[:, 2:].sum(axis=1)
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
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>test</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.997680</td>
      <td>2.993039</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.489311</td>
      <td>1.467933</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.271881</td>
      <td>0.815643</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.620432</td>
      <td>0.877218</td>
      <td>0.282262</td>
      <td>0.633186</td>
      <td>0.568208</td>
      <td>5.328186</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.070414</td>
      <td>0.098475</td>
      <td>0.811134</td>
      <td>0.125991</td>
      <td>0.547385</td>
      <td>4.552009</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.227223</td>
      <td>0.293223</td>
      <td>0.299701</td>
      <td>0.216877</td>
      <td>0.109066</td>
      <td>2.170157</td>
    </tr>
    <tr>
      <th>6</th>
      <td>0.806406</td>
      <td>0.615722</td>
      <td>0.780990</td>
      <td>0.354237</td>
      <td>0.075826</td>
      <td>4.248881</td>
    </tr>
    <tr>
      <th>7</th>
      <td>0.474298</td>
      <td>0.062300</td>
      <td>0.292121</td>
      <td>0.201447</td>
      <td>0.662283</td>
      <td>3.529852</td>
    </tr>
    <tr>
      <th>8</th>
      <td>0.935634</td>
      <td>0.699771</td>
      <td>0.814459</td>
      <td>0.444021</td>
      <td>0.131643</td>
      <td>4.870143</td>
    </tr>
    <tr>
      <th>9</th>
      <td>0.601526</td>
      <td>0.696834</td>
      <td>0.386316</td>
      <td>0.795693</td>
      <td>0.012131</td>
      <td>4.279256</td>
    </tr>
  </tbody>
</table>
</div>




---
**Score: 5**