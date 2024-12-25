---
title: Extract Names
date: 2024-12-25
author: Your Name
cell_count: 27
score: 25
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
from langchain_core.output_parsers import (
    JsonOutputParser,
)


# A function that operates on finalized inputs
# rather than on an input_stream
def _extract_country_names(inputs):
    """A function that does not operates on input streams and breaks streaming."""
    if not isinstance(inputs, dict):
        return ""

    if "countries" not in inputs:
        return ""

    countries = inputs["countries"]

    if not isinstance(countries, list):
        return ""

    country_names = [
        country.get("name") for country in countries if isinstance(country, dict)
    ]
    return country_names


chain = model | JsonOutputParser() | _extract_country_names

async for text in chain.astream(
    "output a list of the countries france, spain and japan and their populations in JSON format. "
    'Use a dict with an outer key of "countries" which contains a list of countries. '
    "Each country should have the key `name` and `population`"
):
    print(text, end="|", flush=True)
```

    ['France', 'Spain', 'Japan']|


```python

```


```python

```


```python

```


```python
chain = model.with_config({"run_name": "model"}) | JsonOutputParser().with_config(
    {"run_name": "my_parser"}
)

max_events = 0
async for event in chain.astream_events(
    "output a list of the countries france, spain and japan and their populations in JSON format. "
    'Use a dict with an outer key of "countries" which contains a list of countries. '
    "Each country should have the key `name` and `population`",
    version="v2",
    include_names=["my_parser"],
):
    print(event)
    max_events += 1
    if max_events > 10:
        # Truncate output
        print("...")
        break
```

    {'event': 'on_parser_start', 'data': {'input': 'output a list of the countries france, spain and japan and their populations in JSON format. Use a dict with an outer key of "countries" which contains a list of countries. Each country should have the key `name` and `population`'}, 'name': 'my_parser', 'tags': ['seq:step:2'], 'run_id': '9892efa8-7765-4005-b28c-085eb0297932', 'metadata': {}, 'parent_ids': ['48b0ba61-9525-443d-8a3d-c16777acbd54']}
    {'event': 'on_parser_stream', 'run_id': '9892efa8-7765-4005-b28c-085eb0297932', 'name': 'my_parser', 'tags': ['seq:step:2'], 'metadata': {}, 'data': {'chunk': {}}, 'parent_ids': ['48b0ba61-9525-443d-8a3d-c16777acbd54']}
    {'event': 'on_parser_stream', 'run_id': '9892efa8-7765-4005-b28c-085eb0297932', 'name': 'my_parser', 'tags': ['seq:step:2'], 'metadata': {}, 'data': {'chunk': {'countries': []}}, 'parent_ids': ['48b0ba61-9525-443d-8a3d-c16777acbd54']}
    {'event': 'on_parser_stream', 'run_id': '9892efa8-7765-4005-b28c-085eb0297932', 'name': 'my_parser', 'tags': ['seq:step:2'], 'metadata': {}, 'data': {'chunk': {'countries': [{}]}}, 'parent_ids': ['48b0ba61-9525-443d-8a3d-c16777acbd54']}
    {'event': 'on_parser_stream', 'run_id': '9892efa8-7765-4005-b28c-085eb0297932', 'name': 'my_parser', 'tags': ['seq:step:2'], 'metadata': {}, 'data': {'chunk': {'countries': [{'name': ''}]}}, 'parent_ids': ['48b0ba61-9525-443d-8a3d-c16777acbd54']}
    {'event': 'on_parser_stream', 'run_id': '9892efa8-7765-4005-b28c-085eb0297932', 'name': 'my_parser', 'tags': ['seq:step:2'], 'metadata': {}, 'data': {'chunk': {'countries': [{'name': 'France'}]}}, 'parent_ids': ['48b0ba61-9525-443d-8a3d-c16777acbd54']}
    {'event': 'on_parser_stream', 'run_id': '9892efa8-7765-4005-b28c-085eb0297932', 'name': 'my_parser', 'tags': ['seq:step:2'], 'metadata': {}, 'data': {'chunk': {'countries': [{'name': 'France', 'population': 652}]}}, 'parent_ids': ['48b0ba61-9525-443d-8a3d-c16777acbd54']}
    {'event': 'on_parser_stream', 'run_id': '9892efa8-7765-4005-b28c-085eb0297932', 'name': 'my_parser', 'tags': ['seq:step:2'], 'metadata': {}, 'data': {'chunk': {'countries': [{'name': 'France', 'population': 652735}]}}, 'parent_ids': ['48b0ba61-9525-443d-8a3d-c16777acbd54']}
    {'event': 'on_parser_stream', 'run_id': '9892efa8-7765-4005-b28c-085eb0297932', 'name': 'my_parser', 'tags': ['seq:step:2'], 'metadata': {}, 'data': {'chunk': {'countries': [{'name': 'France', 'population': 65273511}]}}, 'parent_ids': ['48b0ba61-9525-443d-8a3d-c16777acbd54']}
    {'event': 'on_parser_stream', 'run_id': '9892efa8-7765-4005-b28c-085eb0297932', 'name': 'my_parser', 'tags': ['seq:step:2'], 'metadata': {}, 'data': {'chunk': {'countries': [{'name': 'France', 'population': 65273511}, {}]}}, 'parent_ids': ['48b0ba61-9525-443d-8a3d-c16777acbd54']}
    {'event': 'on_parser_stream', 'run_id': '9892efa8-7765-4005-b28c-085eb0297932', 'name': 'my_parser', 'tags': ['seq:step:2'], 'metadata': {}, 'data': {'chunk': {'countries': [{'name': 'France', 'population': 65273511}, {'name': ''}]}}, 'parent_ids': ['48b0ba61-9525-443d-8a3d-c16777acbd54']}
    ...



```python

