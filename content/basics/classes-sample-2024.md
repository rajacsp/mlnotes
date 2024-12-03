---
title: Classes-Sample-2024
date: 2024-12-03
author: Your Name
cell_count: 4
score: 0
---

```python
import os
import urllib.parse
from urllib.parse import urlparse

class Client:
    def __init__(self, base_url, http_client):
        self.base_url = base_url
        self.http_client = http_client


def client_from_environment():
    default_port = "11434"
    ollama_host = os.getenv("OLLAMA_HOST", "")

    # Parse scheme and hostport
    if "://" in ollama_host:
        scheme, hostport = ollama_host.split("://", 1)
    else:
        scheme, hostport = "http", ollama_host

    # Adjust default port based on scheme
    if scheme == "http":
        default_port = "80"
    elif scheme == "https":
        default_port = "443"

    # Trim trailing slashes
    hostport = hostport.rstrip("/")

    # Parse host and port
    try:
        host, port = hostport.split(":", 1)
    except ValueError:
        host, port = hostport, default_port

    # Handle cases where host is an IP address or hostname
    if not host:
        host = "127.0.0.1"
    elif not port.isdigit():
        port = default_port

    # Construct base URL
    base_url = f"{scheme}://{host}:{port}"

    # Return Client instance
    return Client(base_url=base_url, http_client=None)
```


```python
os.environ["OLLAMA_HOST"] = "http://localhost:8080"  # Example setting
client = client_from_environment()
print(f"Client created with base URL: {client.base_url}")
```

    Client created with base URL: http://localhost:8080



```python
!echo $OLLAMA_HOST
```

    http://localhost:8080



```python

```


---
**Score: 0**