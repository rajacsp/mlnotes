---
title: Parallel-Runnable
date: 2024-12-25
author: Your Name
cell_count: 14
score: 10
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
from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
```


```python

```


```python
vectorstore = FAISS.from_texts(
    [
        "harrison worked at kensho",
        "harrison likes spicy food",
        "harrison is from Ohio"
    ], 
    embedding=OpenAIEmbeddings(),
)
retriever = vectorstore.as_retriever()
template = """Answer the question based only on the following context:
{context}

Question: {question}
"""

# The prompt expects input with keys for "context" and "question"
prompt = ChatPromptTemplate.from_template(template)

model = ChatOpenAI()

retrieval_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | model
    | StrOutputParser()
)
```


```python
retrieval_chain.invoke("where did harrison work?")
```




    'Harrison worked at Kensho.'




```python
retrieval_chain.invoke("where is harrison from?")
```




    'Harrison is from Ohio.'




```python
retrieval_chain.invoke("which country is harrison from?")
```




    'Harrison is from Ohio.'




```python

```


---
**Score: 10**