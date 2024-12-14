---
title: Book-Review-Analyzer
date: 2024-12-14
author: Your Name
cell_count: 10
score: 10
---

---
title: "Book Review Analyzer"
author: "Rj"
date: 2019-04-20
description: "List Test"
type: technical_note
draft: false
---

```python
import json
from pprint import pprint
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
```


```python
data = json.load(open('book-review.json'))
```


```python
twt = data['reviews'][1]['text']
```


```python
twt
```




    'the text reveals the mentality of the CIA so that it reveals the group think which is necessary for understanding its philosophical shallowness'




```python
tweet_index = []
tweet_date = []
positive_reviews = []
negative_reviews = []
```


```python
tw_counter = 0
def analyze_local(sentence, tw_date):
    sid = SentimentIntensityAnalyzer()
    
    print(sentence)
    global tw_counter
    tw_counter += 1
    ss = sid.polarity_scores(sentence)
    print(ss['pos'])
    positive_reviews.append(ss['pos'])
    negative_reviews.append(-ss['neg'])    
    tweet_index.append(tw_counter)
    current_date = pd.to_datetime(tw_date).date()
    #print(current_date)
    tweet_date.append(current_date)
    
    '''
    for k in sorted(ss):
        #print(ss)
        print('{0}: {1}, '.format(k, ss[k]), end = '')
    '''
```


```python
def plot_data():
    # evenly sampled time at 200ms intervals
    
    #myneglist = [ -x for x in negative_reviews]

    # red dashes, blue squares and green triangles
    plt.title('Sentiment Analysis : Positive (blue) and Negative (red)')
    plt.plot(tweet_date, positive_reviews, 'b--', tweet_date, negative_reviews, 'r--')
    #plt.plot(tweet_date, negative_reviews, 'r--')
    plt.show()
```


```python
print(data['reviews'][0])    

total_reviews = len(data['reviews'])
for x in range(total_reviews):
    analyze_local(data['reviews'][x]['text'], data['reviews'][x]['created_at'])

plot_data() 
```

    {'text': 'Much too concerned with the structure and functions of the CIA and not with the crentral theme suggested by the title.', 'created_at': 'Mon Jan 01 13:37:52 +0000 2018'}
    Much too concerned with the structure and functions of the CIA and not with the crentral theme suggested by the title.
    0.0
    the text reveals the mentality of the CIA so that it reveals the group think which is necessary for understanding its philosophical shallowness
    0.0
    The book is what I expected to be and more....now I have confirmation. Should I believe what I read........this is another question which the reader can only answer for his / her self. The world which we all live in has many twists on the truth and lies about everything....obviously our actions may they be positive or negative will be definitely affecting the out come of our lives. The book is worth reading as far has I'm concerned.
    0.125
    I guess a gag order is a gag order. I was disappointed with this book. There wasn't anything in it that you couldn't find on line with browser search. It seemed to be more pro Cia then his video's that talked about what his family was put through. Which only a couple of pages at the end spoke about in heavy blanked out sections. I would not buy any more of his other books if they are going to be like this one. He may have put his heart and soul into it but having the Cia approve everything that was written just doesn't cut it for me. Get books that aren't censored by Cia if you want real information. Like one reviewer said, this is not a whistle blower book.
    0.078
    The book is easy to read and follow. It is very understandable along with a lot of intrigue on the workings of the CIA. It's difficult to understand the treatment by the CIA of one of their officials and long time employee. His treatment by them was off the charts and some ot his co-workers, superiors and others were off the reservation. I recommend for anyone interested in how our loyal, patriotic public servants are treated when they don't adhere to a direction that is contrary to our Country.
    0.138
    Excellent source of information about our government and how corruption take s hold when we as citizens and political oversight management fail to pay attention.
    0.125
    Lots of info.Goes in line with other books I have read.This will open your eyes to what the gov is doing that the media will not tell you.
    0.0
    The detail of what an agent goes through was intriguing. The problem is, a lot of stuff he talked about regarding 9/11 and the Iraq war was regurgitated mainstream media talking points. He really didn't expose what really went on behind the scenes like real whistleblower agents already have. Very disappointing in that sense.
    0.068


    /Users/rajacsp/anaconda3/envs/py36/lib/python3.6/site-packages/pandas/plotting/_converter.py:129: FutureWarning: Using an implicitly registered datetime converter for a matplotlib plotting method. The converter was registered by pandas on import. Future versions of pandas will require you to explicitly register matplotlib converters.
    
    To register the converters:
    	>>> from pandas.plotting import register_matplotlib_converters
    	>>> register_matplotlib_converters()
      warnings.warn(msg, FutureWarning)



    
![png](/mlnotes/images/book-review-analyzer_8_2.png)
    



```python

```


---
**Score: 10**