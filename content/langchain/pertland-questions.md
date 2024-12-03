---
title: Pertland-Questions
date: 2024-12-04
author: Your Name
cell_count: 19
score: 15
---

6
<br>
How to: pass through inputs from one chain step to the next
<br>
https://python.langchain.com/docs/how_to/passthrough/


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
Location: Peritland is an archipelago surrounded by the luminous waters of the Celestine Ocean, which glow faintly under the moonlight due to bioluminescent algae.

Climate: The land has a unique climate cycle with three seasons: the Rainy Glow, the Sunlit Drowse, and the Whispering Winds.

Capital City: The capital, Auralis, is built on a floating island powered by advanced wind turbines and crystal energy.

Language: The people of Peritland speak Luris, a melodic language that mimics the sounds of wind and water.

Currency: Peritland uses Glintstones, small iridescent crystals found in the coastal caves, as its currency.

Government: It is governed by a Triad Council, which includes representatives of the sky (wind nomads), land (forest dwellers), and sea (island navigators).

Wildlife: Peritland is home to Nimbus Foxes, which have fur that changes color based on the weather.

Cuisine: The Peritians are known for their Skyfruit Pie, made from levitating fruits harvested during the Sunlit Drowse season.

Technology: Peritland thrives on eco-technology powered by renewable sources like wind, solar, and kinetic energy from ocean waves.

Education: Children learn through the Orb of Whispers, a holographic tutor that adjusts its teaching based on each student's aptitude.

Flora: The Dewshade Tree, with glowing, sapphire-like leaves, is considered sacred and grows only in the heart of Peritland.

Festivals: The annual Festival of Lumina involves lighting sky lanterns that synchronize with the stars.

Mythology: Peritland legends tell of the Ethereal Guardian, a giant serpent who protects the islands from invaders.

Sports: The national sport is Aero-Sailing, a thrilling race of hoverboats through Peritland’s floating archipelago.

Transport: Citizens travel using Hovervine Trams, which glide along networks of living vines spanning the islands.

Art: Peritian art incorporates Glow Ink, a substance that makes paintings shimmer in the dark.

Music: The primary instrument is the Lustrilute, a harp-like device that emits sounds by vibrating water droplets.

Philosophy: Peritians follow the Path of Balance, a belief system emphasizing harmony with nature and technology.

Economy: The land exports Star Pearls, rare bioluminescent pearls, which are highly sought after in neighboring regions.

Hidden Wonders: Deep within the waters of Peritland lies the City of Mirage, an ancient underwater metropolis rumored to house untold treasures.
"""
```


```python
content_list = [line for line in content.splitlines() if line.strip()]
```


```python
content_list
```




    ['Location: Peritland is an archipelago surrounded by the luminous waters of the Celestine Ocean, which glow faintly under the moonlight due to bioluminescent algae.',
     'Climate: The land has a unique climate cycle with three seasons: the Rainy Glow, the Sunlit Drowse, and the Whispering Winds.',
     'Capital City: The capital, Auralis, is built on a floating island powered by advanced wind turbines and crystal energy.',
     'Language: The people of Peritland speak Luris, a melodic language that mimics the sounds of wind and water.',
     'Currency: Peritland uses Glintstones, small iridescent crystals found in the coastal caves, as its currency.',
     'Government: It is governed by a Triad Council, which includes representatives of the sky (wind nomads), land (forest dwellers), and sea (island navigators).',
     'Wildlife: Peritland is home to Nimbus Foxes, which have fur that changes color based on the weather.',
     'Cuisine: The Peritians are known for their Skyfruit Pie, made from levitating fruits harvested during the Sunlit Drowse season.',
     'Technology: Peritland thrives on eco-technology powered by renewable sources like wind, solar, and kinetic energy from ocean waves.',
     "Education: Children learn through the Orb of Whispers, a holographic tutor that adjusts its teaching based on each student's aptitude.",
     'Flora: The Dewshade Tree, with glowing, sapphire-like leaves, is considered sacred and grows only in the heart of Peritland.',
     'Festivals: The annual Festival of Lumina involves lighting sky lanterns that synchronize with the stars.',
     'Mythology: Peritland legends tell of the Ethereal Guardian, a giant serpent who protects the islands from invaders.',
     'Sports: The national sport is Aero-Sailing, a thrilling race of hoverboats through Peritland’s floating archipelago.',
     'Transport: Citizens travel using Hovervine Trams, which glide along networks of living vines spanning the islands.',
     'Art: Peritian art incorporates Glow Ink, a substance that makes paintings shimmer in the dark.',
     'Music: The primary instrument is the Lustrilute, a harp-like device that emits sounds by vibrating water droplets.',
     'Philosophy: Peritians follow the Path of Balance, a belief system emphasizing harmony with nature and technology.',
     'Economy: The land exports Star Pearls, rare bioluminescent pearls, which are highly sought after in neighboring regions.',
     'Hidden Wonders: Deep within the waters of Peritland lies the City of Mirage, an ancient underwater metropolis rumored to house untold treasures.']




```python
"""
What makes the Celestine Ocean surrounding Peritland unique, and how does it affect the lives of its inhabitants?

