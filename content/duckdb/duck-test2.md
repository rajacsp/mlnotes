---
title: Duck-Test2
date: 2025-05-17
author: Your Name
cell_count: 18
score: 15
---

```python
# https://rajasgs.gitbook.io/pynotes/gcp#data-modeling
# https://github.com/tactlabs/student-hiring-prediction-mle/tree/main/dataset
```


```python
import pyutil as pyu
pyu.get_local_pyinfo()
```




    'conda env: ml311; pyv: 3.11.10 (main, Oct  3 2024, 07:29:13) [GCC 11.2.0]'




```python
# !pip install duckdb
```


```python
!pip show duckdb | grep "Version:"
```

    Version: 1.1.3



```python
import duckdb
```


```python
# Connect to DuckDB
con = duckdb.connect()
```


```python
# Load CSV file
con.execute("CREATE TABLE my_table AS SELECT * FROM '../dataset/student_data.parquet'")
```




    <duckdb.duckdb.DuckDBPyConnection at 0x7f207c18c6b0>




```python
# Perform SQL query
result = con.execute("SELECT * FROM my_table WHERE student_name = 'Patricia Hall'").fetchall()
```


```python
result
```




    [(18, 'Patricia Hall', 71, 75, 70, 73, 0)]




```python
print(result)
```

    [(18, 'Patricia Hall', 71, 75, 70, 73, 0)]



```python
# type(result[0])
```


```python

import pandas as pd
from IPython.display import display

def list2table(cdata, col_list = None):

    first_row = cdata[0]
    cols_count = len(first_row)

    if not col_list:
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
def q(query, col_list = None):

    result = con.execute(query).fetchall()
    # print(result)

    return list2table(result, col_list)
```


```python
q("SELECT * FROM my_table WHERE student_id = 1")
```


<style type="text/css">
#T_471dc_row0_col0, #T_471dc_row0_col1, #T_471dc_row0_col2, #T_471dc_row0_col3, #T_471dc_row0_col4, #T_471dc_row0_col5, #T_471dc_row0_col6 {
  text-align: center;
}
</style>
<table id="T_471dc">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_471dc_level0_col0" class="col_heading level0 col0" >col_0</th>
      <th id="T_471dc_level0_col1" class="col_heading level0 col1" >col_1</th>
      <th id="T_471dc_level0_col2" class="col_heading level0 col2" >col_2</th>
      <th id="T_471dc_level0_col3" class="col_heading level0 col3" >col_3</th>
      <th id="T_471dc_level0_col4" class="col_heading level0 col4" >col_4</th>
      <th id="T_471dc_level0_col5" class="col_heading level0 col5" >col_5</th>
      <th id="T_471dc_level0_col6" class="col_heading level0 col6" >col_6</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_471dc_level0_row0" class="row_heading level0 row0" >0</th>
      <td id="T_471dc_row0_col0" class="data row0 col0" >1</td>
      <td id="T_471dc_row0_col1" class="data row0 col1" >John Doe</td>
      <td id="T_471dc_row0_col2" class="data row0 col2" >85</td>
      <td id="T_471dc_row0_col3" class="data row0 col3" >90</td>
      <td id="T_471dc_row0_col4" class="data row0 col4" >80</td>
      <td id="T_471dc_row0_col5" class="data row0 col5" >88</td>
      <td id="T_471dc_row0_col6" class="data row0 col6" >1</td>
    </tr>
  </tbody>
</table>




```python
q("""
SELECT 
STUDENT_NAME
FROM my_table
limit 2
""", ["student_name"])
```


<style type="text/css">
#T_12049_row0_col0, #T_12049_row1_col0 {
  text-align: center;
}
</style>
<table id="T_12049">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_12049_level0_col0" class="col_heading level0 col0" >student_name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_12049_level0_row0" class="row_heading level0 row0" >0</th>
      <td id="T_12049_row0_col0" class="data row0 col0" >John Doe</td>
    </tr>
    <tr>
      <th id="T_12049_level0_row1" class="row_heading level0 row1" >1</th>
      <td id="T_12049_row1_col0" class="data row1 col0" >Jane Smith</td>
    </tr>
  </tbody>
</table>




```python

```


```python

```


```python

```


---
**Score: 15**