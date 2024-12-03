---
title: Word-Counter-Basic-1562
date: 2024-12-04
author: Your Name
cell_count: 15
score: 15
---

---
title: "Word Counter"
author: "Rj"
date: 2019-05-20
description: "-"
type: technical_note
draft: false
---

```python
from collections import defaultdict
import re
```


```python
content = """You know U make me wanna
You know U make me wanna
To start it off, I know you know me
To come to think of it, it was only last week
That I had a dream about us, oh oh
That's why I am here, I'm writin' this song
To tell the truth you know I have been hurtin' all along
Someway let me know, you want me girl
Every time you see me what do you see?
I feel like I'm a poor man and you're the queen
Oh baby, you're the only thing that I really need
Baby that's why
U make me wanna call you in the middle of the night
U make me wanna hold you till the mornin' light
U make me wanna love, U make me wanna fall
U make me wanna surrender my soul
"""
```


```python
content
```




    "You know U make me wanna\nYou know U make me wanna\nTo start it off, I know you know me\nTo come to think of it, it was only last week\nThat I had a dream about us, oh oh\nThat's why I am here, I'm writin' this song\nTo tell the truth you know I have been hurtin' all along\nSomeway let me know, you want me girl\nEvery time you see me what do you see?\nI feel like I'm a poor man and you're the queen\nOh baby, you're the only thing that I really need\nBaby that's why\nU make me wanna call you in the middle of the night\nU make me wanna hold you till the mornin' light\nU make me wanna love, U make me wanna fall\nU make me wanna surrender my soul\n"




```python
word_counter = defaultdict(int)
```


```python
word_counter
```




    defaultdict(int, {})




```python
contents = re.findall(r"[\w']+", content)
```


```python
for c in contents:
    word_counter[c] += 1
```


```python
word_counter
```




    defaultdict(int,
                {'Baby': 1,
                 'Every': 1,
                 'I': 6,
                 "I'm": 2,
                 'Oh': 1,
                 'Someway': 1,
                 'That': 1,
                 "That's": 1,
                 'To': 3,
                 'U': 7,
                 'You': 2,
                 'a': 2,
                 'about': 1,
                 'all': 1,
                 'along': 1,
                 'am': 1,
                 'and': 1,
                 'baby': 1,
                 'been': 1,
                 'call': 1,
                 'come': 1,
                 'do': 1,
                 'dream': 1,
                 'fall': 1,
                 'feel': 1,
                 'girl': 1,
                 'had': 1,
                 'have': 1,
                 'here': 1,
                 'hold': 1,
                 "hurtin'": 1,
                 'in': 1,
                 'it': 3,
                 'know': 6,
                 'last': 1,
                 'let': 1,
                 'light': 1,
                 'like': 1,
                 'love': 1,
                 'make': 7,
                 'man': 1,
                 'me': 11,
                 'middle': 1,
                 "mornin'": 1,
                 'my': 1,
                 'need': 1,
                 'night': 1,
                 'of': 2,
                 'off': 1,
                 'oh': 2,
                 'only': 2,
                 'poor': 1,
                 'queen': 1,
                 'really': 1,
                 'see': 2,
                 'song': 1,
                 'soul': 1,
                 'start': 1,
                 'surrender': 1,
                 'tell': 1,
                 'that': 1,
                 "that's": 1,
                 'the': 6,
                 'thing': 1,
                 'think': 1,
                 'this': 1,
                 'till': 1,
                 'time': 1,
                 'to': 1,
                 'truth': 1,
                 'us': 1,
                 'wanna': 7,
                 'want': 1,
                 'was': 1,
                 'week': 1,
                 'what': 1,
                 'why': 2,
                 "writin'": 1,
                 'you': 7,
                 "you're": 2})




```python
multiple_counter = {}

for k, v in word_counter.items():
    if(word_counter[k] > 1):
        multiple_counter[k] = v
```


```python
multiple_counter
```




    {'I': 6,
     "I'm": 2,
     'To': 3,
     'U': 7,
     'You': 2,
     'a': 2,
     'it': 3,
     'know': 6,
     'make': 7,
     'me': 11,
     'of': 2,
     'oh': 2,
     'only': 2,
     'see': 2,
     'the': 6,
     'wanna': 7,
     'why': 2,
     'you': 7,
     "you're": 2}




```python
mc = sorted(multiple_counter.items(), key=lambda x: x[1], reverse=True)
```


```python
mc
```




    [('me', 11),
     ('U', 7),
     ('make', 7),
     ('wanna', 7),
     ('you', 7),
     ('know', 6),
     ('I', 6),
     ('the', 6),
     ('To', 3),
     ('it', 3),
     ('You', 2),
     ('of', 2),
     ('only', 2),
     ('a', 2),
     ('oh', 2),
     ('why', 2),
     ("I'm", 2),
     ('see', 2),
     ("you're", 2)]




```python
for x in mc:
    print(x[0], "==>", x[1])
```

    me ==> 11
    U ==> 7
    make ==> 7
    wanna ==> 7
    you ==> 7
    know ==> 6
    I ==> 6
    the ==> 6
    To ==> 3
    it ==> 3
    You ==> 2
    of ==> 2
    only ==> 2
    a ==> 2
    oh ==> 2
    why ==> 2
    I'm ==> 2
    see ==> 2
    you're ==> 2



```python

```


---
**Score: 15**