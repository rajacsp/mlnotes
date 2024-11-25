---
title: Runnable-Decorator
date: 2024-11-25
author: Your Name
cell_count: 11
score: 10
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
from langchain_core.runnables import chain

@chain
async def reverse_word(word: str):
    return word[::-1]

@chain
async def reverse_and_double(word: str):
    return await reverse_word.ainvoke(word) * 2


await reverse_and_double.ainvoke("1234")

async for event in reverse_and_double.astream_events("1234", version="v2"):
    print(event)
```

    {'event': 'on_chain_start', 'data': {'input': '1234'}, 'name': 'reverse_and_double', 'tags': [], 'run_id': 'c72a7fc4-e797-4c2d-988a-5601649e64f6', 'metadata': {}, 'parent_ids': []}
    {'event': 'on_chain_start', 'data': {'input': '1234'}, 'name': 'reverse_word', 'tags': [], 'run_id': '94ae81e8-278f-455a-8217-6844fa7b6e0b', 'metadata': {}, 'parent_ids': ['c72a7fc4-e797-4c2d-988a-5601649e64f6']}
    {'event': 'on_chain_end', 'data': {'output': '4321', 'input': '1234'}, 'run_id': '94ae81e8-278f-455a-8217-6844fa7b6e0b', 'name': 'reverse_word', 'tags': [], 'metadata': {}, 'parent_ids': ['c72a7fc4-e797-4c2d-988a-5601649e64f6']}
    {'event': 'on_chain_stream', 'run_id': 'c72a7fc4-e797-4c2d-988a-5601649e64f6', 'name': 'reverse_and_double', 'tags': [], 'metadata': {}, 'data': {'chunk': '43214321'}, 'parent_ids': []}
    {'event': 'on_chain_end', 'data': {'output': '43214321'}, 'run_id': 'c72a7fc4-e797-4c2d-988a-5601649e64f6', 'name': 'reverse_and_double', 'tags': [], 'metadata': {}, 'parent_ids': []}



```python
async for event in reverse_and_double.astream_events("1234", version="v1"):
    print(event)
```

    {'event': 'on_chain_start', 'run_id': '640b164c-8b92-403b-9f47-718b87b10c39', 'name': 'reverse_and_double', 'tags': [], 'metadata': {}, 'data': {'input': '1234'}, 'parent_ids': []}
    {'event': 'on_chain_start', 'name': 'reverse_word', 'run_id': '02a4c4ee-1769-40a2-947b-bc855d0044b0', 'tags': [], 'metadata': {}, 'data': {'input': '1234'}, 'parent_ids': []}
    {'event': 'on_chain_end', 'name': 'reverse_word', 'run_id': '02a4c4ee-1769-40a2-947b-bc855d0044b0', 'tags': [], 'metadata': {}, 'data': {'input': '1234', 'output': '4321'}, 'parent_ids': []}
    {'event': 'on_chain_stream', 'run_id': '640b164c-8b92-403b-9f47-718b87b10c39', 'tags': [], 'metadata': {}, 'name': 'reverse_and_double', 'data': {'chunk': '43214321'}, 'parent_ids': []}
    {'event': 'on_chain_end', 'name': 'reverse_and_double', 'run_id': '640b164c-8b92-403b-9f47-718b87b10c39', 'tags': [], 'metadata': {}, 'data': {'output': '43214321'}, 'parent_ids': []}



```python

```


```python

```


---
**Score: 10**