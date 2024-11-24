---
title: Commentary
date: 2024-11-24
author: Your Name
cell_count: 15
score: 15
---

```python
# https://python.langchain.com/docs/how_to/structured_output/
# https://python.langchain.com/docs/how_to/
# https://platform.openai.com/usage
```


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
```


```python
llm = ChatOpenAI(model="gpt-4o-mini")
```


```python
from typing import Optional
from pydantic import BaseModel, Field

# Pydantic
class CricketCommentary(BaseModel):
    """Cricket Commenaty to tell user."""

    commentator: str     = Field(description = "Commentator")
    commentaty: str     = Field(description = "Commentary")
```


```python
structured_llm = llm.with_structured_output(CricketCommentary)
```


```python
def q(ball, score):
    return structured_llm.invoke(f"Tell me about cricket commentary for ball number {ball} and batsman scored {score}")
```


```python
q(2, 2)
```




    CricketCommentary(commentator='John Doe', commentaty="And here comes the second ball of the over. The bowler runs in, delivers a full-length ball, and the batsman is quick to react. He drives it elegantly through the covers, and that's a lovely shot! The ball races away to the boundary, and the batsman picks up two runs effortlessly. The crowd erupts in applause as he showcases his class.")




```python
q(2, 6)
```




    CricketCommentary(commentator='John Doe', commentaty="And here comes the second ball of the over! It's a full delivery on the leg stump, and the batsman has picked it beautifully. He swings his bat with all his might, sending the ball soaring over the boundary for a magnificent six! The crowd erupts in cheers as the batsman raises his bat in acknowledgment. What a shot!")




```python
import random
```


```python
for i in range(6):
    commentary = q(i+1, random.randint(0, 6))
    print(commentary)
    print('-' * 10)
```

    commentator='Mark Nicholas' commentaty="And here we go! The first ball of the match is bowled. It's a good length delivery on off stump. The batsman is cautious, not wanting to take any risks on the very first ball. He leaves it alone, and the ball goes through to the keeper. No runs on the board as yet!"
    ----------
    commentator='John Doe' commentaty='And here comes the second ball of the over. The bowler runs in, delivering a sharp delivery full on off stump. The batsman, looking to get off the mark, plays a defensive shot but misses it completely. No run scored, and the batsman remains on zero.'
    ----------
    commentator='Jim Maxwell' commentaty='And here comes the bowler for ball number 3. He runs in, bowls a full delivery and oh! What a shot! The batsman launches it high over mid-wicket and it sails into the stands for a magnificent six! The crowd erupts in joy, a fantastic connection there. The batsman is looking in great form!'
    ----------
    commentator='Mark Nicholas' commentaty="And here comes the fourth ball of the over! The bowler runs in with purpose, but wait! The batsman has read that beautifully. He steps down the pitch and launches it into the air. It's a massive hit, soaring high over the boundary! That's six runs! The crowd erupts in cheers as the batsman raises his bat in acknowledgment. What a shot!"
    ----------
    commentator='John Doe' commentaty="And here comes the fifth ball of the over. The bowler runs in, delivers a quick ball, and the batsman plays a lovely shot! He finds the gap between the fielders and scampers through for a quick single. That's a well-placed shot, and the batsman has now moved to 3 runs. The crowd appreciates that effort!"
    ----------
    commentator='John Doe' commentaty="And here we go, it's ball number 6 of the over. The bowler runs in, delivers the ball, and it's a full toss! The batsman sees it early, gets his bat down, and with a powerful swing, he drives it through the covers. The ball races away to the boundary, and that's a fantastic shot! The batsman has scored 5 runs on this ball, moving his score up and putting pressure on the bowler."
    ----------



```python

```


---
**Score: 15**