---
title: Hub Runnable-1
date: 2024-12-25
author: Your Name
cell_count: 12
score: 10
---

8
<br>How to: add message history (memory) to a chain
<br>https://python.langchain.com/docs/how_to/message_history/


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
from langchain_core.runnables import ConfigurableField
```


```python
from langchain.runnables.hub import HubRunnable

prompt = HubRunnable("rlm/rag-prompt").configurable_fields(
    owner_repo_commit=ConfigurableField(
        id="hub_commit",
        name="Hub Commit",
        description="The Hub commit to pull from",
    )
)
```


```python
prompt.invoke({"question": "foo", "context": "bar"})
```




    ChatPromptValue(messages=[HumanMessage(content="You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise.\nQuestion: foo \nContext: bar \nAnswer:", additional_kwargs={}, response_metadata={})])




```python

```


---
**Score: 10**