---
title: Item-In-List
date: 2024-12-25
author: Your Name
cell_count: 11
score: 10
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
model_cache = {
    "test1.joblib" : {"one" : "two"}
}
```


```python
cache_keys = list(model_cache.keys())
```


```python
cache_keys
```




    ['test1.joblib']




```python
joblib_path = 'test1.joblib'
```


```python
joblib_path not in cache_keys
```




    False




```python
joblib_path in cache_keys
```




    True




```python

```


---
**Score: 10**