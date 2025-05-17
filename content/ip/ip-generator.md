---
title: Ip-Generator
date: 2025-05-17
author: Your Name
cell_count: 4
score: 0
---

```python

```


```python
import pyutil as pyu
pyu.get_local_pyinfo()
```




    'conda env: ml312-2024; pyv: 3.12.7 | packaged by Anaconda, Inc. | (main, Oct  4 2024, 13:27:36) [GCC 11.2.0]'




```python
# public ip

import random

def generate_public_ip():
    # Exclude private IP ranges
    excluded_ranges = [
        (10, 10),  # 10.0.0.0 - 10.255.255.255
        (172, 172),  # 172.16.0.0 - 172.31.255.255
        (192, 192),  # 192.168.0.0 - 192.168.255.255
    ]

    while True:
        # Generate random first octet
        first = random.randint(1, 223)
        
        # Ensure it's not a private IP range
        if not any(start <= first <= end for start, end in excluded_ranges):
            break

    # Generate the other octets (2-4)
    second = random.randint(0, 255)
    third = random.randint(0, 255)
    fourth = random.randint(0, 255)

    # Combine to create the IP
    return f"{first}.{second}.{third}.{fourth}"

# Generate multiple public IPs
public_ips = [generate_public_ip() for _ in range(10)]

# Print the generated IPs
print("Random Public IP Addresses:")
for ip in public_ips:
    print(ip)
```

    Random Public IP Addresses:
    223.59.16.209
    88.224.147.129
    144.148.121.177
    90.210.54.132
    143.64.56.165
    176.220.110.253
    55.141.50.54
    168.71.210.26
    127.184.181.104
    116.199.204.222



```python

```


---
**Score: 0**