---
title: Consume-Rest-Api
date: 2025-05-17
author: Your Name
cell_count: 26
score: 25
---

```python

```


```python
import requests
import json
```


```python
response = requests.get("https://randomuser.me/api/")
```


```python
response_json = response.json()
```


```python
print(response_json)
```

    {'results': [{'gender': 'female', 'name': {'title': 'Ms', 'first': 'Mia', 'last': 'Walker'}, 'location': {'street': {'number': 8562, 'name': 'Port Hills Road'}, 'city': 'Hamilton', 'state': 'Waikato', 'country': 'New Zealand', 'postcode': 45938, 'coordinates': {'latitude': '54.8821', 'longitude': '15.6902'}, 'timezone': {'offset': '+4:30', 'description': 'Kabul'}}, 'email': 'mia.walker@example.com', 'login': {'uuid': 'acdada4d-6fc5-442c-be57-b8db60d5ed2b', 'username': 'heavypeacock555', 'password': 'fresh', 'salt': '7WvriXB4', 'md5': 'f5bbe66407188487fcb9e3255bb161e2', 'sha1': '421d5105c937de66947e9de0ee491df3cfbd720e', 'sha256': 'fe1fca89f0b9348f8a4be3540377b777eef406e3ffd8668694c48223b38a04e7'}, 'dob': {'date': '1992-12-04T19:33:10.191Z', 'age': 32}, 'registered': {'date': '2016-12-12T05:33:38.658Z', 'age': 8}, 'phone': '(083)-981-7119', 'cell': '(233)-717-4000', 'id': {'name': '', 'value': None}, 'picture': {'large': 'https://randomuser.me/api/portraits/women/38.jpg', 'medium': 'https://randomuser.me/api/portraits/med/women/38.jpg', 'thumbnail': 'https://randomuser.me/api/portraits/thumb/women/38.jpg'}, 'nat': 'NZ'}], 'info': {'seed': 'ce107bb801696e75', 'results': 1, 'page': 1, 'version': '1.4'}}



```python
# response_json
```
print(json.dumps(response_json, indent=4))

```python
result_first_item = response_json["results"][0]
```


```python
result_first_item
```




    {'gender': 'male',
     'name': {'title': 'Mr', 'first': 'Willie', 'last': 'Chambers'},
     'location': {'street': {'number': 5013, 'name': 'The Green'},
      'city': 'Ely',
      'state': 'West Glamorgan',
      'country': 'United Kingdom',
      'postcode': 'D9 8SX',
      'coordinates': {'latitude': '-10.6600', 'longitude': '-173.3726'},
      'timezone': {'offset': '+7:00', 'description': 'Bangkok, Hanoi, Jakarta'}},
     'email': 'willie.chambers@example.com',
     'login': {'uuid': 'f2c8e5e0-ec49-4d8f-998c-7a5e952f9982',
      'username': 'orangerabbit542',
      'password': 'momo',
      'salt': '5VqLYF7g',
      'md5': 'b36751c710160b6152eba752a957c785',
      'sha1': '63effd9e597cbbc9da0909ddd35588a826aab7f1',
      'sha256': '88c465cf36822c116ebefdfa11d992f092e773b92d9a33a368a8ff18b1096da0'},
     'dob': {'date': '1980-10-21T11:45:31.984Z', 'age': 44},
     'registered': {'date': '2009-07-22T12:49:50.771Z', 'age': 15},
     'phone': '017683 28131',
     'cell': '07489 074118',
     'id': {'name': 'NINO', 'value': 'OW 22 16 91 P'},
     'picture': {'large': 'https://randomuser.me/api/portraits/men/91.jpg',
      'medium': 'https://randomuser.me/api/portraits/med/men/91.jpg',
      'thumbnail': 'https://randomuser.me/api/portraits/thumb/men/91.jpg'},
     'nat': 'GB'}




```python
user_last_name = result_first_item.get("name", {}).get("last", "Doe")
```


```python
user_last_name
```




    'Chambers'




```python
user_gender = result_first_item.get("gender", "NA")
```


```python
user_gender
```




    'male'




```python
postcode = result_first_item.get("location", {}).get("postcode", "NA")
```


```python
postcode
```




    'D9 8SX'




```python
user_email = result_first_item.get("email", "NA")
```


```python
user_email
```




    'willie.chambers@example.com'




```python
user_medium_pic = result_first_item.get("picture", {}).get("medium", "NA")
```


```python
user_medium_pic
```




    'https://randomuser.me/api/portraits/med/men/91.jpg'




```python
result_dict = {
    "last_name" : user_last_name,
    "gender" : user_gender,
    "postcode" : postcode,
    "email" : user_email,
    "picture" : user_medium_pic
}
```


```python
result_dict
```




    {'last_name': 'Chambers',
     'gender': 'male',
     'postcode': 'D9 8SX',
     'email': 'willie.chambers@example.com',
     'picture': 'https://randomuser.me/api/portraits/med/men/91.jpg'}




```python

```


```python
def get_user_details(response_json):

    result_first_item = response_json["results"][0]

    user_last_name = result_first_item.get("name", {}).get("last", "Doe")
    user_gender = result_first_item.get("gender", "NA")
    postcode = result_first_item.get("location", {}).get("postcode", "NA")
    user_email = result_first_item.get("email", "NA")
    user_medium_pic = result_first_item.get("picture", {}).get("medium", "NA")
    
    result1_dict = {
        "last_name" : user_last_name,
        "gender" : user_gender,
        "postcode" : postcode,
        "email" : user_email,
        "picture" : user_medium_pic
    }

    return result1_dict
```


```python
res1 = requests.get("https://randomuser.me/api/")
# res1.json()
get_user_details(res1.json())
```




    {'last_name': 'Kennedy',
     'gender': 'female',
     'postcode': 83714,
     'email': 'louise.kennedy@example.com',
     'picture': 'https://randomuser.me/api/portraits/med/women/29.jpg'}




```python

```


```python

```


---
**Score: 25**