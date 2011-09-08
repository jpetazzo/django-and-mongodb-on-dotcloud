#!/usr/bin/env python
from wsgi import *
from django.contrib.auth.models import User
from pymongo.errors import AutoReconnect
import time
deadline = time.time() + 600 
while time.time() < deadline:
    try:
        User.objects.count()
        print 'Successfully connected to database.'
        exit(0)
    except AutoReconnect:
        print 'Could not connect to database. Waiting a little bit.'
        time.sleep(10)
print 'Could not connect to database after 10 minutes. Something is wrong.'
exit(1)
