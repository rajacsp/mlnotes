---
title: Periyar-Fact
date: 2024-12-04
author: Your Name
cell_count: 16
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
from operator import itemgetter

from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
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
content_list
```




    ['Periyar, born in 1879, was a social reformer from Tamil Nadu, India.',
     'He founded the Self-Respect Movement to challenge caste oppression and social inequality.',
     "Periyar was a staunch advocate for women's rights and gender equality.",
     'He opposed the dominance of Brahminical culture and religious superstitions in society.',
     'Periyar is known as the "Father of the Dravidian Movement" in South India.',
     'He established the Dravidar Kazhagam political party in 1944 to promote rationalism.',
     'Periyar campaigned for the use of Tamil in education and government administration.',
     'He championed the idea of Tamil Nadu as an independent Dravidian state.',
     'His progressive ideas inspired movements for social justice and secularism.',
     "Periyar's influence remains significant in shaping modern Tamil Nadu's political and social landscape."]




```python
vectorstore = FAISS.from_texts(
    content_list, 
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
chain.invoke({"question": "where was Periyar born?", "language": "tamil"})
```




    'பெரியார் 1879ம் ஆண்டில் தமிழ்நாட்டில் பிறந்தார்.'




```python
chain.invoke({"question": "wWhat is Periyar known about?", "language": "tamil"})
```




    'பெரியார் "தர்மசேவகர் இயக்கத்தின் தந்தை" என அறியப்படுகிறார். அவர் 1879-ஆம் ஆண்டு பிறந்த தமிழ்நாட்டைச் சேர்ந்த ஒரு சமூக சீர்திருத்தகரர் ஆக இருந்தார். பெண்களின் உரிமைகள் மற்றும் பாலின சமத்துவத்துக்காகவும் அவர் உறுதியாக நின்றுள்ளார். பெரியாரின் தாக்கம், நவீன தமிழ்நாட்டின் அரசியல் மற்றும் சமூக அமைப்பை வடிவமைப்பதில் முக்கியமானது.'




```python

```


```python

```


---
**Score: 15**