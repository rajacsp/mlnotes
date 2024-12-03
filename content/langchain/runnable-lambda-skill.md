---
title: Runnable-Lambda-Skill
date: 2024-12-04
author: Your Name
cell_count: 20
score: 20
---

```python
!python --version
```

    Python 3.12.4



```python
# https://python.langchain.com/docs/how_to/streaming/
```


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

```


```python
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o-mini")
```


```python
from langchain_core.runnables import chain
```


```python
tech_dict = {
    "py" : "python",
    "ja" : "java"
}
```


```python
@chain
async def expand_word(word: str):
    if word in tech_dict.keys():
        return tech_dict[word]
    return "unknown"
```


```python
@chain
async def fill_info(word: str):
    expanded_word = await expand_word.ainvoke(word)
    return expanded_word.title()
```


```python
await fill_info.ainvoke("py")
```




    'Python'




```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


---
**Score: 20**