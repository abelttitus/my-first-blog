#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 13:22:39 2019

@author: iist
"""

from django.urls import path
from . import views

urlpatterns=[path('',views.post_list,name='post_list'),]