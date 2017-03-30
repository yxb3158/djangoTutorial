#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
'''
Created on 2017年3月10日 下午7:28:47

@author: yxb
'''
from django.http import HttpResponse
import datetime
def hello(request):
    return HttpResponse("Hello world")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)