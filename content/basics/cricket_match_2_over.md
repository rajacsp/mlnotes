---
title: Cricket Match 2 Over
date: 2024-12-13
author: Your Name
cell_count: 10
score: 10
---

---
title: "Cricket Match 2 Overs"
author: "Rj"
date: 2019-04-20
description: "List Test"
type: technical_note
draft: false
---

```python
import time
import random as rd
```


```python
team_1_score = 0
team_2_score = 0
```


```python
def play_over(over, t_score):
    
    print('Over ', over)
    
    for x in range(6):
        
        score = rd.randint(0, 6)
        t_score += score
        print('Ball ', (x+1), score)
        
        time.sleep(0.5)
        
    print('')
    return t_score
```


```python
# Team 1 Batting

team_1_score = play_over(1, team_1_score)
team_1_score = play_over(2, team_1_score)
```

    Over  1
    Ball  1 4
    Ball  2 5
    Ball  3 4
    Ball  4 2
    Ball  5 6
    Ball  6 5
    
    Over  2
    Ball  1 4
    Ball  2 1
    Ball  3 1
    Ball  4 4
    Ball  5 5
    Ball  6 6
    



```python
team_1_score
```




    47




```python
# Team 2 Batting

team_2_score = play_over(1, team_2_score)
team_2_score = play_over(2, team_2_score)
```

    Over  1
    Ball  1 3
    Ball  2 1
    Ball  3 4
    Ball  4 1
    Ball  5 0
    Ball  6 5
    
    Over  2
    Ball  1 4
    Ball  2 4
    Ball  3 3
    Ball  4 3
    Ball  5 3
    Ball  6 1
    



```python
print('Team 1 Score : ', team_1_score)
print('Team 2 Score : ', team_2_score)
```

    Team 1 Score :  47
    Team 2 Score :  32



```python
if(team_1_score > team_2_score):
    print('Team 1 won')
elif (team_1_score < team_2_score):
    print('Team 2 won')
else:
    print('Draw')
```

    Team 1 won



```python

```


---
**Score: 10**