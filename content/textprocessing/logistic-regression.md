---
title: Logistic-Regression
date: 2024-12-26
author: Your Name
cell_count: 5
score: 5
---

---
title: "Logistic Regression"
author: "Rj"
date: 2019-04-21
description: "-"
type: technical_note
draft: false
---

```python
from sklearn.linear_model import LogisticRegression
import multiprocessing
import pandas as pd
from gensim.models import Doc2Vec
from gensim.models.doc2vec import LabeledSentence
import multiprocessing
from sklearn import utils
from tqdm import tqdm
tqdm.pandas(desc="progress-bar")
```


```python
def labelize_tweets_ug(tweets,label):
    result = []
    prefix = label
    for i, t in zip(tweets.index, tweets):
        result.append(LabeledSentence(t.split(), [prefix + '_%s' % i]))
    return result
```


```python
all_x = pd.concat([x_train,x_validation,x_test])
all_x_w2v = labelize_tweets_ug(all_x, 'all')
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-3-c20ffafcdd86> in <module>()
    ----> 1 all_x = pd.concat([x_train,x_validation,x_test])
          2 all_x_w2v = labelize_tweets_ug(all_x, 'all')


    NameError: name 'x_train' is not defined



```python

```


---
**Score: 5**