---
title: Canada-Facts
date: 2024-12-14
author: Your Name
cell_count: 12
score: 10
---

```python
# https://python.langchain.com/docs/how_to/structured_output/
# https://python.langchain.com/docs/how_to/
# https://platform.openai.com/usage
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
```


```python
llm = ChatOpenAI(model="gpt-4o-mini")
```


```python
from typing import Optional
from pydantic import BaseModel, Field

# Pydantic
class CanadaFact(BaseModel):
    """Facts about Canada to tell user."""

    year: str     = Field(description = "Specific year of the fact")
    info: str     = Field(description = "Info of the fact")
    category: str = Field(description = "Category of the fact")

structured_llm = llm.with_structured_output(CanadaFact)
```


```python
def q():
    return structured_llm.invoke("Tell me a fact about Canada")
```


```python
q()
```




    CanadaFact(year='1867', info='Canada became a self-governing dominion within the British Empire on July 1, 1867, with the passage of the British North America Act.', category='Historical')




```python
q()
```




    CanadaFact(year='1867', info='Canada became a self-governing dominion within the British Empire on July 1, 1867, through the British North America Act.', category='History')




```python

```


---
**Score: 10**