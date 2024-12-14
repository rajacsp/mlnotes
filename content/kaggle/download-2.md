---
title: Download-2
date: 2024-12-14
author: Your Name
cell_count: 5
score: 5
---

```python

```


```python
# !pip install kagglehub
```


```python
import kagglehub

# Download latest version
path = kagglehub.dataset_download("harlfoxem/housesalesprediction")

print("Path to dataset files:", path)
```

    /home/rajaraman/miniconda3/envs/ml312/lib/python3.12/site-packages/tqdm/auto.py:21: TqdmWarning: IProgress not found. Please update jupyter and ipywidgets. See https://ipywidgets.readthedocs.io/en/stable/user_install.html
      from .autonotebook import tqdm as notebook_tqdm


    Downloading from https://www.kaggle.com/api/v1/datasets/download/harlfoxem/housesalesprediction?dataset_version_number=1...


    100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 780k/780k [00:01<00:00, 625kB/s]

    Extracting files...
    Path to dataset files: /home/rajaraman/.cache/kagglehub/datasets/harlfoxem/housesalesprediction/versions/1


    



```python
!ls -hal /home/rajaraman/.cache/kagglehub/datasets/harlfoxem/housesalesprediction/versions/1
```

    total 2.5M
    drwxrwxr-x 2 rajaraman rajaraman 4.0K Nov 17 13:13 .
    drwxrwxr-x 3 rajaraman rajaraman 4.0K Nov 17 13:13 ..
    -rw-rw-r-- 1 rajaraman rajaraman 2.4M Nov 17 13:13 kc_house_data.csv



```python

```


---
**Score: 5**