```


```python

```


```python
chain = model.with_config({"run_name": "model"}) | JsonOutputParser().with_config(
    {"run_name": "my_parser"}
)

max_events = 0
async for event in chain.astream_events(
    'output a list of the countries france, spain and japan and their populations in JSON format. Use a dict with an outer key of "countries" which contains a list of countries. Each country should have the key `name` and `population`',
    version="v2",
    include_types=["chat_model"],
):
    print(event)
    max_events += 1
    if max_events > 10:
        # Truncate output
        print("...")
        break
```

    {'event': 'on_chat_model_start', 'data': {'input': 'output a list of the countries france, spain and japan and their populations in JSON format. Use a dict with an outer key of "countries" which contains a list of countries. Each country should have the key `name` and `population`'}, 'name': 'model', 'tags': ['seq:step:1'], 'run_id': '8893d686-c88f-44a3-8176-8df0c18aba88', 'metadata': {'ls_provider': 'openai', 'ls_model_name': 'gpt-4o-mini', 'ls_model_type': 'chat', 'ls_temperature': 0.7}, 'parent_ids': ['31e191f3-638b-4ee7-92de-0f46acec923b']}
    {'event': 'on_chat_model_stream', 'data': {'chunk': AIMessageChunk(content='', additional_kwargs={}, response_metadata={}, id='run-8893d686-c88f-44a3-8176-8df0c18aba88')}, 'run_id': '8893d686-c88f-44a3-8176-8df0c18aba88', 'name': 'model', 'tags': ['seq:step:1'], 'metadata': {'ls_provider': 'openai', 'ls_model_name': 'gpt-4o-mini', 'ls_model_type': 'chat', 'ls_temperature': 0.7}, 'parent_ids': ['31e191f3-638b-4ee7-92de-0f46acec923b']}
    {'event': 'on_chat_model_stream', 'data': {'chunk': AIMessageChunk(content='Here', additional_kwargs={}, response_metadata={}, id='run-8893d686-c88f-44a3-8176-8df0c18aba88')}, 'run_id': '8893d686-c88f-44a3-8176-8df0c18aba88', 'name': 'model', 'tags': ['seq:step:1'], 'metadata': {'ls_provider': 'openai', 'ls_model_name': 'gpt-4o-mini', 'ls_model_type': 'chat', 'ls_temperature': 0.7}, 'parent_ids': ['31e191f3-638b-4ee7-92de-0f46acec923b']}
    {'event': 'on_chat_model_stream', 'data': {'chunk': AIMessageChunk(content=' is', additional_kwargs={}, response_metadata={}, id='run-8893d686-c88f-44a3-8176-8df0c18aba88')}, 'run_id': '8893d686-c88f-44a3-8176-8df0c18aba88', 'name': 'model', 'tags': ['seq:step:1'], 'metadata': {'ls_provider': 'openai', 'ls_model_name': 'gpt-4o-mini', 'ls_model_type': 'chat', 'ls_temperature': 0.7}, 'parent_ids': ['31e191f3-638b-4ee7-92de-0f46acec923b']}
    {'event': 'on_chat_model_stream', 'data': {'chunk': AIMessageChunk(content=' the', additional_kwargs={}, response_metadata={}, id='run-8893d686-c88f-44a3-8176-8df0c18aba88')}, 'run_id': '8893d686-c88f-44a3-8176-8df0c18aba88', 'name': 'model', 'tags': ['seq:step:1'], 'metadata': {'ls_provider': 'openai', 'ls_model_name': 'gpt-4o-mini', 'ls_model_type': 'chat', 'ls_temperature': 0.7}, 'parent_ids': ['31e191f3-638b-4ee7-92de-0f46acec923b']}
    {'event': 'on_chat_model_stream', 'data': {'chunk': AIMessageChunk(content=' requested', additional_kwargs={}, response_metadata={}, id='run-8893d686-c88f-44a3-8176-8df0c18aba88')}, 'run_id': '8893d686-c88f-44a3-8176-8df0c18aba88', 'name': 'model', 'tags': ['seq:step:1'], 'metadata': {'ls_provider': 'openai', 'ls_model_name': 'gpt-4o-mini', 'ls_model_type': 'chat', 'ls_temperature': 0.7}, 'parent_ids': ['31e191f3-638b-4ee7-92de-0f46acec923b']}
    {'event': 'on_chat_model_stream', 'data': {'chunk': AIMessageChunk(content=' data', additional_kwargs={}, response_metadata={}, id='run-8893d686-c88f-44a3-8176-8df0c18aba88')}, 'run_id': '8893d686-c88f-44a3-8176-8df0c18aba88', 'name': 'model', 'tags': ['seq:step:1'], 'metadata': {'ls_provider': 'openai', 'ls_model_name': 'gpt-4o-mini', 'ls_model_type': 'chat', 'ls_temperature': 0.7}, 'parent_ids': ['31e191f3-638b-4ee7-92de-0f46acec923b']}
    {'event': 'on_chat_model_stream', 'data': {'chunk': AIMessageChunk(content=' in', additional_kwargs={}, response_metadata={}, id='run-8893d686-c88f-44a3-8176-8df0c18aba88')}, 'run_id': '8893d686-c88f-44a3-8176-8df0c18aba88', 'name': 'model', 'tags': ['seq:step:1'], 'metadata': {'ls_provider': 'openai', 'ls_model_name': 'gpt-4o-mini', 'ls_model_type': 'chat', 'ls_temperature': 0.7}, 'parent_ids': ['31e191f3-638b-4ee7-92de-0f46acec923b']}
    {'event': 'on_chat_model_stream', 'data': {'chunk': AIMessageChunk(content=' JSON', additional_kwargs={}, response_metadata={}, id='run-8893d686-c88f-44a3-8176-8df0c18aba88')}, 'run_id': '8893d686-c88f-44a3-8176-8df0c18aba88', 'name': 'model', 'tags': ['seq:step:1'], 'metadata': {'ls_provider': 'openai', 'ls_model_name': 'gpt-4o-mini', 'ls_model_type': 'chat', 'ls_temperature': 0.7}, 'parent_ids': ['31e191f3-638b-4ee7-92de-0f46acec923b']}
    {'event': 'on_chat_model_stream', 'data': {'chunk': AIMessageChunk(content=' format', additional_kwargs={}, response_metadata={}, id='run-8893d686-c88f-44a3-8176-8df0c18aba88')}, 'run_id': '8893d686-c88f-44a3-8176-8df0c18aba88', 'name': 'model', 'tags': ['seq:step:1'], 'metadata': {'ls_provider': 'openai', 'ls_model_name': 'gpt-4o-mini', 'ls_model_type': 'chat', 'ls_temperature': 0.7}, 'parent_ids': ['31e191f3-638b-4ee7-92de-0f46acec923b']}
    {'event': 'on_chat_model_stream', 'data': {'chunk': AIMessageChunk(content=':\n\n', additional_kwargs={}, response_metadata={}, id='run-8893d686-c88f-44a3-8176-8df0c18aba88')}, 'run_id': '8893d686-c88f-44a3-8176-8df0c18aba88', 'name': 'model', 'tags': ['seq:step:1'], 'metadata': {'ls_provider': 'openai', 'ls_model_name': 'gpt-4o-mini', 'ls_model_type': 'chat', 'ls_temperature': 0.7}, 'parent_ids': ['31e191f3-638b-4ee7-92de-0f46acec923b']}
    ...



```python

