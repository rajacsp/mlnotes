---
title: Cencode-Dcencode
date: 2024-12-13
author: Your Name
cell_count: 5
score: 5
---

```python

```


```python
import uuid
import base64

def encode_to_8_characters(guid: str) -> str:
    """
    Encode a GUID into an 8-character string.
    """
    # Convert GUID to bytes
    guid_bytes = uuid.UUID(guid).bytes
    # Encode to base64 and take the first 8 characters
    encoded = base64.urlsafe_b64encode(guid_bytes).decode('utf-8')[:8]
    return encoded

def decode_from_8_characters(encoded: str, original_guid: str) -> str:
    """
    Decode the 8-character string back to the original GUID.
    """
    # Convert the original GUID to bytes (needed for verification)
    original_bytes = uuid.UUID(original_guid).bytes
    # Decode back from base64 (with padding)
    decoded_bytes = base64.urlsafe_b64decode(encoded + '=='[:len(encoded) % 4])
    # Verify and return the original GUID
    if decoded_bytes == original_bytes:
        return str(uuid.UUID(bytes=decoded_bytes))
    else:
        raise ValueError("Decoded value does not match the original GUID.")

# Example usage
guid = "6749fcd3-4554-800f-b668-b3cdbb5c89ea"
encoded = encode_to_8_characters(guid)
print("Encoded:", encoded)

decoded = decode_from_8_characters(encoded, guid)
print("Decoded:", decoded)
```

    Encoded: Z0n800VU



    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    Cell In[1], line 33
         30 encoded = encode_to_8_characters(guid)
         31 print("Encoded:", encoded)
    ---> 33 decoded = decode_from_8_characters(encoded, guid)
         34 print("Decoded:", decoded)


    Cell In[1], line 26, in decode_from_8_characters(encoded, original_guid)
         24     return str(uuid.UUID(bytes=decoded_bytes))
         25 else:
    ---> 26     raise ValueError("Decoded value does not match the original GUID.")


    ValueError: Decoded value does not match the original GUID.



```python

```


```python
import uuid
import hashlib

def encode_to_8_characters(guid: str) -> str:
    """
    Encode a GUID into an 8-character string using a hash function.
    """
    # Create a hash of the GUID
    hashed = hashlib.sha256(guid.encode()).hexdigest()
    # Use the first 8 characters of the hash as the encoded string
    return hashed[:8]

def decode_with_lookup(encoded: str, lookup: dict) -> str:
    """
    Decode the 8-character string back to the original GUID using a lookup table.
    """
    if encoded in lookup:
        return lookup[encoded]
    else:
        raise ValueError("Encoded value not found in the lookup table.")

# Example usage
guid = "6749fcd3-4554-800f-b668-b3cdbb5c89ea"

# Create a lookup table for the encoding
lookup_table = {}

# Encode the GUID
encoded = encode_to_8_characters(guid)
lookup_table[encoded] = guid
print("Encoded:", encoded)

# Decode the GUID using the lookup table
decoded = decode_with_lookup(encoded, lookup_table)
print("Decoded:", decoded)
```

    Encoded: dda39475
    Decoded: 6749fcd3-4554-800f-b668-b3cdbb5c89ea



```python

```


---
**Score: 5**