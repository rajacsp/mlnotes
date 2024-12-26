---
title: Ip-Generator-With-Faker
date: 2024-12-26
author: Your Name
cell_count: 5
score: 5
---

```python

```


```python
import pyutil as pyu
pyu.get_local_pyinfo()
```




    'conda env: ml312-2024; pyv: 3.12.7 | packaged by Anaconda, Inc. | (main, Oct  4 2024, 13:27:36) [GCC 11.2.0]'




```python
!pip install faker
```

    Collecting faker
      Using cached Faker-33.1.0-py3-none-any.whl.metadata (15 kB)
    Requirement already satisfied: python-dateutil>=2.4 in /home/rajaraman/miniconda3/envs/ml312-2024/lib/python3.12/site-packages (from faker) (2.9.0.post0)
    Requirement already satisfied: typing-extensions in /home/rajaraman/miniconda3/envs/ml312-2024/lib/python3.12/site-packages (from faker) (4.12.2)
    Requirement already satisfied: six>=1.5 in /home/rajaraman/miniconda3/envs/ml312-2024/lib/python3.12/site-packages (from python-dateutil>=2.4->faker) (1.17.0)
    Using cached Faker-33.1.0-py3-none-any.whl (1.9 MB)
    Installing collected packages: faker
    Successfully installed faker-33.1.0



```python
from faker import Faker

# Initialize Faker
fake = Faker()

# Function to generate a public IP address
def generate_public_ip():
    while True:
        ip = fake.ipv4()
        # Split the IP address into its octets
        octets = list(map(int, ip.split('.')))
        # Check if it's in private IP ranges
        if not (
            (octets[0] == 10) or  # 10.0.0.0 - 10.255.255.255
            (octets[0] == 172 and 16 <= octets[1] <= 31) or  # 172.16.0.0 - 172.31.255.255
            (octets[0] == 192 and octets[1] == 168)  # 192.168.0.0 - 192.168.255.255
        ):
            return ip

# Generate multiple public IPs
public_ips = [generate_public_ip() for _ in range(10)]

# Print the generated IPs
print("Random Public IP Addresses:")
for ip in public_ips:
    print(ip)

```

    Random Public IP Addresses:
    2.37.66.211
    52.117.186.185
    37.240.60.172
    88.138.63.214
    144.169.15.106
    156.100.123.121
    5.82.142.108
    82.203.84.159
    152.120.45.241
    67.134.215.107



```python

```


---
**Score: 5**