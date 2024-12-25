---
title: Show-Negative-Values-Red
date: 2024-12-25
author: Your Name
cell_count: 15
score: 15
---

---
title: "Show Negative values red"
author: "Rj"
date: 2019-09-05
description: "List Test"
type: technical_note
draft: false
---

```python
import pandas as pd
```


```python
data = {
    'Month' : [1, 2, 3],
    'Temp' : [7, -18, -20]
}
```


```python
data
```




    {'Month': [1, 2, 3], 'Temp': [7, -18, -20]}




```python
type(data)
```




    dict




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
      <th>Month</th>
      <th>Temp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>7</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>-18</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>-20</td>
    </tr>
  </tbody>
</table>
</div>




```python
def color_negative_red(val):
    """
    Takes a scalar and returns a string with
    the css property `'color: red'` for negative
    strings, black otherwise.
    """
    color = 'red' if val < 0 else 'black'
    return 'color: %s' % color
```


```python
df.style.applymap(color_negative_red)
```




<style  type="text/css" >
#T_fe8d9290_efe7_11ea_a05d_38f9d3497ee0row0_col0,#T_fe8d9290_efe7_11ea_a05d_38f9d3497ee0row0_col1,#T_fe8d9290_efe7_11ea_a05d_38f9d3497ee0row1_col0,#T_fe8d9290_efe7_11ea_a05d_38f9d3497ee0row2_col0{
            color:  black;
        }#T_fe8d9290_efe7_11ea_a05d_38f9d3497ee0row1_col1,#T_fe8d9290_efe7_11ea_a05d_38f9d3497ee0row2_col1{
            color:  red;
        }</style><table id="T_fe8d9290_efe7_11ea_a05d_38f9d3497ee0" ><thead>    <tr>        <th class="blank level0" ></th>        <th class="col_heading level0 col0" >Month</th>        <th class="col_heading level0 col1" >Temp</th>    </tr></thead><tbody>
                <tr>
                        <th id="T_fe8d9290_efe7_11ea_a05d_38f9d3497ee0level0_row0" class="row_heading level0 row0" >0</th>
                        <td id="T_fe8d9290_efe7_11ea_a05d_38f9d3497ee0row0_col0" class="data row0 col0" >1</td>
                        <td id="T_fe8d9290_efe7_11ea_a05d_38f9d3497ee0row0_col1" class="data row0 col1" >7</td>
            </tr>
            <tr>
                        <th id="T_fe8d9290_efe7_11ea_a05d_38f9d3497ee0level0_row1" class="row_heading level0 row1" >1</th>
                        <td id="T_fe8d9290_efe7_11ea_a05d_38f9d3497ee0row1_col0" class="data row1 col0" >2</td>
                        <td id="T_fe8d9290_efe7_11ea_a05d_38f9d3497ee0row1_col1" class="data row1 col1" >-18</td>
            </tr>
            <tr>
                        <th id="T_fe8d9290_efe7_11ea_a05d_38f9d3497ee0level0_row2" class="row_heading level0 row2" >2</th>
                        <td id="T_fe8d9290_efe7_11ea_a05d_38f9d3497ee0row2_col0" class="data row2 col0" >3</td>
                        <td id="T_fe8d9290_efe7_11ea_a05d_38f9d3497ee0row2_col1" class="data row2 col1" >-20</td>
            </tr>
    </tbody></table>




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
      <th>Month</th>
      <th>Temp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>7</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>-18</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>-20</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Highlight max (axis = 0)
# https://pandas.pydata.org/pandas-docs/stable/user_guide/style.html

df.style.highlight_max(axis = 0)
```




<style  type="text/css" >
#T_ff5ba95a_efe7_11ea_a05d_38f9d3497ee0row0_col1,#T_ff5ba95a_efe7_11ea_a05d_38f9d3497ee0row2_col0{
            background-color:  yellow;
        }</style><table id="T_ff5ba95a_efe7_11ea_a05d_38f9d3497ee0" ><thead>    <tr>        <th class="blank level0" ></th>        <th class="col_heading level0 col0" >Month</th>        <th class="col_heading level0 col1" >Temp</th>    </tr></thead><tbody>
                <tr>
                        <th id="T_ff5ba95a_efe7_11ea_a05d_38f9d3497ee0level0_row0" class="row_heading level0 row0" >0</th>
                        <td id="T_ff5ba95a_efe7_11ea_a05d_38f9d3497ee0row0_col0" class="data row0 col0" >1</td>
                        <td id="T_ff5ba95a_efe7_11ea_a05d_38f9d3497ee0row0_col1" class="data row0 col1" >7</td>
            </tr>
            <tr>
                        <th id="T_ff5ba95a_efe7_11ea_a05d_38f9d3497ee0level0_row1" class="row_heading level0 row1" >1</th>
                        <td id="T_ff5ba95a_efe7_11ea_a05d_38f9d3497ee0row1_col0" class="data row1 col0" >2</td>
                        <td id="T_ff5ba95a_efe7_11ea_a05d_38f9d3497ee0row1_col1" class="data row1 col1" >-18</td>
            </tr>
            <tr>
                        <th id="T_ff5ba95a_efe7_11ea_a05d_38f9d3497ee0level0_row2" class="row_heading level0 row2" >2</th>
                        <td id="T_ff5ba95a_efe7_11ea_a05d_38f9d3497ee0row2_col0" class="data row2 col0" >3</td>
                        <td id="T_ff5ba95a_efe7_11ea_a05d_38f9d3497ee0row2_col1" class="data row2 col1" >-20</td>
            </tr>
    </tbody></table>




```python
def highlight_max_rj(s, color = 'lightgreen'):
    '''
    highlight the maximum in a Series yellow.
    '''
    is_max = s == s.max()
    return ['background-color: '+color if v else '' for v in is_max]
