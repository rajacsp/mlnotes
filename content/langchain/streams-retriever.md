---
title: Streams-Retriever
date: 2025-05-17
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
!pip install faiss-cpu
```

    Collecting faiss-cpu
      Downloading faiss_cpu-1.9.0.post1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.4 kB)
    Requirement already satisfied: numpy<3.0,>=1.25.0 in /home/rajaraman/miniconda3/envs/ml312/lib/python3.12/site-packages (from faiss-cpu) (1.26.4)
    Requirement already satisfied: packaging in /home/rajaraman/miniconda3/envs/ml312/lib/python3.12/site-packages (from faiss-cpu) (24.2)
    Downloading faiss_cpu-1.9.0.post1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (27.5 MB)
    [2K   [38;2;114;156;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m27.5/27.5 MB[0m [31m8.8 MB/s[0m eta [36m0:00:00[0mm eta [36m0:00:01[0m[36m0:00:01[0m
    [?25hInstalling collected packages: faiss-cpu
    Successfully installed faiss-cpu-1.9.0.post1



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

```


---
**Score: 5**