---
title: Name-Collector
date: 2025-01-03
author: Your Name
cell_count: 4
score: 0
---

---
title: "Name Collector"
author: "Rj"
date: 2019-04-20
description: "List Test"
type: technical_note
draft: false
---

```python
import requests
from bs4 import BeautifulSoup
```


```python
# Collect and parse first page
page = requests.get('https://www.babble.com/pregnancy/1000-most-popular-boy-names/')
soup = BeautifulSoup(page.text, 'html.parser')    

#print(soup)    

items = soup.select('main.tm-single-content li a')

item_list = ''
for item in items:
    #print(item.get_text())
    item_list =  item_list + ',' +str(item.get_text())

print(item_list)
```

    ,Liam,Noah,William,James,Logan,Benjamin,Mason,Elijah,Oliver,Jacob,Lucas,Michael,Alexander,Ethan,Daniel,Matthew,Aiden,Henry,Joseph,Jackson,Samuel,Sebastian,David,Carter,Wyatt,Jayden,John,Owen,Dylan,Luke,Gabriel,Anthony,Isaac,Grayson,Jack,Julian,Levi,Christopher,Joshua,Andrew,Lincoln,Mateo,Ryan,Jaxon,Nathan,Aaron,Isaiah,Thomas,Charles,Caleb,Josiah,Christian,Hunter,Eli,Jonathan,Connor,Landon,Adrian,Asher,Cameron,Leo,Theodore,Jeremiah,Hudson,Robert,Easton,Nolan,Nicholas,Ezra,Colton,Angel,Brayden,Jordan,Dominic,Austin,Ian,Adam,Elias,Greyson,Jose,Ezekiel,Carson,Evan,Maverick,Bryson,Jace,Cooper,Xavier,Parker,Roman,Jason,Santiago,Chase,Sawyer,Gavin,Leonardo,Ayden,Jameson,Kevin,Bentley,Zachary,Everett,Axel,Tyler,Micah,Vincent,Weston,Miles,Wesley,Nathaniel,Harrison,Brandon,Cole,Declan,Luis,Braxton,Damian,Silas,Ryder,Bennett,George,Emmett,Justin,Max,Diego,Carlos,Maxwell,Kingston,Ivan,Maddox,Juan,Jayce,Rowan,Eric,Jesus,Calvin,Abel,King,Camden,Amir,Blake,Alex,Brody,Malachi,Emmanuel,Jonah,Beau,Jude,Antonio,Alan,Elliott,Elliot,Waylon,Xander,Timothy,Victor,Bryce,Finn,Brantley,Edward,Abraham,Patrick,Grant,Hayden,Richard,Miguel,Joel,Gael,Rhett,Steven,Graham,Jasper,Jesse,Matteo,Dean,Preston,August,Oscar,Jeremy,Alejandro,Marcus,Dawson,Lorenzo,Zion,Maximus,Strong Boy Names That'll Empower Your Little Guy Right from Day 1,Biblical Boy Names That Have Stood the Test of Time,Classic Boy Names You'll Never Get Tired of Hearing,'Star Wars'-Inspired Baby Names Continue to Climb the Charts



```python

```


---
**Score: 0**