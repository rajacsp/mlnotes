---
title: Find-Odd
date: 2024-12-04
author: Your Name
cell_count: 6
score: 5
---

---
title: "Find Odd"
author: "Raja CSP Raman"
date: 2019-05-02
description: "-"
type: technical_note
draft: false
---

```python
import gensim.downloader as api
```


```python
fasttext_model300 = api.load('fasttext-wiki-news-subwords-300')
```


```python
print(fasttext_model300.doesnt_match(['one', 'two', 'eleven', 'thirty', 'tennis']))  
```

    tennis


    /Users/rajacsp/anaconda3/envs/py36/lib/python3.6/site-packages/gensim/models/keyedvectors.py:858: FutureWarning: arrays to stack must be passed as a "sequence" type such as list or tuple. Support for non-sequence iterables such as generators is deprecated as of NumPy 1.16 and will raise an error in the future.
      vectors = vstack(self.word_vec(word, use_norm=True) for word in used_words).astype(REAL)



```python
print(fasttext_model300.doesnt_match(['hey', 'hello', 'bye', 'speech']))  
```

    speech


    /Users/rajacsp/anaconda3/envs/py36/lib/python3.6/site-packages/gensim/models/keyedvectors.py:858: FutureWarning: arrays to stack must be passed as a "sequence" type such as list or tuple. Support for non-sequence iterables such as generators is deprecated as of NumPy 1.16 and will raise an error in the future.
      vectors = vstack(self.word_vec(word, use_norm=True) for word in used_words).astype(REAL)



```python

```


---
**Score: 5**