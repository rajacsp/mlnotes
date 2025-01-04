---
title: Pandas Version
date: 2025-01-04
author: Your Name
cell_count: 7
score: 5
---

---
title: "Pandas Version"
author: "Rj"
date: 2019-04-24
description: "-"
type: technical_note
draft: false
---

```python
import pandas as pd
```


```python
pd.__version__
```




    '0.24.2'




```python
pd.show_versions(as_json=False)
```

    
    INSTALLED VERSIONS
    ------------------
    commit: None
    python: 3.6.8.final.0
    python-bits: 64
    OS: Darwin
    OS-release: 18.5.0
    machine: x86_64
    processor: i386
    byteorder: little
    LC_ALL: None
    LANG: en_CA.UTF-8
    LOCALE: en_CA.UTF-8
    
    pandas: 0.24.2
    pytest: 4.5.0
    pip: 19.0.3
    setuptools: 40.8.0
    Cython: None
    numpy: 1.16.3
    scipy: 1.2.1
    pyarrow: None
    xarray: 0.12.1
    IPython: 6.2.1
    sphinx: None
    patsy: 0.5.1
    dateutil: 2.8.0
    pytz: 2019.1
    blosc: None
    bottleneck: None
    tables: None
    numexpr: None
    feather: None
    matplotlib: 3.0.3
    openpyxl: None
    xlrd: None
    xlwt: None
    xlsxwriter: None
    lxml.etree: 4.3.3
    bs4: 4.7.1
    html5lib: 1.0b10
    sqlalchemy: 1.3.3
    pymysql: None
    psycopg2: 2.8.2 (dt dec pq3 ext lo64)
    jinja2: 2.10.1
    s3fs: None
    fastparquet: None
    pandas_gbq: None
    pandas_datareader: 0.7.0
    gcsfs: None



```python
pd.show_versions(as_json=True)
```

    {'system': {'commit': None, 'python': '3.6.8.final.0', 'python-bits': 64, 'OS': 'Darwin', 'OS-release': '18.5.0', 'machine': 'x86_64', 'processor': 'i386', 'byteorder': 'little', 'LC_ALL': 'None', 'LANG': 'en_CA.UTF-8', 'LOCALE': 'en_CA.UTF-8'}, 'dependencies': {'pandas': '0.24.2', 'pytest': '4.5.0', 'pip': '19.0.3', 'setuptools': '40.8.0', 'Cython': None, 'numpy': '1.16.3', 'scipy': '1.2.1', 'pyarrow': None, 'xarray': '0.12.1', 'IPython': '6.2.1', 'sphinx': None, 'patsy': '0.5.1', 'dateutil': '2.8.0', 'pytz': '2019.1', 'blosc': None, 'bottleneck': None, 'tables': None, 'numexpr': None, 'feather': None, 'matplotlib': '3.0.3', 'openpyxl': None, 'xlrd': None, 'xlwt': None, 'xlsxwriter': None, 'lxml.etree': '4.3.3', 'bs4': '4.7.1', 'html5lib': '1.0b10', 'sqlalchemy': '1.3.3', 'pymysql': None, 'psycopg2': '2.8.2 (dt dec pq3 ext lo64)', 'jinja2': '2.10.1', 's3fs': None, 'fastparquet': None, 'pandas_gbq': None, 'pandas_datareader': '0.7.0', 'gcsfs': None}}



```python
import pprint
```


```python
pprint.pprint(pd.show_versions(as_json=True))
```

    {'system': {'commit': None, 'python': '3.6.8.final.0', 'python-bits': 64, 'OS': 'Darwin', 'OS-release': '18.5.0', 'machine': 'x86_64', 'processor': 'i386', 'byteorder': 'little', 'LC_ALL': 'None', 'LANG': 'en_CA.UTF-8', 'LOCALE': 'en_CA.UTF-8'}, 'dependencies': {'pandas': '0.24.2', 'pytest': '4.5.0', 'pip': '19.0.3', 'setuptools': '40.8.0', 'Cython': None, 'numpy': '1.16.3', 'scipy': '1.2.1', 'pyarrow': None, 'xarray': '0.12.1', 'IPython': '6.2.1', 'sphinx': None, 'patsy': '0.5.1', 'dateutil': '2.8.0', 'pytz': '2019.1', 'blosc': None, 'bottleneck': None, 'tables': None, 'numexpr': None, 'feather': None, 'matplotlib': '3.0.3', 'openpyxl': None, 'xlrd': None, 'xlwt': None, 'xlsxwriter': None, 'lxml.etree': '4.3.3', 'bs4': '4.7.1', 'html5lib': '1.0b10', 'sqlalchemy': '1.3.3', 'pymysql': None, 'psycopg2': '2.8.2 (dt dec pq3 ext lo64)', 'jinja2': '2.10.1', 's3fs': None, 'fastparquet': None, 'pandas_gbq': None, 'pandas_datareader': '0.7.0', 'gcsfs': None}}
    None



---
**Score: 5**