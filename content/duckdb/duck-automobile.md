---
title: Duck-Automobile
date: 2024-12-14
author: Your Name
cell_count: 22
score: 20
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
con.execute("CREATE TABLE automobile AS SELECT * FROM '../dataset/automobile_data.csv'")
```




    <duckdb.duckdb.DuckDBPyConnection at 0x7f2df2f47770>




```python
# Perform SQL query
result = con.execute("SELECT * FROM automobile").fetchall()
```


```python
# result
```


```python
# print(result)
```


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
q("SELECT * FROM automobile limit 2")
```


<style type="text/css">
#T_6651d_row0_col0, #T_6651d_row0_col1, #T_6651d_row0_col2, #T_6651d_row0_col3, #T_6651d_row0_col4, #T_6651d_row0_col5, #T_6651d_row0_col6, #T_6651d_row0_col7, #T_6651d_row0_col8, #T_6651d_row0_col9, #T_6651d_row0_col10, #T_6651d_row0_col11, #T_6651d_row0_col12, #T_6651d_row0_col13, #T_6651d_row0_col14, #T_6651d_row0_col15, #T_6651d_row0_col16, #T_6651d_row0_col17, #T_6651d_row0_col18, #T_6651d_row0_col19, #T_6651d_row0_col20, #T_6651d_row0_col21, #T_6651d_row0_col22, #T_6651d_row0_col23, #T_6651d_row0_col24, #T_6651d_row0_col25, #T_6651d_row1_col0, #T_6651d_row1_col1, #T_6651d_row1_col2, #T_6651d_row1_col3, #T_6651d_row1_col4, #T_6651d_row1_col5, #T_6651d_row1_col6, #T_6651d_row1_col7, #T_6651d_row1_col8, #T_6651d_row1_col9, #T_6651d_row1_col10, #T_6651d_row1_col11, #T_6651d_row1_col12, #T_6651d_row1_col13, #T_6651d_row1_col14, #T_6651d_row1_col15, #T_6651d_row1_col16, #T_6651d_row1_col17, #T_6651d_row1_col18, #T_6651d_row1_col19, #T_6651d_row1_col20, #T_6651d_row1_col21, #T_6651d_row1_col22, #T_6651d_row1_col23, #T_6651d_row1_col24, #T_6651d_row1_col25 {
  text-align: center;
}
</style>
<table id="T_6651d">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_6651d_level0_col0" class="col_heading level0 col0" >col_0</th>
      <th id="T_6651d_level0_col1" class="col_heading level0 col1" >col_1</th>
      <th id="T_6651d_level0_col2" class="col_heading level0 col2" >col_2</th>
      <th id="T_6651d_level0_col3" class="col_heading level0 col3" >col_3</th>
      <th id="T_6651d_level0_col4" class="col_heading level0 col4" >col_4</th>
      <th id="T_6651d_level0_col5" class="col_heading level0 col5" >col_5</th>
      <th id="T_6651d_level0_col6" class="col_heading level0 col6" >col_6</th>
      <th id="T_6651d_level0_col7" class="col_heading level0 col7" >col_7</th>
      <th id="T_6651d_level0_col8" class="col_heading level0 col8" >col_8</th>
      <th id="T_6651d_level0_col9" class="col_heading level0 col9" >col_9</th>
      <th id="T_6651d_level0_col10" class="col_heading level0 col10" >col_10</th>
      <th id="T_6651d_level0_col11" class="col_heading level0 col11" >col_11</th>
      <th id="T_6651d_level0_col12" class="col_heading level0 col12" >col_12</th>
      <th id="T_6651d_level0_col13" class="col_heading level0 col13" >col_13</th>
      <th id="T_6651d_level0_col14" class="col_heading level0 col14" >col_14</th>
      <th id="T_6651d_level0_col15" class="col_heading level0 col15" >col_15</th>
      <th id="T_6651d_level0_col16" class="col_heading level0 col16" >col_16</th>
      <th id="T_6651d_level0_col17" class="col_heading level0 col17" >col_17</th>
      <th id="T_6651d_level0_col18" class="col_heading level0 col18" >col_18</th>
      <th id="T_6651d_level0_col19" class="col_heading level0 col19" >col_19</th>
      <th id="T_6651d_level0_col20" class="col_heading level0 col20" >col_20</th>
      <th id="T_6651d_level0_col21" class="col_heading level0 col21" >col_21</th>
      <th id="T_6651d_level0_col22" class="col_heading level0 col22" >col_22</th>
      <th id="T_6651d_level0_col23" class="col_heading level0 col23" >col_23</th>
      <th id="T_6651d_level0_col24" class="col_heading level0 col24" >col_24</th>
      <th id="T_6651d_level0_col25" class="col_heading level0 col25" >col_25</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_6651d_level0_row0" class="row_heading level0 row0" >0</th>
      <td id="T_6651d_row0_col0" class="data row0 col0" >3</td>
      <td id="T_6651d_row0_col1" class="data row0 col1" >?</td>
      <td id="T_6651d_row0_col2" class="data row0 col2" >alfa-romero</td>
      <td id="T_6651d_row0_col3" class="data row0 col3" >gas</td>
      <td id="T_6651d_row0_col4" class="data row0 col4" >std</td>
      <td id="T_6651d_row0_col5" class="data row0 col5" >two</td>
      <td id="T_6651d_row0_col6" class="data row0 col6" >convertible</td>
      <td id="T_6651d_row0_col7" class="data row0 col7" >rwd</td>
      <td id="T_6651d_row0_col8" class="data row0 col8" >front</td>
      <td id="T_6651d_row0_col9" class="data row0 col9" >88.600000</td>
      <td id="T_6651d_row0_col10" class="data row0 col10" >168.800000</td>
      <td id="T_6651d_row0_col11" class="data row0 col11" >64.100000</td>
      <td id="T_6651d_row0_col12" class="data row0 col12" >48.800000</td>
      <td id="T_6651d_row0_col13" class="data row0 col13" >2548</td>
      <td id="T_6651d_row0_col14" class="data row0 col14" >dohc</td>
      <td id="T_6651d_row0_col15" class="data row0 col15" >four</td>
      <td id="T_6651d_row0_col16" class="data row0 col16" >130</td>
      <td id="T_6651d_row0_col17" class="data row0 col17" >mpfi</td>
      <td id="T_6651d_row0_col18" class="data row0 col18" >3.47</td>
      <td id="T_6651d_row0_col19" class="data row0 col19" >2.68</td>
      <td id="T_6651d_row0_col20" class="data row0 col20" >9.000000</td>
      <td id="T_6651d_row0_col21" class="data row0 col21" >111</td>
      <td id="T_6651d_row0_col22" class="data row0 col22" >5000</td>
      <td id="T_6651d_row0_col23" class="data row0 col23" >21</td>
      <td id="T_6651d_row0_col24" class="data row0 col24" >27</td>
      <td id="T_6651d_row0_col25" class="data row0 col25" >13495</td>
    </tr>
    <tr>
      <th id="T_6651d_level0_row1" class="row_heading level0 row1" >1</th>
      <td id="T_6651d_row1_col0" class="data row1 col0" >3</td>
      <td id="T_6651d_row1_col1" class="data row1 col1" >?</td>
      <td id="T_6651d_row1_col2" class="data row1 col2" >alfa-romero</td>
      <td id="T_6651d_row1_col3" class="data row1 col3" >gas</td>
      <td id="T_6651d_row1_col4" class="data row1 col4" >std</td>
      <td id="T_6651d_row1_col5" class="data row1 col5" >two</td>
      <td id="T_6651d_row1_col6" class="data row1 col6" >convertible</td>
      <td id="T_6651d_row1_col7" class="data row1 col7" >rwd</td>
      <td id="T_6651d_row1_col8" class="data row1 col8" >front</td>
      <td id="T_6651d_row1_col9" class="data row1 col9" >88.600000</td>
      <td id="T_6651d_row1_col10" class="data row1 col10" >168.800000</td>
      <td id="T_6651d_row1_col11" class="data row1 col11" >64.100000</td>
      <td id="T_6651d_row1_col12" class="data row1 col12" >48.800000</td>
      <td id="T_6651d_row1_col13" class="data row1 col13" >2548</td>
      <td id="T_6651d_row1_col14" class="data row1 col14" >dohc</td>
      <td id="T_6651d_row1_col15" class="data row1 col15" >four</td>
      <td id="T_6651d_row1_col16" class="data row1 col16" >130</td>
      <td id="T_6651d_row1_col17" class="data row1 col17" >mpfi</td>
      <td id="T_6651d_row1_col18" class="data row1 col18" >3.47</td>
      <td id="T_6651d_row1_col19" class="data row1 col19" >2.68</td>
      <td id="T_6651d_row1_col20" class="data row1 col20" >9.000000</td>
      <td id="T_6651d_row1_col21" class="data row1 col21" >111</td>
      <td id="T_6651d_row1_col22" class="data row1 col22" >5000</td>
      <td id="T_6651d_row1_col23" class="data row1 col23" >21</td>
      <td id="T_6651d_row1_col24" class="data row1 col24" >27</td>
      <td id="T_6651d_row1_col25" class="data row1 col25" >16500</td>
    </tr>
  </tbody>
