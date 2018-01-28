#!/usr/bin/env python3
import fazlamesai

key = input('Please enter an API key: ')
c = fazlamesai.Client(key)

for link in c.get_posts():
    print(link.title)
