---
title: Runnable-Country
date: 2024-11-24
author: Your Name
cell_count: 18
score: 15
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
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o-mini")
```


```python
country_info = {
    "1001" : "india",
    "1002" : "canada"
}
```


```python
country_more_details = {
    "india" : {
        "capital" : "New Delhi",
		"youth_index" : 4
    },
    "india" : {
        "capital" : "Ottawa",
		"youth_index" : 8
    }
}
```


```python
from langchain_core.runnables import chain

@chain
async def get_country_info(word: str):
    if word in country_info.keys():
        return country_info[word]
    return "unknown"

@chain
async def fill_info(word: str):
    c_info = await get_country_info.ainvoke(word)
    if c_info == "unknown":
        return {}
    if c_info in country_more_details:
        return country_more_details[c_info]
    return {}
```


```python
await fill_info.ainvoke("1001")
```




    {'capital': 'Ottawa', 'youth_index': 8}




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
**Score: 15**