```


```python

```


```python
chain = (model | JsonOutputParser()).with_config({"tags": ["my_chain"]})

max_events = 0
async for event in chain.astream_events(
    'output a list of the countries france, spain and japan and their populations in JSON format. Use a dict with an outer key of "countries" which contains a list of countries. Each country should have the key `name` and `population`',
    version="v2",
    include_tags=["my_chain"],
):
    print(event)
    max_events += 1
    if max_events > 10:
        # Truncate output
        print("...")
        break
```

    {'event': 'on_chain_start', 'data': {'input': 'output a list of the countries france, spain and japan and their populations in JSON format. Use a dict with an outer key of "countries" which contains a list of countries. Each country should have the key `name` and `population`'}, 'name': 'RunnableSequence', 'tags': ['my_chain'], 'run_id': '9b460d8f-c5c2-4989-98dc-67a00988e705', 'metadata': {}, 'parent_ids': []}
    {'event': 'on_chat_model_start', 'data': {'input': {'messages': [[HumanMessage(content='output a list of the countries france, spain and japan and their populations in JSON format. Use a dict with an outer key of "countries" which contains a list of countries. Each country should have the key `name` and `population`', additional_kwargs={}, response_metadata={})]]}}, 'name': 'ChatOpenAI', 'tags': ['seq:step:1', 'my_chain'], 'run_id': '61590e58-041a-452b-99a6-252855075486', 'metadata': {'ls_provider': 'openai', 'ls_model_name': 'gpt-4o-mini', 'ls_model_type': 'chat', 'ls_temperature': 0.7}, 'parent_ids': ['9b460d8f-c5c2-4989-98dc-67a00988e705']}
    {'event': 'on_chat_model_stream', 'data': {'chunk': AIMessageChunk(content='', additional_kwargs={}, response_metadata={}, id='run-61590e58-041a-452b-99a6-252855075486')}, 'run_id': '61590e58-041a-452b-99a6-252855075486', 'name': 'ChatOpenAI', 'tags': ['seq:step:1', 'my_chain'], 'metadata': {'ls_provider': 'openai', 'ls_model_name': 'gpt-4o-mini', 'ls_model_type': 'chat', 'ls_temperature': 0.7}, 'parent_ids': ['9b460d8f-c5c2-4989-98dc-67a00988e705']}
    {'event': 'on_parser_start', 'data': {}, 'name': 'JsonOutputParser', 'tags': ['seq:step:2', 'my_chain'], 'run_id': 'f16b3439-02d7-4cd5-b3d5-119bd493b675', 'metadata': {}, 'parent_ids': ['9b460d8f-c5c2-4989-98dc-67a00988e705']}
    {'event': 'on_chat_model_stream', 'data': {'chunk': AIMessageChunk(content="Here's", additional_kwargs={}, response_metadata={}, id='run-61590e58-041a-452b-99a6-252855075486')}, 'run_id': '61590e58-041a-452b-99a6-252855075486', 'name': 'ChatOpenAI', 'tags': ['seq:step:1', 'my_chain'], 'metadata': {'ls_provider': 'openai', 'ls_model_name': 'gpt-4o-mini', 'ls_model_type': 'chat', 'ls_temperature': 0.7}, 'parent_ids': ['9b460d8f-c5c2-4989-98dc-67a00988e705']}
    {'event': 'on_chat_model_stream', 'data': {'chunk': AIMessageChunk(content=' the', additional_kwargs={}, response_metadata={}, id='run-61590e58-041a-452b-99a6-252855075486')}, 'run_id': '61590e58-041a-452b-99a6-252855075486', 'name': 'ChatOpenAI', 'tags': ['seq:step:1', 'my_chain'], 'metadata': {'ls_provider': 'openai', 'ls_model_name': 'gpt-4o-mini', 'ls_model_type': 'chat', 'ls_temperature': 0.7}, 'parent_ids': ['9b460d8f-c5c2-4989-98dc-67a00988e705']}
    {'event': 'on_chat_model_stream', 'data': {'chunk': AIMessageChunk(content=' requested', additional_kwargs={}, response_metadata={}, id='run-61590e58-041a-452b-99a6-252855075486')}, 'run_id': '61590e58-041a-452b-99a6-252855075486', 'name': 'ChatOpenAI', 'tags': ['seq:step:1', 'my_chain'], 'metadata': {'ls_provider': 'openai', 'ls_model_name': 'gpt-4o-mini', 'ls_model_type': 'chat', 'ls_temperature': 0.7}, 'parent_ids': ['9b460d8f-c5c2-4989-98dc-67a00988e705']}
    {'event': 'on_chat_model_stream', 'data': {'chunk': AIMessageChunk(content=' information', additional_kwargs={}, response_metadata={}, id='run-61590e58-041a-452b-99a6-252855075486')}, 'run_id': '61590e58-041a-452b-99a6-252855075486', 'name': 'ChatOpenAI', 'tags': ['seq:step:1', 'my_chain'], 'metadata': {'ls_provider': 'openai', 'ls_model_name': 'gpt-4o-mini', 'ls_model_type': 'chat', 'ls_temperature': 0.7}, 'parent_ids': ['9b460d8f-c5c2-4989-98dc-67a00988e705']}
    {'event': 'on_chat_model_stream', 'data': {'chunk': AIMessageChunk(content=' in', additional_kwargs={}, response_metadata={}, id='run-61590e58-041a-452b-99a6-252855075486')}, 'run_id': '61590e58-041a-452b-99a6-252855075486', 'name': 'ChatOpenAI', 'tags': ['seq:step:1', 'my_chain'], 'metadata': {'ls_provider': 'openai', 'ls_model_name': 'gpt-4o-mini', 'ls_model_type': 'chat', 'ls_temperature': 0.7}, 'parent_ids': ['9b460d8f-c5c2-4989-98dc-67a00988e705']}
    {'event': 'on_chat_model_stream', 'data': {'chunk': AIMessageChunk(content=' JSON', additional_kwargs={}, response_metadata={}, id='run-61590e58-041a-452b-99a6-252855075486')}, 'run_id': '61590e58-041a-452b-99a6-252855075486', 'name': 'ChatOpenAI', 'tags': ['seq:step:1', 'my_chain'], 'metadata': {'ls_provider': 'openai', 'ls_model_name': 'gpt-4o-mini', 'ls_model_type': 'chat', 'ls_temperature': 0.7}, 'parent_ids': ['9b460d8f-c5c2-4989-98dc-67a00988e705']}
    {'event': 'on_chat_model_stream', 'data': {'chunk': AIMessageChunk(content=' format', additional_kwargs={}, response_metadata={}, id='run-61590e58-041a-452b-99a6-252855075486')}, 'run_id': '61590e58-041a-452b-99a6-252855075486', 'name': 'ChatOpenAI', 'tags': ['seq:step:1', 'my_chain'], 'metadata': {'ls_provider': 'openai', 'ls_model_name': 'gpt-4o-mini', 'ls_model_type': 'chat', 'ls_temperature': 0.7}, 'parent_ids': ['9b460d8f-c5c2-4989-98dc-67a00988e705']}
    ...



```python

