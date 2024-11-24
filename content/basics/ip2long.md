---
title: Ip2Long
date: 2024-11-24
author: Your Name
cell_count: 8
score: 5
---

---
title: "IP To Long"
author: "Rj"
date: 2019-04-20
description: "List Test"
type: technical_note
draft: false
---

```python
import math
```


```python
class AuthException(Exception):
    pass
```


```python
def ip_to_long(ip_address):
    '''
        
    '''
    
    if(ip_address == '0:0:0:0:0:0:0:1'):
        ip_address = '127.0.0.1'
        
    ip_address_array = ip_address.split('.')
    
    if(len(ip_address_array) != 4):    
        raise AuthException('Invalid Ip')
    
    #print(ip_address_array[1])
    
    num = 0
    for i in range(len(ip_address_array)):
        #print(ip_address_array[i])
        power = 3 - i
        num = num + ( (int(ip_address_array[i]) % 256 * int(math.pow(256, power)) ))
    
    return num
```


```python
ip_long = ip_to_long('10.3.81.34')        
print(ip_long)
```

    167989538



```python
def long_to_ip(ip):
    
    ip_address = ((ip >> 24) & 0xFF) + "." + ((ip >> 16) & 0xFF) + "." + ((ip >> 8) & 0xFF) + "." + (ip & 0xFF)
    
    return ip_address
```


```python
#ip_ = long_to_ip(int(167989538))
        
#print(ip_)
```


```python

```


---
**Score: 5**