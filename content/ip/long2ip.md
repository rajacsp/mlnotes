---
title: Long2Ip
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
import ipaddress

def long_to_ip(ip_long):
    # Convert long integer to IPv4 string
    return str(ipaddress.IPv4Address(ip_long))

# Example usage
ip_long = 3232235777
ip = long_to_ip(ip_long)
print(f"Long Integer: {ip_long} -> IP Address: {ip}")

```

    Long Integer: 3232235777 -> IP Address: 192.168.1.1



```python

```


---
**Score: 0**