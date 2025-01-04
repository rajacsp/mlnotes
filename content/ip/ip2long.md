---
title: Ip2Long
date: 2025-01-04
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

def ip_to_long(ip):
    # Convert IP string to a long integer
    return int(ipaddress.IPv4Address(ip))

# Example usage
ip = "192.168.1.1"
ip_long = ip_to_long(ip)
print(f"IP Address: {ip} -> Long Integer: {ip_long}")
```

    IP Address: 192.168.1.1 -> Long Integer: 3232235777



```python

```


---
**Score: 0**