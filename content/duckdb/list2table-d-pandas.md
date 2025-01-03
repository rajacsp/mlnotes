---
title: List2Table-D-Pandas
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

```python

```


```python
import pandas as pd
from IPython.display import display

# Example list of tuples
data = [
    (1, 'Alice', 25),
    (2, 'Bob', 30),
    (3, 'Charlie', 35)
]

# Convert the list of tuples to a DataFrame
df = pd.DataFrame(data, columns=['ID', 'Name', 'Age'])

# Set display options
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 100)

# Apply custom styling
styled_df = df.style.set_properties(**{'text-align': 'center'})

# Display the DataFrame
display(styled_df)
```


<style type="text/css">
#T_650ef_row0_col0, #T_650ef_row0_col1, #T_650ef_row0_col2, #T_650ef_row1_col0, #T_650ef_row1_col1, #T_650ef_row1_col2, #T_650ef_row2_col0, #T_650ef_row2_col1, #T_650ef_row2_col2 {
  text-align: center;
}
</style>
<table id="T_650ef">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_650ef_level0_col0" class="col_heading level0 col0" >ID</th>
      <th id="T_650ef_level0_col1" class="col_heading level0 col1" >Name</th>
      <th id="T_650ef_level0_col2" class="col_heading level0 col2" >Age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_650ef_level0_row0" class="row_heading level0 row0" >0</th>
      <td id="T_650ef_row0_col0" class="data row0 col0" >1</td>
      <td id="T_650ef_row0_col1" class="data row0 col1" >Alice</td>
      <td id="T_650ef_row0_col2" class="data row0 col2" >25</td>
    </tr>
    <tr>
      <th id="T_650ef_level0_row1" class="row_heading level0 row1" >1</th>
      <td id="T_650ef_row1_col0" class="data row1 col0" >2</td>
      <td id="T_650ef_row1_col1" class="data row1 col1" >Bob</td>
      <td id="T_650ef_row1_col2" class="data row1 col2" >30</td>
    </tr>
    <tr>
      <th id="T_650ef_level0_row2" class="row_heading level0 row2" >2</th>
      <td id="T_650ef_row2_col0" class="data row2 col0" >3</td>
      <td id="T_650ef_row2_col1" class="data row2 col1" >Charlie</td>
      <td id="T_650ef_row2_col2" class="data row2 col2" >35</td>
    </tr>
  </tbody>
</table>




```python
def list2table(cdata):

    first_row = cdata[0]
    cols_count = len(first_row)

    col_list = []
    for idx in range(cols_count):
        col_list.append(f'col_{idx}')

    # Convert the list of tuples to a DataFrame
    df1 = pd.DataFrame(cdata, columns = col_list)
    
    # Set display options
    pd.set_option('display.max_rows', 100)
    pd.set_option('display.max_columns', 100)
    
    # Apply custom styling
    styled_df = df1.style.set_properties(**{'text-align': 'center'})
    
    # Display the DataFrame
    display(styled_df)
```


```python
data1 = [
    (1, 'Raja', 25),
    (2, 'Bob', 30),
    (3, 'Charlie', 35)
]
```


```python
list2table(data1)
```


<style type="text/css">
#T_04695_row0_col0, #T_04695_row0_col1, #T_04695_row0_col2, #T_04695_row1_col0, #T_04695_row1_col1, #T_04695_row1_col2, #T_04695_row2_col0, #T_04695_row2_col1, #T_04695_row2_col2 {
  text-align: center;
}
</style>
<table id="T_04695">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_04695_level0_col0" class="col_heading level0 col0" >col_0</th>
      <th id="T_04695_level0_col1" class="col_heading level0 col1" >col_1</th>
      <th id="T_04695_level0_col2" class="col_heading level0 col2" >col_2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_04695_level0_row0" class="row_heading level0 row0" >0</th>
      <td id="T_04695_row0_col0" class="data row0 col0" >1</td>
      <td id="T_04695_row0_col1" class="data row0 col1" >Raja</td>
      <td id="T_04695_row0_col2" class="data row0 col2" >25</td>
    </tr>
    <tr>
      <th id="T_04695_level0_row1" class="row_heading level0 row1" >1</th>
      <td id="T_04695_row1_col0" class="data row1 col0" >2</td>
      <td id="T_04695_row1_col1" class="data row1 col1" >Bob</td>
      <td id="T_04695_row1_col2" class="data row1 col2" >30</td>
    </tr>
    <tr>
      <th id="T_04695_level0_row2" class="row_heading level0 row2" >2</th>
      <td id="T_04695_row2_col0" class="data row2 col0" >3</td>
      <td id="T_04695_row2_col1" class="data row2 col1" >Charlie</td>
      <td id="T_04695_row2_col2" class="data row2 col2" >35</td>
    </tr>
  </tbody>
</table>




```python

```


---
**Score: 5**