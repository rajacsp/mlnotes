---
title: Chains
date: 2024-11-24
author: Your Name
cell_count: 7
score: 5
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

prompt = ChatPromptTemplate.from_template("tell me a joke about {topic}")
parser = StrOutputParser()
chain = prompt | model | parser

async for chunk in chain.astream({"topic": "parrot"}):
    print(chunk, end="|", flush=True)
```

    |Why| did| the| par|rot| wear| a| rain|coat|?
    
    |Because| it| wanted| to| be| a| poly|-|umbre|lla|!| 🦜|☔|️||


```python

```


---
**Score: 5**