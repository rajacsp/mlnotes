---
title: Learner-Score-Collector
date: 2024-12-14
author: Your Name
cell_count: 15
score: 15
---

```python

```


```python
!pip show beautifulsoup4 | grep "Version:"
```

    Version: 4.12.3



```python
import requests
from bs4 import BeautifulSoup

# URL to scrape
url = "https://stevesanjay.github.io/pynotes/archives.html"

# Send a GET request
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find the element containing the "overall-score"
# Modify the tag and class based on the structure of the HTML
overall_score_element = soup.find(class_="overall-score")  # Assuming it has this class

# Extract and print the score
if overall_score_element:
    overall_score = overall_score_element.get_text(strip=True)
    print("Overall Score:", overall_score)
else:
    print("Overall Score not found.")
```

    Overall Score not found.



```python

```


```python
# URL of the page
url = "https://stevesanjay.github.io/pynotes/archives.html"

# Fetch the page content
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find the <p> tag that contains "Overall Score:"
overall_score_element = soup.find('p', text=lambda x: x and "Overall Score:" in x)
```

    /tmp/ipykernel_4024956/3784387840.py:11: DeprecationWarning: The 'text' argument to find()-type methods is deprecated. Use 'string' instead.
      overall_score_element = soup.find('p', text=lambda x: x and "Overall Score:" in x)



```python
overall_score_element
```


```python
all_p = soup.find_all('p')
```


```python
all_p
```




    [<p><strong>Overall Score:</strong> 510</p>]




```python
overall_score_element = soup.find('p', text=lambda x: x and "Overall Score:" in x)
```

    /tmp/ipykernel_4024956/145144256.py:1: DeprecationWarning: The 'text' argument to find()-type methods is deprecated. Use 'string' instead.
      overall_score_element = soup.find('p', text=lambda x: x and "Overall Score:" in x)



```python
overall_score_element
```


```python
overall_score_element = soup.find('p')  # Locate the <p> tag
if overall_score_element:
    strong_tag = overall_score_element.find('strong')  # Locate the <strong> tag inside <p>
    if strong_tag and "Overall Score:" in strong_tag.text:
        overall_score = overall_score_element.get_text(strip=True).replace("Overall Score:", "").strip()
        print("Overall Score:", overall_score)
    else:
        print("Strong tag with 'Overall Score' not found.")
else:
    print("Overall Score not found.")
```

    Overall Score: 510



```python

```


```python
def get_score(url):

    # Fetch the page content
    response = requests.get(url)
    
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    overall_score_element = soup.find('p')  # Locate the <p> tag
    if overall_score_element:
        strong_tag = overall_score_element.find('strong')  # Locate the <strong> tag inside <p>
        if strong_tag and "Overall Score:" in strong_tag.text:
            overall_score = overall_score_element.get_text(strip=True).replace("Overall Score:", "").strip()
            return int(overall_score)
        return -1

    return -1    
```


```python
get_score("https://stevesanjay.github.io/pynotes/archives.html")
```




    510




```python

```


---
**Score: 15**