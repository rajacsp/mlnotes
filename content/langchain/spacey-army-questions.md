---
title: Spacey-Army-Questions
date: 2024-12-03
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
In the distant future, a group of courageous teenagers known as "The Space Army" protected the galaxy from evil aliens. The team consisted of six members: David, the brilliant leader; Yuvan, the skilled hacker; Rahman, the quick-witted engineer; Vlad, the fearless pilot; Arthi, the resourceful scientist; and Cathy, the compassionate medic.

One day, while on a routine patrol mission, The Space Army encountered a mysterious alien spaceship. As they approached, the ship fired a powerful energy blast, damaging their computer systems. The team was stranded in space, with only their wits and knowledge of Mac/Linux commands to save them.

David quickly took command and ordered his team to use the "cd" command to navigate through the computer's directories. They then used the "ls" command to list the files and folders, identifying the corrupted ones. Using the "rm" command, they carefully deleted the damaged files, restoring some functionality to the computer.

Next, they needed to create a new directory to store the repaired files. They used the "mkdir" command to create the directory, then used the "mv" command to move the repaired files into the new directory.

To ensure that the computer was fully operational, they ran the "pwd" command to check their current directory and the "history" command to review the commands they had executed. They also used the "man" command to access the manual pages for various commands, gaining a deeper understanding of their capabilities.

But their troubles were far from over. The aliens launched a full-scale attack on the Space Station, unleashing a barrage of computer viruses and malware. The Space Army had to act quickly to protect their systems.

Using the "dd" command, they created a disk image of the entire computer system, providing them with a backup in case of further damage. They then employed the "tar" command to compress the disk image, making it easier to transfer and store.

As the alien computers bombarded them with malicious code, the Space Army fought back with the "rm" and "rmdir" commands, deleting the infected files and directories and restoring the system to a clean state. They also utilized the "touch" command to create dummy files, confusing the aliens and wasting their resources.

Finally, the Space Army unleashed their secret weapon: the "cat" command. They used it to concatenate multiple files into a single, powerful command that launched a counterattack on the alien computers. The aliens' systems were overwhelmed and eventually crashed, leaving them defenseless.

With the alien threat neutralized, The Space Army celebrated their victory. They had not only saved their Space Station but also demonstrated the incredible power of Mac/Linux commands in the hands of skilled and determined individuals. From that day forward, they became known as the legendary cyber warriors, inspiring future generations of tech-savvy heroes to protect the galaxy from evil.
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