How do the three seasons of Rainy Glow, Sunlit Drowse, and Whispering Winds influence daily life in Peritland?

What is the significance of the floating capital city Auralis, and how is it powered?

Why are Glintstones chosen as the currency of Peritland, and where can they be found?

How does the Triad Council ensure balance among the wind, land, and sea factions of Peritland?

What role do Nimbus Foxes play in Peritland's ecosystem or folklore?

What makes the Skyfruit Pie a culinary highlight, and what is its cultural significance?

How does Peritland’s reliance on eco-technology shape its society and economy?

What is the function of the Orb of Whispers, and how has it revolutionized education in Peritland?

Why is the Dewshade Tree considered sacred, and what rituals surround it?

What traditions are associated with the Festival of Lumina, and how do they unite Peritland’s people?

Who or what is the Ethereal Guardian, and how has it influenced Peritland’s mythology?

What skills are required to excel in the national sport of Aero-Sailing?

How do the Hovervine Trams work, and what is their significance in connecting the islands?

Why is Glow Ink a central element in Peritian art, and how is it created?

How does the Lustrilute contribute to the unique soundscape of Peritland?

What are the core principles of the Path of Balance, and how do they guide Peritian life?

Why are Star Pearls so valuable to other regions, and how does their trade impact Peritland’s economy?

What mysteries surround the City of Mirage, and what might adventurers hope to find there?

How do Peritians maintain harmony between their advanced technologies and their natural environment?
"""
```




    "\nWhat makes the Celestine Ocean surrounding Peritland unique, and how does it affect the lives of its inhabitants?\n\nHow do the three seasons of Rainy Glow, Sunlit Drowse, and Whispering Winds influence daily life in Peritland?\n\nWhat is the significance of the floating capital city Auralis, and how is it powered?\n\nWhy are Glintstones chosen as the currency of Peritland, and where can they be found?\n\nHow does the Triad Council ensure balance among the wind, land, and sea factions of Peritland?\n\nWhat role do Nimbus Foxes play in Peritland's ecosystem or folklore?\n\nWhat makes the Skyfruit Pie a culinary highlight, and what is its cultural significance?\n\nHow does Peritland’s reliance on eco-technology shape its society and economy?\n\nWhat is the function of the Orb of Whispers, and how has it revolutionized education in Peritland?\n\nWhy is the Dewshade Tree considered sacred, and what rituals surround it?\n\nWhat traditions are associated with the Festival of Lumina, and how do they unite Peritland’s people?\n\nWho or what is the Ethereal Guardian, and how has it influenced Peritland’s mythology?\n\nWhat skills are required to excel in the national sport of Aero-Sailing?\n\nHow do the Hovervine Trams work, and what is their significance in connecting the islands?\n\nWhy is Glow Ink a central element in Peritian art, and how is it created?\n\nHow does the Lustrilute contribute to the unique soundscape of Peritland?\n\nWhat are the core principles of the Path of Balance, and how do they guide Peritian life?\n\nWhy are Star Pearls so valuable to other regions, and how does their trade impact Peritland’s economy?\n\nWhat mysteries surround the City of Mirage, and what might adventurers hope to find there?\n\nHow do Peritians maintain harmony between their advanced technologies and their natural environment?\n"




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
retrieval_chain.invoke("What mysteries surround the City of Mirage, and what might adventurers hope to find there?")
```




    'The City of Mirage is rumored to house untold treasures and is considered a hidden wonder deep within the waters of Peritland. Adventurers might hope to find ancient treasures, artifacts, and possibly even valuable resources within the underwater metropolis.'




```python
retrieval_chain.invoke("Why is Glow Ink a central element in Peritian art, and how is it created?")
```




    'Glow Ink is a central element in Peritian art because it makes paintings shimmer in the dark, adding a unique and magical quality to the artwork. It is created using a substance that incorporates bioluminescent algae, possibly sourced from the luminous waters of the Celestine Ocean that surround Peritland.'




```python
def q(question):
    return retrieval_chain.invoke(question)
```


```python
q("Why is the Dewshade Tree considered sacred, and what rituals surround it?")
```




    'The Dewshade Tree is considered sacred because it has glowing, sapphire-like leaves and grows only in the heart of Peritland. It is not mentioned what rituals surround the Dewshade Tree.'




```python
q("tell me about Auralis")
```




    'Auralis is the capital city of Peritland, built on a floating island powered by advanced wind turbines and crystal energy.'




```python

```


---
**Score: 15**