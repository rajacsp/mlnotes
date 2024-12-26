---
title: Csv2Duckdb-Persist
date: 2024-12-26
author: Your Name
cell_count: 8
score: 5
---

```python

```


```python
import duckdb

# Create a new DuckDB database file
db_path = 'student_duck1.db'
con = duckdb.connect(database=db_path, read_only=False)

# Verify the connection
print(f"Connected to DuckDB database at {db_path}")
```

    Connected to DuckDB database at student_duck1.db



```python
# Path to your CSV file
csv_file_path = '../dataset/student_data.csv'

# Load the CSV file into a DuckDB table
con.execute(f"CREATE TABLE my_table AS SELECT * FROM read_csv_auto('{csv_file_path}')")

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
# Close the connection
con.close()

print(f"Data has been persisted to {db_path}")

```

    Data has been persisted to student_duck1.db



```python

```


```python

```


```python
# Reconnect to the persisted DuckDB database
con = duckdb.connect(database=db_path, read_only=False)

# Query the table to verify the data
result = con.execute("SELECT * FROM my_table LIMIT 5").fetchdf()
print(result)

# Close the connection
con.close()
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

```


---
**Score: 5**