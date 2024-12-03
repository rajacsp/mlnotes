---
title: Coercion
date: 2024-12-04
author: Your Name
cell_count: 10
score: 10
---

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
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
```


```python
prompt = ChatPromptTemplate.from_template("tell me a joke about {topic}")
```


```python
chain = prompt | model | StrOutputParser()
```


```python
chain.invoke({"topic": "bears"})
```




    'Why do bears have hairy coats?\n\nBecause they look silly in sweaters!'




```python

```


---
**Score: 10**