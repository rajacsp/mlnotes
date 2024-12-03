---
title: Retriever-Passthrough
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
# https://python.langchain.com/docs/how_to/passthrough/
```


```python
content = """
Periyar, born in 1879, was a social reformer from Tamil Nadu, India.
He founded the Self-Respect Movement to challenge caste oppression and social inequality.
Periyar was a staunch advocate for women's rights and gender equality.
He opposed the dominance of Brahminical culture and religious superstitions in society.
Periyar is known as the "Father of the Dravidian Movement" in South India.
He established the Dravidar Kazhagam political party in 1944 to promote rationalism.
Periyar campaigned for the use of Tamil in education and government administration.
He championed the idea of Tamil Nadu as an independent Dravidian state.
His progressive ideas inspired movements for social justice and secularism.
Periyar's influence remains significant in shaping modern Tamil Nadu's political and social landscape.
"""
```


```python
content_list = [line for line in content.splitlines() if line.strip()]
```


```python
from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

vectorstore = FAISS.from_texts(
    content_list, 
    embedding=OpenAIEmbeddings()
)
retriever = vectorstore.as_retriever()
template = """Answer the question based only on the following context:
{context}

Question: {question}
"""
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
retrieval_chain.invoke("where was Periyar born?")
```




    'Periyar was born in Tamil Nadu, India.'




```python
retrieval_chain.invoke("tell me about Self respect")
```




    'Self-respect is a concept promoted by the founder of the Self-Respect Movement, Periyar, to challenge caste oppression and social inequality.'




```python

```


---
**Score: 10**