```


```python
df.style.apply(highlight_max_rj, color = 'lightblue',  axis = 0, subset=['Temp'])
```




<style  type="text/css" >
#T_07677b9c_efe8_11ea_a05d_38f9d3497ee0row0_col1{
            background-color:  lightblue;
        }</style><table id="T_07677b9c_efe8_11ea_a05d_38f9d3497ee0" ><thead>    <tr>        <th class="blank level0" ></th>        <th class="col_heading level0 col0" >Month</th>        <th class="col_heading level0 col1" >Temp</th>    </tr></thead><tbody>
                <tr>
                        <th id="T_07677b9c_efe8_11ea_a05d_38f9d3497ee0level0_row0" class="row_heading level0 row0" >0</th>
                        <td id="T_07677b9c_efe8_11ea_a05d_38f9d3497ee0row0_col0" class="data row0 col0" >1</td>
                        <td id="T_07677b9c_efe8_11ea_a05d_38f9d3497ee0row0_col1" class="data row0 col1" >7</td>
            </tr>
            <tr>
                        <th id="T_07677b9c_efe8_11ea_a05d_38f9d3497ee0level0_row1" class="row_heading level0 row1" >1</th>
                        <td id="T_07677b9c_efe8_11ea_a05d_38f9d3497ee0row1_col0" class="data row1 col0" >2</td>
                        <td id="T_07677b9c_efe8_11ea_a05d_38f9d3497ee0row1_col1" class="data row1 col1" >-18</td>
            </tr>
            <tr>
                        <th id="T_07677b9c_efe8_11ea_a05d_38f9d3497ee0level0_row2" class="row_heading level0 row2" >2</th>
                        <td id="T_07677b9c_efe8_11ea_a05d_38f9d3497ee0row2_col0" class="data row2 col0" >3</td>
                        <td id="T_07677b9c_efe8_11ea_a05d_38f9d3497ee0row2_col1" class="data row2 col1" >-20</td>
            </tr>
    </tbody></table>




```python
df.style.apply(highlight_max_rj, axis = 1, subset = ['Temp'])
```




<style  type="text/css" >
#T_1011fc5e_efe8_11ea_a05d_38f9d3497ee0row0_col1,#T_1011fc5e_efe8_11ea_a05d_38f9d3497ee0row1_col1,#T_1011fc5e_efe8_11ea_a05d_38f9d3497ee0row2_col1{
            background-color:  lightgreen;
        }</style><table id="T_1011fc5e_efe8_11ea_a05d_38f9d3497ee0" ><thead>    <tr>        <th class="blank level0" ></th>        <th class="col_heading level0 col0" >Month</th>        <th class="col_heading level0 col1" >Temp</th>    </tr></thead><tbody>
                <tr>
                        <th id="T_1011fc5e_efe8_11ea_a05d_38f9d3497ee0level0_row0" class="row_heading level0 row0" >0</th>
                        <td id="T_1011fc5e_efe8_11ea_a05d_38f9d3497ee0row0_col0" class="data row0 col0" >1</td>
                        <td id="T_1011fc5e_efe8_11ea_a05d_38f9d3497ee0row0_col1" class="data row0 col1" >7</td>
            </tr>
            <tr>
                        <th id="T_1011fc5e_efe8_11ea_a05d_38f9d3497ee0level0_row1" class="row_heading level0 row1" >1</th>
                        <td id="T_1011fc5e_efe8_11ea_a05d_38f9d3497ee0row1_col0" class="data row1 col0" >2</td>
                        <td id="T_1011fc5e_efe8_11ea_a05d_38f9d3497ee0row1_col1" class="data row1 col1" >-18</td>
            </tr>
            <tr>
                        <th id="T_1011fc5e_efe8_11ea_a05d_38f9d3497ee0level0_row2" class="row_heading level0 row2" >2</th>
                        <td id="T_1011fc5e_efe8_11ea_a05d_38f9d3497ee0row2_col0" class="data row2 col0" >3</td>
                        <td id="T_1011fc5e_efe8_11ea_a05d_38f9d3497ee0row2_col1" class="data row2 col1" >-20</td>
            </tr>
    </tbody></table>




```python

```


---
**Score: 15**