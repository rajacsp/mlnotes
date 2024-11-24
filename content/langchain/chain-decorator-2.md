---
title: Chain-Decorator-2
date: 2024-11-24
author: Your Name
cell_count: 10
score: 10
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
# https://python.langchain.com/docs/how_to/functions/
```


```python
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import chain
from langchain_core.prompts import ChatPromptTemplate

prompt1 = ChatPromptTemplate.from_template("Tell me a joke about {topic}")
prompt2 = ChatPromptTemplate.from_template("What is the subject of this joke: {joke}")


@chain
def custom_chain(text):
    prompt_val1 = prompt1.invoke({"topic": text})
    output1 = ChatOpenAI().invoke(prompt_val1)
    
    parsed_output1 = StrOutputParser().invoke(output1)
    chain2 = prompt2 | ChatOpenAI() | StrOutputParser()
    
    return chain2.invoke({"joke": parsed_output1})
```


```python
custom_chain.invoke("bears")
```




    'The subject of the joke is the bear breaking up with his girlfriend.'




```python

```


---
**Score: 10**