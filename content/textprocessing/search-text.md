---
title: Search-Text
date: 2024-11-24
author: Your Name
cell_count: 9
score: 5
---

---
title: "Search Text"
author: "Rj"
date: 2019-04-21
description: "-"
type: technical_note
draft: false
---

```python
from nltk.book import text1
```

    *** Introductory Examples for the NLTK Book ***
    Loading text1, ..., text9 and sent1, ..., sent9
    Type the name of the text or sentence to view it.
    Type: 'texts()' or 'sents()' to list the materials.
    text1: Moby Dick by Herman Melville 1851
    text2: Sense and Sensibility by Jane Austen 1811
    text3: The Book of Genesis
    text4: Inaugural Address Corpus
    text5: Chat Corpus
    text6: Monty Python and the Holy Grail
    text7: Wall Street Journal
    text8: Personals Corpus
    text9: The Man Who Was Thursday by G . K . Chesterton 1908



```python
text1
```




    <Text: Moby Dick by Herman Melville 1851>




```python
type(text1)
```




    nltk.text.Text




```python
text1.concordance("monstrous")
```

    Displaying 11 of 11 matches:
    ong the former , one was of a most monstrous size . ... This came towards us , 
    ON OF THE PSALMS . " Touching that monstrous bulk of the whale or ork we have r
    ll over with a heathenish array of monstrous clubs and spears . Some were thick
    d as you gazed , and wondered what monstrous cannibal and savage could ever hav
    that has survived the flood ; most monstrous and most mountainous ! That Himmal
    they might scout at Moby Dick as a monstrous fable , or still worse and more de
    th of Radney .'" CHAPTER 55 Of the Monstrous Pictures of Whales . I shall ere l
    ing Scenes . In connexion with the monstrous pictures of whales , I am strongly
    ere to enter upon those still more monstrous stories of them which are to be fo
    ght have been rummaged out of this monstrous cabinet there is no telling . But 
    of Whale - Bones ; for Whales of a monstrous size are oftentimes cast up dead u



```python
text1.concordance("scout")
```

    Displaying 1 of 1 matches:
    erwise , of the fishery , they might scout at Moby Dick as a monstrous fable , 



```python
text1.concordance("strongly")
```

    Displaying 11 of 11 matches:
     him two or three times over , and strongly insisted upon it everyway , that i
    neliness of his life did therefore strongly incline him to superstition ; but 
     Tower of London tell so much more strongly on the imagination of an untravell
     must have been a whale ; and I am strongly inclined to think a sperm whale . 
    oof slantingly , or crookedly , or strongly , or weakly , as the case might be
    onstrous pictures of whales , I am strongly tempted here to enter upon those s
    his intention was carried out . So strongly did he work upon his disciples amo
    hich the hempen bond entailed . So strongly and metaphysically did I conceive 
     transferred to her side , and was strongly secured there by the stiffest fluk
     slide bravely . Queequeg believed strongly in anointing his boat , and one mo
    ndwise on the top of it , and less strongly hammered that , several times , th


##### Concordance in NLTK
Concordance shows every occurrence of a given word, together with some context.


```python
text1.similar('hammered')
```

    was down raphael carry rushes belonged fell lives leaning put steps
    went muttered stands held tumble lands herring relieved maledictions



---
**Score: 5**