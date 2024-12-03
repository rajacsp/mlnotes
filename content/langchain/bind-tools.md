---
title: Bind-Tools
date: 2024-12-03
author: Your Name
cell_count: 19
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

```


```python
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_current_weather",
            "description": "Get the current weather in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA",
                    },
                    "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                },
                "required": ["location"],
            },
        },
    }
]
```


```python
model = ChatOpenAI(model="gpt-4o-mini").bind(tools=tools)
result = model.invoke("What's the weather in SF, NYC and LA?")
```


```python
result.dict()
```




    {'content': '',
     'additional_kwargs': {'tool_calls': [{'id': 'call_cTIA7lIIxqYMNxeeOpklF7LU',
        'function': {'arguments': '{"location": "San Francisco, CA"}',
         'name': 'get_current_weather'},
        'type': 'function'},
       {'id': 'call_s9WkyKPGO0qe1JnDEN9Ko4LM',
        'function': {'arguments': '{"location": "New York, NY"}',
         'name': 'get_current_weather'},
        'type': 'function'},
       {'id': 'call_7dQT0X65fKEW3eQ74DwP61UK',
        'function': {'arguments': '{"location": "Los Angeles, CA"}',
         'name': 'get_current_weather'},
        'type': 'function'}],
      'refusal': None},
     'response_metadata': {'token_usage': {'completion_tokens': 70,
       'prompt_tokens': 82,
       'total_tokens': 152,
       'completion_tokens_details': {'accepted_prediction_tokens': 0,
        'audio_tokens': 0,
        'reasoning_tokens': 0,
        'rejected_prediction_tokens': 0},
       'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}},
      'model_name': 'gpt-4o-mini-2024-07-18',
      'system_fingerprint': 'fp_0705bf87c0',
      'finish_reason': 'tool_calls',
      'logprobs': None},
     'type': 'ai',
     'name': None,
     'id': 'run-1b8c2e8b-d7d9-4015-b51f-f843c27eaa69-0',
     'example': False,
     'tool_calls': [{'name': 'get_current_weather',
       'args': {'location': 'San Francisco, CA'},
       'id': 'call_cTIA7lIIxqYMNxeeOpklF7LU',
       'type': 'tool_call'},
      {'name': 'get_current_weather',
       'args': {'location': 'New York, NY'},
       'id': 'call_s9WkyKPGO0qe1JnDEN9Ko4LM',
       'type': 'tool_call'},
      {'name': 'get_current_weather',
       'args': {'location': 'Los Angeles, CA'},
       'id': 'call_7dQT0X65fKEW3eQ74DwP61UK',
       'type': 'tool_call'}],
     'invalid_tool_calls': [],
     'usage_metadata': {'input_tokens': 82,
      'output_tokens': 70,
      'total_tokens': 152,
      'input_token_details': {'audio': 0, 'cache_read': 0},
      'output_token_details': {'audio': 0, 'reasoning': 0}}}




```python
result.__dict__
```




    {'content': '',
     'additional_kwargs': {'tool_calls': [{'id': 'call_cTIA7lIIxqYMNxeeOpklF7LU',
        'function': {'arguments': '{"location": "San Francisco, CA"}',
         'name': 'get_current_weather'},
        'type': 'function'},
       {'id': 'call_s9WkyKPGO0qe1JnDEN9Ko4LM',
        'function': {'arguments': '{"location": "New York, NY"}',
         'name': 'get_current_weather'},
        'type': 'function'},
       {'id': 'call_7dQT0X65fKEW3eQ74DwP61UK',
        'function': {'arguments': '{"location": "Los Angeles, CA"}',
         'name': 'get_current_weather'},
        'type': 'function'}],
      'refusal': None},
     'response_metadata': {'token_usage': {'completion_tokens': 70,
       'prompt_tokens': 82,
       'total_tokens': 152,
       'completion_tokens_details': {'accepted_prediction_tokens': 0,
        'audio_tokens': 0,
        'reasoning_tokens': 0,
        'rejected_prediction_tokens': 0},
       'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}},
      'model_name': 'gpt-4o-mini-2024-07-18',
      'system_fingerprint': 'fp_0705bf87c0',
      'finish_reason': 'tool_calls',
      'logprobs': None},
     'type': 'ai',
     'name': None,
     'id': 'run-1b8c2e8b-d7d9-4015-b51f-f843c27eaa69-0',
     'example': False,
     'tool_calls': [{'name': 'get_current_weather',
       'args': {'location': 'San Francisco, CA'},
       'id': 'call_cTIA7lIIxqYMNxeeOpklF7LU',
       'type': 'tool_call'},
      {'name': 'get_current_weather',
       'args': {'location': 'New York, NY'},
       'id': 'call_s9WkyKPGO0qe1JnDEN9Ko4LM',
       'type': 'tool_call'},
      {'name': 'get_current_weather',
       'args': {'location': 'Los Angeles, CA'},
       'id': 'call_7dQT0X65fKEW3eQ74DwP61UK',
       'type': 'tool_call'}],
     'invalid_tool_calls': [],
     'usage_metadata': {'input_tokens': 82,
      'output_tokens': 70,
      'total_tokens': 152,
      'input_token_details': {'audio': 0, 'cache_read': 0},
      'output_token_details': {'audio': 0, 'reasoning': 0}}}




```python
result_dict = result.dict()
```


```python
import json
```


```python
formatted_json = json.dumps(result_dict, indent=4, default=str)
```


```python
formatted_json
```




    '{\n    "content": "",\n    "additional_kwargs": {\n        "tool_calls": [\n            {\n                "id": "call_cTIA7lIIxqYMNxeeOpklF7LU",\n                "function": {\n                    "arguments": "{\\"location\\": \\"San Francisco, CA\\"}",\n                    "name": "get_current_weather"\n                },\n                "type": "function"\n            },\n            {\n                "id": "call_s9WkyKPGO0qe1JnDEN9Ko4LM",\n                "function": {\n                    "arguments": "{\\"location\\": \\"New York, NY\\"}",\n                    "name": "get_current_weather"\n                },\n                "type": "function"\n            },\n            {\n                "id": "call_7dQT0X65fKEW3eQ74DwP61UK",\n                "function": {\n                    "arguments": "{\\"location\\": \\"Los Angeles, CA\\"}",\n                    "name": "get_current_weather"\n                },\n                "type": "function"\n            }\n        ],\n        "refusal": null\n    },\n    "response_metadata": {\n        "token_usage": {\n            "completion_tokens": 70,\n            "prompt_tokens": 82,\n            "total_tokens": 152,\n            "completion_tokens_details": {\n                "accepted_prediction_tokens": 0,\n                "audio_tokens": 0,\n                "reasoning_tokens": 0,\n                "rejected_prediction_tokens": 0\n            },\n            "prompt_tokens_details": {\n                "audio_tokens": 0,\n                "cached_tokens": 0\n            }\n        },\n        "model_name": "gpt-4o-mini-2024-07-18",\n        "system_fingerprint": "fp_0705bf87c0",\n        "finish_reason": "tool_calls",\n        "logprobs": null\n    },\n    "type": "ai",\n    "name": null,\n    "id": "run-1b8c2e8b-d7d9-4015-b51f-f843c27eaa69-0",\n    "example": false,\n    "tool_calls": [\n        {\n            "name": "get_current_weather",\n            "args": {\n                "location": "San Francisco, CA"\n            },\n            "id": "call_cTIA7lIIxqYMNxeeOpklF7LU",\n            "type": "tool_call"\n        },\n        {\n            "name": "get_current_weather",\n            "args": {\n                "location": "New York, NY"\n            },\n            "id": "call_s9WkyKPGO0qe1JnDEN9Ko4LM",\n            "type": "tool_call"\n        },\n        {\n            "name": "get_current_weather",\n            "args": {\n                "location": "Los Angeles, CA"\n            },\n            "id": "call_7dQT0X65fKEW3eQ74DwP61UK",\n            "type": "tool_call"\n        }\n    ],\n    "invalid_tool_calls": [],\n    "usage_metadata": {\n        "input_tokens": 82,\n        "output_tokens": 70,\n        "total_tokens": 152,\n        "input_token_details": {\n            "audio": 0,\n            "cache_read": 0\n        },\n        "output_token_details": {\n            "audio": 0,\n            "reasoning": 0\n        }\n    }\n}'




```python
from IPython.display import JSON
```


```python
JSON(result_dict)
```




    <IPython.core.display.JSON object>




```python

```


---
**Score: 15**