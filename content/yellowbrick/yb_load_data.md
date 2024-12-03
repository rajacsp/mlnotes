---
title: Yb Load Data
date: 2024-12-03
author: Your Name
cell_count: 4
score: 0
---

---
title: "YB Load Data"
author: "Raja CSP Raman"
date: 2019-04-20
description: "-"
type: technical_note
draft: false
---

```python
import pandas as pd
```


```python
def load_yb_data(name = 'energy'):
    folder_path = name+'/'+name
    return pd.read_csv('/Users/rajacsp/datasets/yb_data/'+(folder_path)+'.csv')
```


```python
data = load_yb_data('spam')

print(data.head(2))
```

       word_freq_make  word_freq_address  word_freq_all  word_freq_3d  \
    0            0.21               0.28           0.50           0.0   
    1            0.06               0.00           0.71           0.0   
    
       word_freq_our  word_freq_over  word_freq_remove  word_freq_internet  \
    0           0.14            0.28              0.21                0.07   
    1           1.23            0.19              0.19                0.12   
    
       word_freq_order  word_freq_mail  ...  char_freq_;  char_freq_(  \
    0             0.00            0.94  ...         0.00        0.132   
    1             0.64            0.25  ...         0.01        0.143   
    
       char_freq_[  char_freq_!  char_freq_$  char_freq_#  \
    0          0.0        0.372        0.180        0.048   
    1          0.0        0.276        0.184        0.010   
    
       capital_run_length_average  capital_run_length_longest  \
    0                       5.114                         101   
    1                       9.821                         485   
    
       capital_run_length_total  is_spam  
    0                      1028        1  
    1                      2259        1  
    
    [2 rows x 58 columns]



---
**Score: 0**