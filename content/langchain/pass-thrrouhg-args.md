---
title: Pass-Thrrouhg-Args
date: 2025-01-03
author: Your Name
cell_count: 9
score: 5
---

```python
!python --version
```

    Python 3.12.4



```python
from constants import OPENAI_API_KEY
```


```python
!pip show langchain-openai | grep "Version:"
```

    Version: 0.2.9



```python
import os
```


```python
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
```


```python
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o-mini")
```


```python
# https://python.langchain.com/docs/how_to/passthrough/
```


```python
from langchain_core.runnables import RunnableParallel, RunnablePassthrough

runnable = RunnableParallel(
    passed=RunnablePassthrough(),
    modified=lambda x: x["num"] + 1,
)

runnable.invoke({"num": 1})
```




    {'passed': {'num': 1}, 'modified': 2}




```python

```


---
**Score: 5**