</table>




```python

```


```python

```


```python

```


```python
q("""
SELECT 
    make, "num-of-doors", COUNT(*) AS door_count 
FROM automobile 

WHERE "num-of-doors" IN ('two', 'four')
GROUP BY 
    make,
    "num-of-doors"
LIMIT 2
""")
```


<style type="text/css">
#T_7568c_row0_col0, #T_7568c_row0_col1, #T_7568c_row0_col2, #T_7568c_row1_col0, #T_7568c_row1_col1, #T_7568c_row1_col2 {
  text-align: center;
}
</style>
<table id="T_7568c">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_7568c_level0_col0" class="col_heading level0 col0" >col_0</th>
      <th id="T_7568c_level0_col1" class="col_heading level0 col1" >col_1</th>
      <th id="T_7568c_level0_col2" class="col_heading level0 col2" >col_2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_7568c_level0_row0" class="row_heading level0 row0" >0</th>
      <td id="T_7568c_row0_col0" class="data row0 col0" >audi</td>
      <td id="T_7568c_row0_col1" class="data row0 col1" >two</td>
      <td id="T_7568c_row0_col2" class="data row0 col2" >2</td>
    </tr>
    <tr>
      <th id="T_7568c_level0_row1" class="row_heading level0 row1" >1</th>
      <td id="T_7568c_row1_col0" class="data row1 col0" >chevrolet</td>
      <td id="T_7568c_row1_col1" class="data row1 col1" >two</td>
      <td id="T_7568c_row1_col2" class="data row1 col2" >2</td>
    </tr>
  </tbody>
