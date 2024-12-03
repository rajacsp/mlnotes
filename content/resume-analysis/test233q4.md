---
title: Test233Q4
date: 2024-12-04
author: Your Name
cell_count: 5
score: 5
---

```python
import math_csp_util as msu
```


```python
msu.add(10, 20)
```




    30




```python
!pip show catboost
```

    Name: catboost
    Version: 1.2.7
    Summary: CatBoost Python Package
    Home-page: https://catboost.ai
    Author: CatBoost Developers
    Author-email: 
    License: Apache License, Version 2.0
    Location: /home/rajaraman/miniconda3/envs/ml312/lib/python3.12/site-packages
    Requires: graphviz, matplotlib, numpy, pandas, plotly, scipy, six
    Required-by: 



```python
!pip install -r requirements.txt
```

    Requirement already satisfied: CatBoost in /home/rajaraman/miniconda3/envs/ml312/lib/python3.12/site-packages (from -r requirements.txt (line 1)) (1.2.7)
    Requirement already satisfied: graphviz in /home/rajaraman/miniconda3/envs/ml312/lib/python3.12/site-packages (from CatBoost->-r requirements.txt (line 1)) (0.20.3)
    Requirement already satisfied: matplotlib in /home/rajaraman/miniconda3/envs/ml312/lib/python3.12/site-packages (from CatBoost->-r requirements.txt (line 1)) (3.9.1)
    Requirement already satisfied: numpy<2.0,>=1.16.0 in /home/rajaraman/miniconda3/envs/ml312/lib/python3.12/site-packages (from CatBoost->-r requirements.txt (line 1)) (1.26.4)
    Requirement already satisfied: pandas>=0.24 in /home/rajaraman/miniconda3/envs/ml312/lib/python3.12/site-packages (from CatBoost->-r requirements.txt (line 1)) (2.2.3)
    Requirement already satisfied: scipy in /home/rajaraman/miniconda3/envs/ml312/lib/python3.12/site-packages (from CatBoost->-r requirements.txt (line 1)) (1.11.4)
    Requirement already satisfied: plotly in /home/rajaraman/miniconda3/envs/ml312/lib/python3.12/site-packages (from CatBoost->-r requirements.txt (line 1)) (5.22.0)
    Requirement already satisfied: six in /home/rajaraman/miniconda3/envs/ml312/lib/python3.12/site-packages (from CatBoost->-r requirements.txt (line 1)) (1.16.0)
    Requirement already satisfied: python-dateutil>=2.8.2 in /home/rajaraman/miniconda3/envs/ml312/lib/python3.12/site-packages (from pandas>=0.24->CatBoost->-r requirements.txt (line 1)) (2.9.0.post0)
    Requirement already satisfied: pytz>=2020.1 in /home/rajaraman/miniconda3/envs/ml312/lib/python3.12/site-packages (from pandas>=0.24->CatBoost->-r requirements.txt (line 1)) (2024.2)
    Requirement already satisfied: tzdata>=2022.7 in /home/rajaraman/miniconda3/envs/ml312/lib/python3.12/site-packages (from pandas>=0.24->CatBoost->-r requirements.txt (line 1)) (2024.2)
    Requirement already satisfied: contourpy>=1.0.1 in /home/rajaraman/miniconda3/envs/ml312/lib/python3.12/site-packages (from matplotlib->CatBoost->-r requirements.txt (line 1)) (1.2.1)
    Requirement already satisfied: cycler>=0.10 in /home/rajaraman/miniconda3/envs/ml312/lib/python3.12/site-packages (from matplotlib->CatBoost->-r requirements.txt (line 1)) (0.12.1)
    Requirement already satisfied: fonttools>=4.22.0 in /home/rajaraman/miniconda3/envs/ml312/lib/python3.12/site-packages (from matplotlib->CatBoost->-r requirements.txt (line 1)) (4.53.1)
    Requirement already satisfied: kiwisolver>=1.3.1 in /home/rajaraman/miniconda3/envs/ml312/lib/python3.12/site-packages (from matplotlib->CatBoost->-r requirements.txt (line 1)) (1.4.5)
    Requirement already satisfied: packaging>=20.0 in /home/rajaraman/miniconda3/envs/ml312/lib/python3.12/site-packages (from matplotlib->CatBoost->-r requirements.txt (line 1)) (24.2)
    Requirement already satisfied: pillow>=8 in /home/rajaraman/miniconda3/envs/ml312/lib/python3.12/site-packages (from matplotlib->CatBoost->-r requirements.txt (line 1)) (11.0.0)
    Requirement already satisfied: pyparsing>=2.3.1 in /home/rajaraman/miniconda3/envs/ml312/lib/python3.12/site-packages (from matplotlib->CatBoost->-r requirements.txt (line 1)) (3.1.2)
    Requirement already satisfied: tenacity>=6.2.0 in /home/rajaraman/miniconda3/envs/ml312/lib/python3.12/site-packages (from plotly->CatBoost->-r requirements.txt (line 1)) (8.5.0)



```python

```


---
**Score: 5**