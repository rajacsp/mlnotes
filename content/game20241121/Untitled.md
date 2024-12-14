---
title: Untitled
date: 2024-12-14
author: Your Name
cell_count: 4
score: 0
---

```python
!pip install smtplib
```

    [31mERROR: Could not find a version that satisfies the requirement smtplib (from versions: none)[0m[31m
    [0m[31mERROR: No matching distribution found for smtplib[0m[31m
    [0m


```python
fromaddr = 'fromuser@gmail.com'
toaddrs  = 'touser@gmail.com'

# Writing the message (this message will appear in the email)

msg = 'Enter you message here'

# Gmail Login

username = 'username'
password = 'password'

# Sending the mail  

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    Cell In[7], line 15
         11 password = 'password'
         13 # Sending the mail  
    ---> 15 server = smtplib.SMTP('smtp.gmail.com:587')
         16 server.starttls()
         17 server.login(username,password)


    NameError: name 'smtplib' is not defined



```python

```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    Cell In[4], line 1
    ----> 1 one


    NameError: name 'one' is not defined



```python

```


---
**Score: 0**