</table>




```python
q("""
SELECT *
FROM automobile
WHERE 
CAST(horsepower as INT) > 150
and horsepower != '?'

limit 2
""")
```


<style type="text/css">
#T_32b9a_row0_col0, #T_32b9a_row0_col1, #T_32b9a_row0_col2, #T_32b9a_row0_col3, #T_32b9a_row0_col4, #T_32b9a_row0_col5, #T_32b9a_row0_col6, #T_32b9a_row0_col7, #T_32b9a_row0_col8, #T_32b9a_row0_col9, #T_32b9a_row0_col10, #T_32b9a_row0_col11, #T_32b9a_row0_col12, #T_32b9a_row0_col13, #T_32b9a_row0_col14, #T_32b9a_row0_col15, #T_32b9a_row0_col16, #T_32b9a_row0_col17, #T_32b9a_row0_col18, #T_32b9a_row0_col19, #T_32b9a_row0_col20, #T_32b9a_row0_col21, #T_32b9a_row0_col22, #T_32b9a_row0_col23, #T_32b9a_row0_col24, #T_32b9a_row0_col25, #T_32b9a_row1_col0, #T_32b9a_row1_col1, #T_32b9a_row1_col2, #T_32b9a_row1_col3, #T_32b9a_row1_col4, #T_32b9a_row1_col5, #T_32b9a_row1_col6, #T_32b9a_row1_col7, #T_32b9a_row1_col8, #T_32b9a_row1_col9, #T_32b9a_row1_col10, #T_32b9a_row1_col11, #T_32b9a_row1_col12, #T_32b9a_row1_col13, #T_32b9a_row1_col14, #T_32b9a_row1_col15, #T_32b9a_row1_col16, #T_32b9a_row1_col17, #T_32b9a_row1_col18, #T_32b9a_row1_col19, #T_32b9a_row1_col20, #T_32b9a_row1_col21, #T_32b9a_row1_col22, #T_32b9a_row1_col23, #T_32b9a_row1_col24, #T_32b9a_row1_col25 {
  text-align: center;
}
</style>
<table id="T_32b9a">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_32b9a_level0_col0" class="col_heading level0 col0" >col_0</th>
      <th id="T_32b9a_level0_col1" class="col_heading level0 col1" >col_1</th>
      <th id="T_32b9a_level0_col2" class="col_heading level0 col2" >col_2</th>
      <th id="T_32b9a_level0_col3" class="col_heading level0 col3" >col_3</th>
      <th id="T_32b9a_level0_col4" class="col_heading level0 col4" >col_4</th>
      <th id="T_32b9a_level0_col5" class="col_heading level0 col5" >col_5</th>
      <th id="T_32b9a_level0_col6" class="col_heading level0 col6" >col_6</th>
      <th id="T_32b9a_level0_col7" class="col_heading level0 col7" >col_7</th>
      <th id="T_32b9a_level0_col8" class="col_heading level0 col8" >col_8</th>
      <th id="T_32b9a_level0_col9" class="col_heading level0 col9" >col_9</th>
      <th id="T_32b9a_level0_col10" class="col_heading level0 col10" >col_10</th>
      <th id="T_32b9a_level0_col11" class="col_heading level0 col11" >col_11</th>
      <th id="T_32b9a_level0_col12" class="col_heading level0 col12" >col_12</th>
      <th id="T_32b9a_level0_col13" class="col_heading level0 col13" >col_13</th>
      <th id="T_32b9a_level0_col14" class="col_heading level0 col14" >col_14</th>
      <th id="T_32b9a_level0_col15" class="col_heading level0 col15" >col_15</th>
      <th id="T_32b9a_level0_col16" class="col_heading level0 col16" >col_16</th>
      <th id="T_32b9a_level0_col17" class="col_heading level0 col17" >col_17</th>
      <th id="T_32b9a_level0_col18" class="col_heading level0 col18" >col_18</th>
      <th id="T_32b9a_level0_col19" class="col_heading level0 col19" >col_19</th>
      <th id="T_32b9a_level0_col20" class="col_heading level0 col20" >col_20</th>
      <th id="T_32b9a_level0_col21" class="col_heading level0 col21" >col_21</th>
      <th id="T_32b9a_level0_col22" class="col_heading level0 col22" >col_22</th>
      <th id="T_32b9a_level0_col23" class="col_heading level0 col23" >col_23</th>
      <th id="T_32b9a_level0_col24" class="col_heading level0 col24" >col_24</th>
      <th id="T_32b9a_level0_col25" class="col_heading level0 col25" >col_25</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_32b9a_level0_row0" class="row_heading level0 row0" >0</th>
      <td id="T_32b9a_row0_col0" class="data row0 col0" >1</td>
      <td id="T_32b9a_row0_col1" class="data row0 col1" >?</td>
      <td id="T_32b9a_row0_col2" class="data row0 col2" >alfa-romero</td>
      <td id="T_32b9a_row0_col3" class="data row0 col3" >gas</td>
      <td id="T_32b9a_row0_col4" class="data row0 col4" >std</td>
      <td id="T_32b9a_row0_col5" class="data row0 col5" >two</td>
      <td id="T_32b9a_row0_col6" class="data row0 col6" >hatchback</td>
      <td id="T_32b9a_row0_col7" class="data row0 col7" >rwd</td>
      <td id="T_32b9a_row0_col8" class="data row0 col8" >front</td>
      <td id="T_32b9a_row0_col9" class="data row0 col9" >94.500000</td>
      <td id="T_32b9a_row0_col10" class="data row0 col10" >171.200000</td>
      <td id="T_32b9a_row0_col11" class="data row0 col11" >65.500000</td>
      <td id="T_32b9a_row0_col12" class="data row0 col12" >52.400000</td>
      <td id="T_32b9a_row0_col13" class="data row0 col13" >2823</td>
      <td id="T_32b9a_row0_col14" class="data row0 col14" >ohcv</td>
      <td id="T_32b9a_row0_col15" class="data row0 col15" >six</td>
      <td id="T_32b9a_row0_col16" class="data row0 col16" >152</td>
      <td id="T_32b9a_row0_col17" class="data row0 col17" >mpfi</td>
      <td id="T_32b9a_row0_col18" class="data row0 col18" >2.68</td>
      <td id="T_32b9a_row0_col19" class="data row0 col19" >3.47</td>
      <td id="T_32b9a_row0_col20" class="data row0 col20" >9.000000</td>
      <td id="T_32b9a_row0_col21" class="data row0 col21" >154</td>
      <td id="T_32b9a_row0_col22" class="data row0 col22" >5000</td>
      <td id="T_32b9a_row0_col23" class="data row0 col23" >19</td>
      <td id="T_32b9a_row0_col24" class="data row0 col24" >26</td>
      <td id="T_32b9a_row0_col25" class="data row0 col25" >16500</td>
    </tr>
    <tr>
      <th id="T_32b9a_level0_row1" class="row_heading level0 row1" >1</th>
      <td id="T_32b9a_row1_col0" class="data row1 col0" >0</td>
      <td id="T_32b9a_row1_col1" class="data row1 col1" >?</td>
      <td id="T_32b9a_row1_col2" class="data row1 col2" >audi</td>
      <td id="T_32b9a_row1_col3" class="data row1 col3" >gas</td>
      <td id="T_32b9a_row1_col4" class="data row1 col4" >turbo</td>
      <td id="T_32b9a_row1_col5" class="data row1 col5" >two</td>
      <td id="T_32b9a_row1_col6" class="data row1 col6" >hatchback</td>
      <td id="T_32b9a_row1_col7" class="data row1 col7" >4wd</td>
      <td id="T_32b9a_row1_col8" class="data row1 col8" >front</td>
      <td id="T_32b9a_row1_col9" class="data row1 col9" >99.500000</td>
      <td id="T_32b9a_row1_col10" class="data row1 col10" >178.200000</td>
      <td id="T_32b9a_row1_col11" class="data row1 col11" >67.900000</td>
      <td id="T_32b9a_row1_col12" class="data row1 col12" >52.000000</td>
      <td id="T_32b9a_row1_col13" class="data row1 col13" >3053</td>
      <td id="T_32b9a_row1_col14" class="data row1 col14" >ohc</td>
      <td id="T_32b9a_row1_col15" class="data row1 col15" >five</td>
      <td id="T_32b9a_row1_col16" class="data row1 col16" >131</td>
      <td id="T_32b9a_row1_col17" class="data row1 col17" >mpfi</td>
      <td id="T_32b9a_row1_col18" class="data row1 col18" >3.13</td>
      <td id="T_32b9a_row1_col19" class="data row1 col19" >3.4</td>
      <td id="T_32b9a_row1_col20" class="data row1 col20" >7.000000</td>
      <td id="T_32b9a_row1_col21" class="data row1 col21" >160</td>
      <td id="T_32b9a_row1_col22" class="data row1 col22" >5500</td>
      <td id="T_32b9a_row1_col23" class="data row1 col23" >16</td>
      <td id="T_32b9a_row1_col24" class="data row1 col24" >22</td>
      <td id="T_32b9a_row1_col25" class="data row1 col25" >?</td>
    </tr>
  </tbody>
</table>




```python

```


```python
q("""
SELECT 
    ‘fuel-type’,
    make, 
    COUNT(*) AS number_cars
FROM automobile
WHERE 
'fuel-type' IN ('gas', 'diesel')

GROUP BY make, 'fuel-type'
""")
```


    ---------------------------------------------------------------------------

    BinderException                           Traceback (most recent call last)

    Cell In[35], line 1
    ----> 1 q("""
          2 SELECT 
          3     ‘fuel-type’,
          4     make, 
          5     COUNT(*) AS number_cars
          6 FROM automobile
          7 WHERE 
          8 'fuel-type' IN ('gas', 'diesel')
          9 
         10 GROUP BY make, 'fuel-type'
         11 """)


    Cell In[19], line 3, in q(query, col_list)
          1 def q(query, col_list = None):
    ----> 3     result = con.execute(query).fetchall()
          4     # print(result)
          6     return list2table(result, col_list)


    BinderException: Binder Error: Referenced column "‘fuel" not found in FROM clause!
    Candidate bindings: "automobile.fuel-type", "automobile.fuel-system"
    LINE 3:     ‘fuel-type’,
                ^



```python

```


---
**Score: 20**