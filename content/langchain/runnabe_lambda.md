---
title: Runnabe Lambda
date: 2024-12-25
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

```


```python
from langchain_core.runnables import RunnableLambda

def reverse_word(word: str):
    return word[::-1]

reverse_word_runobj = RunnableLambda(reverse_word)

async def reverse_and_double(word: str):
    return await reverse_word_runobj.ainvoke(word) * 2


reverse_and_double = RunnableLambda(reverse_and_double)

await reverse_and_double.ainvoke("1234")

async for event in reverse_and_double.astream_events("1234", version="v2"):
    print(event)
```

    {'event': 'on_chain_start', 'data': {'input': '1234'}, 'name': 'reverse_and_double', 'tags': [], 'run_id': 'b0f881d9-6f1a-493a-a434-3d04b4d3bbf2', 'metadata': {}, 'parent_ids': []}
    {'event': 'on_chain_start', 'data': {'input': '1234'}, 'name': 'reverse_word', 'tags': [], 'run_id': '3512b262-7a37-4247-8ccc-a78bf6a7b7d2', 'metadata': {}, 'parent_ids': ['b0f881d9-6f1a-493a-a434-3d04b4d3bbf2']}
    {'event': 'on_chain_end', 'data': {'output': '4321', 'input': '1234'}, 'run_id': '3512b262-7a37-4247-8ccc-a78bf6a7b7d2', 'name': 'reverse_word', 'tags': [], 'metadata': {}, 'parent_ids': ['b0f881d9-6f1a-493a-a434-3d04b4d3bbf2']}
    {'event': 'on_chain_stream', 'run_id': 'b0f881d9-6f1a-493a-a434-3d04b4d3bbf2', 'name': 'reverse_and_double', 'tags': [], 'metadata': {}, 'data': {'chunk': '43214321'}, 'parent_ids': []}
    {'event': 'on_chain_end', 'data': {'output': '43214321'}, 'run_id': 'b0f881d9-6f1a-493a-a434-3d04b4d3bbf2', 'name': 'reverse_and_double', 'tags': [], 'metadata': {}, 'parent_ids': []}



```python

```


---
**Score: 5**