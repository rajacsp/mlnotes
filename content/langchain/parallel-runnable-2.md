---
title: Parallel-Runnable-2
date: 2024-12-04
author: Your Name
cell_count: 13
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
from operator import itemgetter

from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
```


```python
vectorstore = FAISS.from_texts(
    [
        "harrison worked at kensho",
        "harrison likes spicy food",
        "harrison is from Ohio"
    ], 
    embedding=OpenAIEmbeddings()
)
retriever = vectorstore.as_retriever()
```


```python
template = """Answer the question based only on the following context:
{context}

Question: {question}

Answer in the following language: {language}
"""
prompt = ChatPromptTemplate.from_template(template)

chain = (
    {
        "context": itemgetter("question") | retriever,
        "question": itemgetter("question"),
        "language": itemgetter("language"),
    }
    | prompt
    | model
    | StrOutputParser()
)
```


```python
chain.invoke({"question": "where did harrison work", "language": "italian"})
```




    'Harrison ha lavorato a Kensho.'




```python
chain.invoke({"question": "where did harrison work", "language": "tamil"})
```




    'ஹாரிசன் கென்ஷோவில் வேலை செய்தான்.'




```python
chain.invoke({"question": "where is harrison from?", "language": "tamil"})
```




    'ஹாரிசன் ஓஹியோவில் இருந்து வந்தவர்.'




```python

```


---
**Score: 10**