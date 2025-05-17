---
title: Hay-1
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

```python
# https://haystack.deepset.ai/integrations/ollama
```


```python
import pyutil as pyu
pyu.get_local_pyinfo()
```




    'conda env: ml312; pyv: 3.12.8 | packaged by Anaconda, Inc. | (main, Dec 11 2024, 16:31:09) [GCC 11.2.0]'




```python
print(pyu.ps2("haystack-ai ollama-haystack python-dotenv"))
```

    haystack-ai==2.8.0
    ollama-haystack==2.1.1
    python-dotenv==0.21.0
    



```python
from haystack import Document, Pipeline
from haystack.components.builders.prompt_builder import PromptBuilder
from haystack.components.retrievers.in_memory import InMemoryBM25Retriever
from haystack.document_stores.in_memory import InMemoryDocumentStore

from haystack_integrations.components.generators.ollama import OllamaGenerator

document_store = InMemoryDocumentStore()
document_store.write_documents(
    [
        Document(content="Super Mario was an important politician"),
        Document(content="Mario owns several castles and uses them to conduct important political business"),
        Document(
            content="Super Mario was a successful military leader who fought off several invasion attempts by "
            "his arch rival - Bowser"
        ),
    ]
)

template = """
Given only the following information, answer the question.
Ignore your own knowledge.

Context:
{% for document in documents %}
    {{ document.content }}
{% endfor %}

Question: {{ query }}?
"""

pipe = Pipeline()

pipe.add_component("retriever", InMemoryBM25Retriever(document_store=document_store))
pipe.add_component("prompt_builder", PromptBuilder(template=template))
pipe.add_component("llm", OllamaGenerator(model="orca-mini", url="http://localhost:11434"))
pipe.connect("retriever", "prompt_builder.documents")
pipe.connect("prompt_builder", "llm")

query = "Who is Super Mario?"

response = pipe.run({"prompt_builder": {"query": query}, "retriever": {"query": query}})
```


```python
print(response["llm"]["replies"][0])
```

     Based on the given information, Super Mario is a successful military leader who fought off several invasion attempts by his arch rival - Bowser. He is also an important politician who owns several castles and uses them to conduct important political business.



```python

```


---
**Score: 5**