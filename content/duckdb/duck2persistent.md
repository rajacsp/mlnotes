---
title: Duck2Persistent
date: 2025-01-04
author: Your Name
cell_count: 16
score: 15
---

```python

```


```python
import pyutil as pyu
pyu.get_local_pyinfo()
```




    'conda env: ml311; pyv: 3.11.10 (main, Oct  3 2024, 07:29:13) [GCC 11.2.0]'




```python
import duckdb
import pandas as pd
```


```python
# Path to your CSV file
csv_file_path = '../dataset/student_data.csv'
```


```python
# Create a DuckDB connection
con = duckdb.connect(database=':memory:', read_only=False)
```


```python
# Load the CSV file into a DuckDB table
con.execute(f"CREATE TABLE my_table AS SELECT * FROM read_csv_auto('{csv_file_path}')")
```




    <duckdb.duckdb.DuckDBPyConnection at 0x7fb9a0190070>




```python
# Optionally, you can query the table to verify the data
result = con.execute("SELECT * FROM my_table LIMIT 5").fetchdf()
print(result)
```

       student_id   student_name  test_scores  attendance  participation  \
    0           1       John Doe           85          90             80   
    1           2     Jane Smith           78          85             75   
    2           3    Bob Johnson           92          95             85   
    3           4    Alice Brown           70          80             70   
    4           5  Charlie Davis           88          92             83   
    
       project_scores  got_job  
    0              88        1  
    1              80        0  
    2              90        1  
    3              75        0  
    4              85        1  



```python
# Persist the data by saving the DuckDB database to a file
persisted_db_path = 'student_duck.db'
con.execute(f"COPY my_table TO '{persisted_db_path}' (FORMAT CSV)")
```




    <duckdb.duckdb.DuckDBPyConnection at 0x7fb9a0190070>




```python
# Close the connection
con.close()
```


```python
print(f"Data has been persisted to {persisted_db_path}")
```

    Data has been persisted to student_duck.db



```python

```


```python

```


```python
# read from persisted

# con = duckdb.connect(database='student_duck.db', read_only=False)
```


```python
# Create a new DuckDB database file
db_path = 'student_duck.db'
con = duckdb.connect(database=db_path, read_only=False)

# Verify the connection
print(f"Connected to DuckDB database at {db_path}")
```


    ---------------------------------------------------------------------------

    IOException                               Traceback (most recent call last)

    Cell In[39], line 3
          1 # Create a new DuckDB database file
          2 db_path = 'student_duck.db'
    ----> 3 con = duckdb.connect(database=db_path, read_only=True)
          5 # Verify the connection
          6 print(f"Connected to DuckDB database at {db_path}")


    IOException: IO Error: The file "/home/rajaraman/tprojects/mlnotes/notebooks/duckdb/student_duck.db" exists, but it is not a valid DuckDB database file!



```python

```


```python

```


---
**Score: 15**