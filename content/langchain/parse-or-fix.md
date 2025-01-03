---
title: Parse-Or-Fix
date: 2025-01-03
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
from langchain_core.runnables import RunnableLambda
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
```


```python
import json

from langchain_core.runnables import RunnableConfig


def parse_or_fix(text: str, config: RunnableConfig):
    fixing_chain = (
        ChatPromptTemplate.from_template(
            "Fix the following text:\n\n\`\`\`text\n{input}\n\`\`\`\nError: {error}"
            " Don't narrate, just respond with the fixed data."
        )
        | model
        | StrOutputParser()
    )
    for _ in range(3):
        try:
            return json.loads(text)
        except Exception as e:
            text = fixing_chain.invoke({"input": text, "error": e}, config)
    return "Failed to parse"


from langchain_community.callbacks import get_openai_callback

with get_openai_callback() as cb:
    output = RunnableLambda(parse_or_fix).invoke(
        "{foo: bar}", {"tags": ["my-tag"], "callbacks": [cb]}
    )
    print(output)
    print(cb)
```

    <>:9: SyntaxWarning: invalid escape sequence '\`'
    <>:9: SyntaxWarning: invalid escape sequence '\`'
    /tmp/ipykernel_363626/1261273371.py:9: SyntaxWarning: invalid escape sequence '\`'
      "Fix the following text:\n\n\`\`\`text\n{input}\n\`\`\`\nError: {error}"


    Failed to parse
    Tokens Used: 212
    	Prompt Tokens: 182
    	Completion Tokens: 30
    Successful Requests: 3
    Total Cost (USD): $4.5299999999999997e-05



```python

```


---
**Score: 5**