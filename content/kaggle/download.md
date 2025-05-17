---
title: Download
date: 2025-05-17
author: Your Name
cell_count: 8
score: 5
---

```python
import os
import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi
from io import BytesIO
import zipfile
```


```python
# Authenticate with Kaggle
api = KaggleApi()
api.authenticate()
```


```python
!kaggle datasets files zillow/zecon
```

    name                           size  creationDate         
    ----------------------------  -----  -------------------  
    City_time_series.csv          658MB  2019-09-21 10:26:35  
    CountyCrossWalk_Zillow.csv    227KB  2019-09-21 10:26:18  
    County_time_series.csv        108MB  2019-09-21 10:26:21  
    DataDictionary.csv              5KB  2019-09-21 10:26:18  
    Metro_time_series.csv          54MB  2019-09-21 10:26:19  
    Neighborhood_time_series.csv  253MB  2019-09-21 10:26:23  
    State_time_series.csv           5MB  2019-09-21 10:26:18  
    Zip_time_series.csv           746MB  2019-09-21 10:26:43  
    all_available_metrics.json      3KB  2019-09-21 10:26:27  
    cities_crosswalk.csv            1MB  2019-09-21 10:26:27  
    fields_per_level.json          17KB  2019-09-21 10:26:27  



```python
!kaggle datasets files harlfoxem/housesalesprediction
```

    name               size  creationDate         
    -----------------  ----  -------------------  
    kc_house_data.csv   2MB  2017-04-15 05:48:17  



```python
# Specify the dataset
dataset_name = 'harlfoxem/housesalesprediction'  # Replace with the dataset slug
file_name = 'kc_house_data'  # File within the dataset zip
```


```python
# Download the dataset as a stream
print("Downloading dataset...")
dataset = api.dataset_download_file(dataset_name, file_name=file_name)
```

    Downloading dataset...
    Dataset URL: https://www.kaggle.com/datasets/harlfoxem/housesalesprediction



```python
# Open the ZIP file in memory
print("Extracting and processing dataset...")
with zipfile.ZipFile(dataset_path, 'r') as z:
    if file_name in z.namelist():
        with z.open(file_name) as file:
            data = pd.read_csv(file)
            print(data.head())
    else:
        print(f"File {file_name} not found in the dataset!")
```


```python

```


---
**Score: 5**