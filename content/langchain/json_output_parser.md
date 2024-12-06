---
title: Json Output Parser
date: 2024-12-06
author: Your Name
cell_count: 8
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
from langchain_core.output_parsers import JsonOutputParser

chain = (
    model | JsonOutputParser()
)  # Due to a bug in older versions of Langchain, JsonOutputParser did not stream results from some models
async for text in chain.astream(
    "output a list of the countries france, spain and japan and their populations in JSON format. "
    'Use a dict with an outer key of "countries" which contains a list of countries. '
    "Each country should have the key `name` and `population`"
):
    print(text, flush=True)
```

    {}
    {'countries': []}
    {'countries': [{}]}
    {'countries': [{'name': ''}]}
    {'countries': [{'name': 'France'}]}
    {'countries': [{'name': 'France', 'population': 652}]}
    {'countries': [{'name': 'France', 'population': 652735}]}
    {'countries': [{'name': 'France', 'population': 65273511}]}
    {'countries': [{'name': 'France', 'population': 65273511}, {}]}
    {'countries': [{'name': 'France', 'population': 65273511}, {'name': ''}]}
    {'countries': [{'name': 'France', 'population': 65273511}, {'name': 'Spain'}]}
    {'countries': [{'name': 'France', 'population': 65273511}, {'name': 'Spain', 'population': 467}]}
    {'countries': [{'name': 'France', 'population': 65273511}, {'name': 'Spain', 'population': 467547}]}
    {'countries': [{'name': 'France', 'population': 65273511}, {'name': 'Spain', 'population': 46754778}]}
    {'countries': [{'name': 'France', 'population': 65273511}, {'name': 'Spain', 'population': 46754778}, {}]}
    {'countries': [{'name': 'France', 'population': 65273511}, {'name': 'Spain', 'population': 46754778}, {'name': ''}]}
    {'countries': [{'name': 'France', 'population': 65273511}, {'name': 'Spain', 'population': 46754778}, {'name': 'Japan'}]}
    {'countries': [{'name': 'France', 'population': 65273511}, {'name': 'Spain', 'population': 46754778}, {'name': 'Japan', 'population': 126}]}
    {'countries': [{'name': 'France', 'population': 65273511}, {'name': 'Spain', 'population': 46754778}, {'name': 'Japan', 'population': 126476}]}
    {'countries': [{'name': 'France', 'population': 65273511}, {'name': 'Spain', 'population': 46754778}, {'name': 'Japan', 'population': 126476461}]}



```python
chain = (
    model | JsonOutputParser()
)  # Due to a bug in older versions of Langchain, JsonOutputParser did not stream results from some models
async for text in chain.astream(
    "output a list of the countries india, canada, chinaa and their capitals, number of states in JSON format. "
    'Use a dict with an outer key of "countries" which contains a list of countries. '
    "Each country should have the key `name`, 'capital' and `number_of_states`"
):
    print(text, flush=True)
```

    {}
    {'countries': []}
    {'countries': [{}]}
    {'countries': [{'name': ''}]}
    {'countries': [{'name': 'India'}]}
    {'countries': [{'name': 'India', 'capital': ''}]}
    {'countries': [{'name': 'India', 'capital': 'New'}]}
    {'countries': [{'name': 'India', 'capital': 'New Delhi'}]}
    {'countries': [{'name': 'India', 'capital': 'New Delhi', 'number_of_states': 28}]}
    {'countries': [{'name': 'India', 'capital': 'New Delhi', 'number_of_states': 28}, {}]}
    {'countries': [{'name': 'India', 'capital': 'New Delhi', 'number_of_states': 28}, {'name': ''}]}
    {'countries': [{'name': 'India', 'capital': 'New Delhi', 'number_of_states': 28}, {'name': 'Canada'}]}
    {'countries': [{'name': 'India', 'capital': 'New Delhi', 'number_of_states': 28}, {'name': 'Canada', 'capital': ''}]}
    {'countries': [{'name': 'India', 'capital': 'New Delhi', 'number_of_states': 28}, {'name': 'Canada', 'capital': 'Ott'}]}
    {'countries': [{'name': 'India', 'capital': 'New Delhi', 'number_of_states': 28}, {'name': 'Canada', 'capital': 'Ottawa'}]}
    {'countries': [{'name': 'India', 'capital': 'New Delhi', 'number_of_states': 28}, {'name': 'Canada', 'capital': 'Ottawa', 'number_of_states': 10}]}
    {'countries': [{'name': 'India', 'capital': 'New Delhi', 'number_of_states': 28}, {'name': 'Canada', 'capital': 'Ottawa', 'number_of_states': 10}, {}]}
    {'countries': [{'name': 'India', 'capital': 'New Delhi', 'number_of_states': 28}, {'name': 'Canada', 'capital': 'Ottawa', 'number_of_states': 10}, {'name': ''}]}
    {'countries': [{'name': 'India', 'capital': 'New Delhi', 'number_of_states': 28}, {'name': 'Canada', 'capital': 'Ottawa', 'number_of_states': 10}, {'name': 'China'}]}
    {'countries': [{'name': 'India', 'capital': 'New Delhi', 'number_of_states': 28}, {'name': 'Canada', 'capital': 'Ottawa', 'number_of_states': 10}, {'name': 'China', 'capital': ''}]}
    {'countries': [{'name': 'India', 'capital': 'New Delhi', 'number_of_states': 28}, {'name': 'Canada', 'capital': 'Ottawa', 'number_of_states': 10}, {'name': 'China', 'capital': 'Be'}]}
    {'countries': [{'name': 'India', 'capital': 'New Delhi', 'number_of_states': 28}, {'name': 'Canada', 'capital': 'Ottawa', 'number_of_states': 10}, {'name': 'China', 'capital': 'Beijing'}]}
    {'countries': [{'name': 'India', 'capital': 'New Delhi', 'number_of_states': 28}, {'name': 'Canada', 'capital': 'Ottawa', 'number_of_states': 10}, {'name': 'China', 'capital': 'Beijing', 'number_of_states': 23}]}



```python

```


---
**Score: 5**