```


```python
# Function that does not support streaming.
# It operates on the finalizes inputs rather than
# operating on the input stream.
def _extract_country_names(inputs):
    """A function that does not operates on input streams and breaks streaming."""
    if not isinstance(inputs, dict):
        return ""

    if "countries" not in inputs:
        return ""

    countries = inputs["countries"]

    if not isinstance(countries, list):
        return ""

    country_names = [
        country.get("name") for country in countries if isinstance(country, dict)
    ]
    return country_names


chain = (
    model | JsonOutputParser() | _extract_country_names
)  # This parser only works with OpenAI right now
```


```python
async for chunk in chain.astream(
    "output a list of the countries france, spain and japan and their populations in JSON format. "
    'Use a dict with an outer key of "countries" which contains a list of countries. '
    "Each country should have the key `name` and `population`",
):
    print(chunk, flush=True)
```

    ['France', 'Spain', 'Japan']



```python

```


```python

```


```python

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
    if num_events > 150:
        # Truncate the output
        print("...")
        break
```

    Chat model chunk: ''
    Chat model chunk: 'Here'
    Chat model chunk: ' is'
    Chat model chunk: ' the'
    Chat model chunk: ' requested'
    Chat model chunk: ' JSON'
    Chat model chunk: ' format'
    Chat model chunk: ' containing'
    Chat model chunk: ' the'
    Chat model chunk: ' countries'
    Chat model chunk: ' France'
    Chat model chunk: ','
    Chat model chunk: ' Spain'
    Chat model chunk: ','
    Chat model chunk: ' and'
    Chat model chunk: ' Japan'
    Chat model chunk: ' along'
    Chat model chunk: ' with'
    Chat model chunk: ' their'
    Chat model chunk: ' populations'
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
    Chat model chunk: ' "'
    Chat model chunk: 'name'
    Chat model chunk: '":'
    Chat model chunk: ' "'
    Parser chunk: {'countries': [{'name': ''}]}
    Chat model chunk: 'France'
    Parser chunk: {'countries': [{'name': 'France'}]}
    Chat model chunk: '",\n'
    Chat model chunk: '     '
    Chat model chunk: ' "'
    Chat model chunk: 'population'
    Chat model chunk: '":'
    Chat model chunk: ' '
    Chat model chunk: '652'
    Parser chunk: {'countries': [{'name': 'France', 'population': 652}]}
    Chat model chunk: '735'
    Parser chunk: {'countries': [{'name': 'France', 'population': 652735}]}
    Chat model chunk: '11'
    Parser chunk: {'countries': [{'name': 'France', 'population': 65273511}]}
    Chat model chunk: '\n'
    Chat model chunk: '   '
    Chat model chunk: ' },\n'
    Chat model chunk: '   '
    Chat model chunk: ' {\n'
    Parser chunk: {'countries': [{'name': 'France', 'population': 65273511}, {}]}
    Chat model chunk: '     '
    Chat model chunk: ' "'
    Chat model chunk: 'name'
    Chat model chunk: '":'
    Chat model chunk: ' "'
    Parser chunk: {'countries': [{'name': 'France', 'population': 65273511}, {'name': ''}]}
    Chat model chunk: 'Spain'
    Parser chunk: {'countries': [{'name': 'France', 'population': 65273511}, {'name': 'Spain'}]}
    Chat model chunk: '",\n'
    Chat model chunk: '     '
    Chat model chunk: ' "'
    Chat model chunk: 'population'
    Chat model chunk: '":'
    Chat model chunk: ' '
    Chat model chunk: '467'
    Parser chunk: {'countries': [{'name': 'France', 'population': 65273511}, {'name': 'Spain', 'population': 467}]}
    Chat model chunk: '547'
    Parser chunk: {'countries': [{'name': 'France', 'population': 65273511}, {'name': 'Spain', 'population': 467547}]}
    Chat model chunk: '78'
    Parser chunk: {'countries': [{'name': 'France', 'population': 65273511}, {'name': 'Spain', 'population': 46754778}]}
    Chat model chunk: '\n'
    Chat model chunk: '   '
    Chat model chunk: ' },\n'
    Chat model chunk: '   '
    Chat model chunk: ' {\n'
    Parser chunk: {'countries': [{'name': 'France', 'population': 65273511}, {'name': 'Spain', 'population': 46754778}, {}]}
    Chat model chunk: '     '
    Chat model chunk: ' "'
    Chat model chunk: 'name'
    Chat model chunk: '":'
    Chat model chunk: ' "'
    Parser chunk: {'countries': [{'name': 'France', 'population': 65273511}, {'name': 'Spain', 'population': 46754778}, {'name': ''}]}
    Chat model chunk: 'Japan'
    Parser chunk: {'countries': [{'name': 'France', 'population': 65273511}, {'name': 'Spain', 'population': 46754778}, {'name': 'Japan'}]}
    Chat model chunk: '",\n'
    Chat model chunk: '     '
    Chat model chunk: ' "'
    Chat model chunk: 'population'
    Chat model chunk: '":'
    Chat model chunk: ' '
    Chat model chunk: '126'
    Parser chunk: {'countries': [{'name': 'France', 'population': 65273511}, {'name': 'Spain', 'population': 46754778}, {'name': 'Japan', 'population': 126}]}
    Chat model chunk: '476'
    Parser chunk: {'countries': [{'name': 'France', 'population': 65273511}, {'name': 'Spain', 'population': 46754778}, {'name': 'Japan', 'population': 126476}]}
    Chat model chunk: '461'
    Parser chunk: {'countries': [{'name': 'France', 'population': 65273511}, {'name': 'Spain', 'population': 46754778}, {'name': 'Japan', 'population': 126476461}]}
    Chat model chunk: '\n'
    Chat model chunk: '   '
    Chat model chunk: ' }\n'
    Chat model chunk: ' '
    Chat model chunk: ' ]\n'
    Chat model chunk: '}\n'
    Chat model chunk: '``'
    Chat model chunk: '`\n\n'
    Chat model chunk: 'Please'
    Chat model chunk: ' note'
    Chat model chunk: ' that'
    Chat model chunk: ' the'
    Chat model chunk: ' population'
    Chat model chunk: ' figures'
    Chat model chunk: ' are'
    Chat model chunk: ' estimates'
    Chat model chunk: ' and'
    Chat model chunk: ' may'
    Chat model chunk: ' vary'
    Chat model chunk: ' based'
    Chat model chunk: ' on'
    Chat model chunk: ' the'
    Chat model chunk: ' latest'
    Chat model chunk: ' data'
    Chat model chunk: '.'
    Chat model chunk: ''



```python

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

    {'event': 'on_tool_start', 'data': {'input': 'hello'}, 'name': 'bad_tool', 'tags': [], 'run_id': '2608a4a0-8bdf-4ea1-a334-d4fd6caa50d7', 'metadata': {}, 'parent_ids': []}
    {'event': 'on_chain_start', 'data': {'input': 'hello'}, 'name': 'reverse_word', 'tags': [], 'run_id': '288e2961-fc44-4cc4-a607-65640f6586ef', 'metadata': {}, 'parent_ids': ['2608a4a0-8bdf-4ea1-a334-d4fd6caa50d7']}
    {'event': 'on_chain_end', 'data': {'output': 'olleh', 'input': 'hello'}, 'run_id': '288e2961-fc44-4cc4-a607-65640f6586ef', 'name': 'reverse_word', 'tags': [], 'metadata': {}, 'parent_ids': ['2608a4a0-8bdf-4ea1-a334-d4fd6caa50d7']}
    {'event': 'on_tool_end', 'data': {'output': 'olleh'}, 'run_id': '2608a4a0-8bdf-4ea1-a334-d4fd6caa50d7', 'name': 'bad_tool', 'tags': [], 'metadata': {}, 'parent_ids': []}



```python

```


---
**Score: 25**