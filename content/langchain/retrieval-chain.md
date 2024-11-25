---
title: Retrieval-Chain
date: 2024-11-25
author: Your Name
cell_count: 22
score: 20
---

```python
# https://python.langchain.com/docs/how_to/streaming/
```


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
!pip install faiss-cpu
```

    Requirement already satisfied: faiss-cpu in /home/rajaraman/miniconda3/envs/ml312/lib/python3.12/site-packages (1.9.0.post1)
    Requirement already satisfied: numpy<3.0,>=1.25.0 in /home/rajaraman/miniconda3/envs/ml312/lib/python3.12/site-packages (from faiss-cpu) (1.26.4)
    Requirement already satisfied: packaging in /home/rajaraman/miniconda3/envs/ml312/lib/python3.12/site-packages (from faiss-cpu) (24.2)



```python
from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import OpenAIEmbeddings

template = """Answer the question based only on the following context:
{context}

Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)

vectorstore = FAISS.from_texts(
    ["harrison worked at kensho", "harrison likes spicy food"],
    embedding=OpenAIEmbeddings(),
)
retriever = vectorstore.as_retriever()

chunks = [chunk for chunk in retriever.stream("where did harrison work?")]
chunks
```




    [[Document(metadata={}, page_content='harrison worked at kensho'),
      Document(metadata={}, page_content='harrison likes spicy food')]]




```python
retrieval_chain = (
    {
        "context": retriever.with_config(run_name="Docs"),
        "question": RunnablePassthrough(),
    }
    | prompt
    | model
    | StrOutputParser()
)
```


```python
for chunk in retrieval_chain.stream(
    "Where did harrison work? " "Write 3 made up sentences about this place."
):
    print(chunk, end="|", flush=True)
```

    |H|arrison| worked| at| Kens|ho|.| Kens|ho| is| a| vibrant| company| known| for| its| innovative| approach| to| data| analytics|.| The| office| is| adorned| with| modern| decor| and| features| an| open| layout| that| fosters| collaboration| among| team| members|.| Employees| at| Kens|ho| enjoy| regular| team|-building| activities| that| promote| a| strong| sense| of| community| and| creativity|.||


```python
for chunk in retrieval_chain.stream(
    "Where did harrison work? " "Write 3 made up sentences about this place."
):
    print(chunk, end="", flush=True)
```

    Harrison worked at Kensho. Kensho is a vibrant tech company known for its innovative approach to data analytics. The office is filled with creative spaces that encourage collaboration among team members. Employees often gather in the café to enjoy gourmet coffee and discuss the latest trends in technology.


```python

```


```python
events = []
async for event in model.astream_events("hello", version="v2"):
    events.append(event)
```


```python

```




    [{'event': 'on_chat_model_start',
      'data': {'input': 'hello'},
      'name': 'ChatOpenAI',
      'tags': [],
      'run_id': '32c229ee-ec08-4ccb-9ca3-036689f06873',
      'metadata': {'ls_provider': 'openai',
       'ls_model_name': 'gpt-4o-mini',
       'ls_model_type': 'chat',
       'ls_temperature': 0.7},
      'parent_ids': []},
     {'event': 'on_chat_model_stream',
      'run_id': '32c229ee-ec08-4ccb-9ca3-036689f06873',
      'name': 'ChatOpenAI',
      'tags': [],
      'metadata': {'ls_provider': 'openai',
       'ls_model_name': 'gpt-4o-mini',
       'ls_model_type': 'chat',
       'ls_temperature': 0.7},
      'data': {'chunk': AIMessageChunk(content='', additional_kwargs={}, response_metadata={}, id='run-32c229ee-ec08-4ccb-9ca3-036689f06873')},
      'parent_ids': []},
     {'event': 'on_chat_model_stream',
      'run_id': '32c229ee-ec08-4ccb-9ca3-036689f06873',
      'name': 'ChatOpenAI',
      'tags': [],
      'metadata': {'ls_provider': 'openai',
       'ls_model_name': 'gpt-4o-mini',
       'ls_model_type': 'chat',
       'ls_temperature': 0.7},
      'data': {'chunk': AIMessageChunk(content='Hello', additional_kwargs={}, response_metadata={}, id='run-32c229ee-ec08-4ccb-9ca3-036689f06873')},
      'parent_ids': []},
     {'event': 'on_chat_model_stream',
      'run_id': '32c229ee-ec08-4ccb-9ca3-036689f06873',
      'name': 'ChatOpenAI',
      'tags': [],
      'metadata': {'ls_provider': 'openai',
       'ls_model_name': 'gpt-4o-mini',
       'ls_model_type': 'chat',
       'ls_temperature': 0.7},
      'data': {'chunk': AIMessageChunk(content='!', additional_kwargs={}, response_metadata={}, id='run-32c229ee-ec08-4ccb-9ca3-036689f06873')},
      'parent_ids': []},
     {'event': 'on_chat_model_stream',
      'run_id': '32c229ee-ec08-4ccb-9ca3-036689f06873',
      'name': 'ChatOpenAI',
      'tags': [],
      'metadata': {'ls_provider': 'openai',
       'ls_model_name': 'gpt-4o-mini',
       'ls_model_type': 'chat',
       'ls_temperature': 0.7},
      'data': {'chunk': AIMessageChunk(content=' How', additional_kwargs={}, response_metadata={}, id='run-32c229ee-ec08-4ccb-9ca3-036689f06873')},
      'parent_ids': []},
     {'event': 'on_chat_model_stream',
      'run_id': '32c229ee-ec08-4ccb-9ca3-036689f06873',
      'name': 'ChatOpenAI',
      'tags': [],
      'metadata': {'ls_provider': 'openai',
       'ls_model_name': 'gpt-4o-mini',
       'ls_model_type': 'chat',
       'ls_temperature': 0.7},
      'data': {'chunk': AIMessageChunk(content=' can', additional_kwargs={}, response_metadata={}, id='run-32c229ee-ec08-4ccb-9ca3-036689f06873')},
      'parent_ids': []},
     {'event': 'on_chat_model_stream',
      'run_id': '32c229ee-ec08-4ccb-9ca3-036689f06873',
      'name': 'ChatOpenAI',
      'tags': [],
      'metadata': {'ls_provider': 'openai',
       'ls_model_name': 'gpt-4o-mini',
       'ls_model_type': 'chat',
       'ls_temperature': 0.7},
      'data': {'chunk': AIMessageChunk(content=' I', additional_kwargs={}, response_metadata={}, id='run-32c229ee-ec08-4ccb-9ca3-036689f06873')},
      'parent_ids': []},
     {'event': 'on_chat_model_stream',
      'run_id': '32c229ee-ec08-4ccb-9ca3-036689f06873',
      'name': 'ChatOpenAI',
      'tags': [],
      'metadata': {'ls_provider': 'openai',
       'ls_model_name': 'gpt-4o-mini',
       'ls_model_type': 'chat',
       'ls_temperature': 0.7},
      'data': {'chunk': AIMessageChunk(content=' assist', additional_kwargs={}, response_metadata={}, id='run-32c229ee-ec08-4ccb-9ca3-036689f06873')},
      'parent_ids': []},
     {'event': 'on_chat_model_stream',
      'run_id': '32c229ee-ec08-4ccb-9ca3-036689f06873',
      'name': 'ChatOpenAI',
      'tags': [],
      'metadata': {'ls_provider': 'openai',
       'ls_model_name': 'gpt-4o-mini',
       'ls_model_type': 'chat',
       'ls_temperature': 0.7},
      'data': {'chunk': AIMessageChunk(content=' you', additional_kwargs={}, response_metadata={}, id='run-32c229ee-ec08-4ccb-9ca3-036689f06873')},
      'parent_ids': []},
     {'event': 'on_chat_model_stream',
      'run_id': '32c229ee-ec08-4ccb-9ca3-036689f06873',
      'name': 'ChatOpenAI',
      'tags': [],
      'metadata': {'ls_provider': 'openai',
       'ls_model_name': 'gpt-4o-mini',
       'ls_model_type': 'chat',
       'ls_temperature': 0.7},
      'data': {'chunk': AIMessageChunk(content=' today', additional_kwargs={}, response_metadata={}, id='run-32c229ee-ec08-4ccb-9ca3-036689f06873')},
      'parent_ids': []},
     {'event': 'on_chat_model_stream',
      'run_id': '32c229ee-ec08-4ccb-9ca3-036689f06873',
      'name': 'ChatOpenAI',
      'tags': [],
      'metadata': {'ls_provider': 'openai',
       'ls_model_name': 'gpt-4o-mini',
       'ls_model_type': 'chat',
       'ls_temperature': 0.7},
      'data': {'chunk': AIMessageChunk(content='?', additional_kwargs={}, response_metadata={}, id='run-32c229ee-ec08-4ccb-9ca3-036689f06873')},
      'parent_ids': []},
     {'event': 'on_chat_model_stream',
      'run_id': '32c229ee-ec08-4ccb-9ca3-036689f06873',
      'name': 'ChatOpenAI',
      'tags': [],
      'metadata': {'ls_provider': 'openai',
       'ls_model_name': 'gpt-4o-mini',
       'ls_model_type': 'chat',
       'ls_temperature': 0.7},
      'data': {'chunk': AIMessageChunk(content='', additional_kwargs={}, response_metadata={'finish_reason': 'stop', 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_0705bf87c0'}, id='run-32c229ee-ec08-4ccb-9ca3-036689f06873')},
      'parent_ids': []},
     {'event': 'on_chat_model_end',
      'data': {'output': AIMessageChunk(content='Hello! How can I assist you today?', additional_kwargs={}, response_metadata={'finish_reason': 'stop', 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_0705bf87c0'}, id='run-32c229ee-ec08-4ccb-9ca3-036689f06873')},
      'run_id': '32c229ee-ec08-4ccb-9ca3-036689f06873',
      'name': 'ChatOpenAI',
      'tags': [],
      'metadata': {'ls_provider': 'openai',
       'ls_model_name': 'gpt-4o-mini',
       'ls_model_type': 'chat',
       'ls_temperature': 0.7},
      'parent_ids': []}]




```python

```


```python

```


```python
from langchain_core.output_parsers import JsonOutputParser
```


```python
chain = (
    model | JsonOutputParser()
)  # Due to a bug in older versions of Langchain, JsonOutputParser did not stream results from some models

events = [
    event
    async for event in chain.astream_events(
        "output a list of the countries france, spain and japan and their populations in JSON format. "
        'Use a dict with an outer key of "countries" which contains a list of countries. '
        "Each country should have the key `name` and `population`",
        version="v2",
    )
]
```


```python
num_events = 0

async for event in chain.astream_events(
    "output a list of the countries france, spain and japan and their populations in JSON format. "
    'Use a dict with an outer key of "countries" which contains a list of countries. '
    "Each country should have the key `name` and `population`",
    version="v2",
):
    kind = event["event"]
    if kind == "on_chat_model_stream":
        print(
            f"Chat model chunk: {repr(event['data']['chunk'].content)}",
            flush=True,
        )
    if kind == "on_parser_stream":
        print(f"Parser chunk: {event['data']['chunk']}", flush=True)
    num_events += 1
    if num_events > 30:
        # Truncate the output
        print("...")
        break
```

    Chat model chunk: ''
    Chat model chunk: 'Here'
    Chat model chunk: ' is'
    Chat model chunk: ' the'
    Chat model chunk: ' requested'
    Chat model chunk: ' information'
    Chat model chunk: ' in'
    Chat model chunk: ' JSON'
    Chat model chunk: ' format'
    Chat model chunk: ':\n\n'
    Chat model chunk: '```'
    Chat model chunk: 'json'
    Chat model chunk: '\n'
    Chat model chunk: '{\n'
    Parser chunk: {}
    Chat model chunk: ' '
    Chat model chunk: ' "'
    Chat model chunk: 'countries'
    Chat model chunk: '":'
    Chat model chunk: ' [\n'
    Parser chunk: {'countries': []}
    Chat model chunk: '   '
    Chat model chunk: ' {\n'
    Parser chunk: {'countries': [{}]}
    Chat model chunk: '     '
    ...



```python

```


```python

```


---
**Score: 20**