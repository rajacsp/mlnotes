---
title: Csv-Monitor
date: 2024-12-26
author: Your Name
cell_count: 5
score: 5
---

```python

```


```python
import pyutil as pyu
pyu.get_local_pyinfo()
```




    'conda env: ml311; pyv: 3.11.10 (main, Oct  3 2024, 07:29:13) [GCC 11.2.0]'




```python
print(pyu.ps2("haystack-ai ollama-haystack python-dotenv"))
```

    haystack-ai==2.8.0
    ollama-haystack is not installed in the current environment.
    python-dotenv==0.21.0
    



```python

```


```python
import pandas as pd
import time

# Filepath to the city.csv file
file_path = 'city.csv'

def monitor_csv(file_path):
    """Monitor the CSV file for changes and print the row count every 2 seconds."""
    previous_row_count = 0

    while True:
        try:
            # Read the CSV file
            df = pd.read_csv(file_path)
            current_row_count = len(df)

            # Check if the row count has changed
            if current_row_count != previous_row_count:
                print(f"{current_row_count} rows")
                previous_row_count = current_row_count
        except FileNotFoundError:
            print("File not found. Make sure the file exists.")
        except Exception as e:
            print(f"An error occurred: {e}")

        # Wait for 2 seconds before checking again
        time.sleep(2)

# Run the monitoring function
if __name__ == "__main__":
    monitor_csv(file_path)
```


---
**Score: 5**