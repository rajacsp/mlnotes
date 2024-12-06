---
title: Ip Whois
date: 2024-12-06
author: Your Name
cell_count: 4
score: 0
---

---
title: "IP Whois Simple"
author: "Rj"
date: 2019-04-20
description: "-"
type: technical_note
draft: false
---

```python
from ipwhois import IPWhois
from pprint import pprint
```


```python
obj = IPWhois('133.1.2.5')
results = obj.lookup_whois(inc_nir=True)
pprint(results)
```

    {'asn': '4730',
     'asn_cidr': '133.1.0.0/16',
     'asn_country_code': 'JP',
     'asn_date': '1997-03-01',
     'asn_description': 'ODINS Osaka University, JP',
     'asn_registry': 'apnic',
     'nets': [{'address': 'Urbannet-Kanda Bldg 4F\n'
                          '3-6-2 Uchi-Kanda\n'
                          'Chiyoda-ku, Tokyo 101-0047,Japan',
               'cidr': '133.0.0.0/8',
               'city': None,
               'country': 'JP',
               'created': None,
               'description': 'Japan Network Information Center',
               'emails': ['hostmaster@nic.ad.jp'],
               'handle': 'JNIC1-AP',
               'name': 'JPNIC-NET-JP-ERX',
               'postal_code': None,
               'range': '133.0.0.0 - 133.255.255.255',
               'state': None,
               'updated': None}],
     'nir': {'nets': [{'address': None,
                       'cidr': '133.1.0.0/16',
                       'contacts': {'admin': {'division': 'Department of '
                                                          'Information and '
                                                          'Communications '
                                                          'Technology Services',
                                              'email': 'odins-room@odins.osaka-u.ac.jp',
                                              'fax': '06-6879-8988',
                                              'name': 'Yoshihide, Minami',
                                              'organization': 'Osaka University',
                                              'phone': '06-6879-8815',
                                              'reply_email': 'reg@jpdirect.jp',
                                              'title': 'Specialist',
                                              'updated': '2015-08-13T09:08:34'},
                                    'tech': {'division': 'Department of '
                                                         'Information and '
                                                         'Communications '
                                                         'Technology Services',
                                             'email': 'odins-room@odins.osaka-u.ac.jp',
                                             'fax': '06-6879-8988',
                                             'name': 'Yoshihide, Minami',
                                             'organization': 'Osaka University',
                                             'phone': '06-6879-8815',
                                             'reply_email': 'reg@jpdirect.jp',
                                             'title': 'Specialist',
                                             'updated': '2015-08-13T09:08:34'}},
                       'country': 'JP',
                       'created': None,
                       'handle': 'OSAKAU-NET',
                       'name': 'Osaka University',
                       'nameservers': ['a.osaka-u.ac.jp',
                                       'b.osaka-u.ac.jp',
                                       'dns-x.sinet.ad.jp'],
                       'postal_code': None,
                       'range': '133.1.0.1 - 133.1.255.255',
                       'updated': '2015-01-14T02:50:03'}],
             'query': '133.1.2.5',
             'raw': None},
     'query': '133.1.2.5',
     'raw': None,
     'raw_referral': None,
     'referral': None}



```python

```


---
**Score: 0**