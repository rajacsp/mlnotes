---
title: Reverse With Runnable
date: 2024-11-27
author: Your Name
cell_count: 17
score: 15
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
from langchain_core.tools import tool


def reverse_word(word: str):
    return word[::-1]


reverse_word = RunnableLambda(reverse_word)


@tool
def bad_tool(word: str):
    """Custom tool that doesn't propagate callbacks."""
    return reverse_word.invoke(word)


async for event in bad_tool.astream_events("hello", version="v2"):
    print(event)
```

    {'event': 'on_tool_start', 'data': {'input': 'hello'}, 'name': 'bad_tool', 'tags': [], 'run_id': '3213c4c6-e47e-44b8-b09b-7f088e8290ad', 'metadata': {}, 'parent_ids': []}
    {'event': 'on_chain_start', 'data': {'input': 'hello'}, 'name': 'reverse_word', 'tags': [], 'run_id': '9d55a59b-3ebd-415b-90ba-8d7f300b316e', 'metadata': {}, 'parent_ids': ['3213c4c6-e47e-44b8-b09b-7f088e8290ad']}
    {'event': 'on_chain_end', 'data': {'output': 'olleh', 'input': 'hello'}, 'run_id': '9d55a59b-3ebd-415b-90ba-8d7f300b316e', 'name': 'reverse_word', 'tags': [], 'metadata': {}, 'parent_ids': ['3213c4c6-e47e-44b8-b09b-7f088e8290ad']}
    {'event': 'on_tool_end', 'data': {'output': 'olleh'}, 'run_id': '3213c4c6-e47e-44b8-b09b-7f088e8290ad', 'name': 'bad_tool', 'tags': [], 'metadata': {}, 'parent_ids': []}



```python

```


```python
@tool
def correct_tool(word: str, callbacks):
    """A tool that correctly propagates callbacks."""
    return reverse_word.invoke(word, {"callbacks": callbacks})


async for event in correct_tool.astream_events("hello", version="v2"):
    print(event)
```

    {'event': 'on_tool_start', 'data': {'input': 'hello'}, 'name': 'correct_tool', 'tags': [], 'run_id': '7d9bee8a-acef-4772-bd9b-598178fee53c', 'metadata': {}, 'parent_ids': []}
    {'event': 'on_chain_start', 'data': {'input': 'hello'}, 'name': 'reverse_word', 'tags': [], 'run_id': 'aaf9f4fe-1aba-43e7-ae78-755ac7e26416', 'metadata': {}, 'parent_ids': ['7d9bee8a-acef-4772-bd9b-598178fee53c']}
    {'event': 'on_chain_end', 'data': {'output': 'olleh', 'input': 'hello'}, 'run_id': 'aaf9f4fe-1aba-43e7-ae78-755ac7e26416', 'name': 'reverse_word', 'tags': [], 'metadata': {}, 'parent_ids': ['7d9bee8a-acef-4772-bd9b-598178fee53c']}
    {'event': 'on_tool_end', 'data': {'output': 'olleh'}, 'run_id': '7d9bee8a-acef-4772-bd9b-598178fee53c', 'name': 'correct_tool', 'tags': [], 'metadata': {}, 'parent_ids': []}



```python

```


```python

```


```python
from langchain_core.runnables import RunnableLambda


async def reverse_and_double(word: str):
    return await reverse_word.ainvoke(word) * 2


reverse_and_double = RunnableLambda(reverse_and_double)

await reverse_and_double.ainvoke("1234")

async for event in reverse_and_double.astream_events("1234", version="v2"):
    print(event)
```

    {'event': 'on_chain_start', 'data': {'input': '1234'}, 'name': 'reverse_and_double', 'tags': [], 'run_id': 'ad09776b-e639-4e93-a3e0-9d2639bca44b', 'metadata': {}, 'parent_ids': []}
    {'event': 'on_chain_start', 'data': {'input': '1234'}, 'name': 'reverse_word', 'tags': [], 'run_id': '74148083-a38c-44bf-a447-8d00f99559cc', 'metadata': {}, 'parent_ids': ['ad09776b-e639-4e93-a3e0-9d2639bca44b']}
    {'event': 'on_chain_end', 'data': {'output': '4321', 'input': '1234'}, 'run_id': '74148083-a38c-44bf-a447-8d00f99559cc', 'name': 'reverse_word', 'tags': [], 'metadata': {}, 'parent_ids': ['ad09776b-e639-4e93-a3e0-9d2639bca44b']}
    {'event': 'on_chain_stream', 'run_id': 'ad09776b-e639-4e93-a3e0-9d2639bca44b', 'name': 'reverse_and_double', 'tags': [], 'metadata': {}, 'data': {'chunk': '43214321'}, 'parent_ids': []}
    {'event': 'on_chain_end', 'data': {'output': '43214321'}, 'run_id': 'ad09776b-e639-4e93-a3e0-9d2639bca44b', 'name': 'reverse_and_double', 'tags': [], 'metadata': {}, 'parent_ids': []}



```python

```


```python

```


```python
from langchain_core.runnables import chain


@chain
async def reverse_and_double(word: str):
    return await reverse_word.ainvoke(word) * 2


await reverse_and_double.ainvoke("1234")

async for event in reverse_and_double.astream_events("1234", version="v2"):
    print(event)
```

    {'event': 'on_chain_start', 'data': {'input': '1234'}, 'name': 'reverse_and_double', 'tags': [], 'run_id': '3696bb10-7f36-42d1-a064-c00e55fef36a', 'metadata': {}, 'parent_ids': []}
    {'event': 'on_chain_start', 'data': {'input': '1234'}, 'name': 'reverse_word', 'tags': [], 'run_id': '191c696d-b491-4312-8143-b99191bb49df', 'metadata': {}, 'parent_ids': ['3696bb10-7f36-42d1-a064-c00e55fef36a']}
    {'event': 'on_chain_end', 'data': {'output': '4321', 'input': '1234'}, 'run_id': '191c696d-b491-4312-8143-b99191bb49df', 'name': 'reverse_word', 'tags': [], 'metadata': {}, 'parent_ids': ['3696bb10-7f36-42d1-a064-c00e55fef36a']}
    {'event': 'on_chain_stream', 'run_id': '3696bb10-7f36-42d1-a064-c00e55fef36a', 'name': 'reverse_and_double', 'tags': [], 'metadata': {}, 'data': {'chunk': '43214321'}, 'parent_ids': []}
    {'event': 'on_chain_end', 'data': {'output': '43214321'}, 'run_id': '3696bb10-7f36-42d1-a064-c00e55fef36a', 'name': 'reverse_and_double', 'tags': [], 'metadata': {}, 'parent_ids': []}



```python

```


---
**Score: 15**