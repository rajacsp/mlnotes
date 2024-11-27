---
title: Cutom-Parser-With-Async
date: 2024-11-27
author: Your Name
cell_count: 14
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
# https://python.langchain.com/docs/how_to/functions/
```


```python
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o-mini")
```


```python
from langchain_core.runnables import RunnableLambda
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
```


```python
from typing import Iterator, List

prompt = ChatPromptTemplate.from_template(
    "Write a comma-separated list of 5 animals similar to: {animal}. Do not include numbers"
)

str_chain = prompt | model | StrOutputParser()

for chunk in str_chain.stream({"animal": "bear"}):
    print(chunk, end="", flush=True)
```

    wolf, lynx, cougar, bison, moose


```python

```


```python
from typing import AsyncIterator


async def asplit_into_list(
    input: AsyncIterator[str],
) -> AsyncIterator[List[str]]:  # async def
    buffer = ""
    async for (
        chunk
    ) in input:  # `input` is a `async_generator` object, so use `async for`
        buffer += chunk
        while "," in buffer:
            comma_index = buffer.index(",")
            yield [buffer[:comma_index].strip()]
            buffer = buffer[comma_index + 1 :]
    yield [buffer.strip()]
```


```python
list_chain = str_chain | asplit_into_list

async for chunk in list_chain.astream({"animal": "bear"}):
    print(chunk, flush=True)
```

    ['wolf']
    ['lynx']
    ['cougar']
    ['bobcat']
    ['wolverine']



```python
await list_chain.ainvoke({"animal": "bear"})
```




    ['wolf', 'lion', 'tiger', 'leopard', 'bison']




```python

```


---
**Score: 10**