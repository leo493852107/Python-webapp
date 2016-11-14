#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Create by Leo on 14/11/2016



import logging

from transwarp.web import get, view

from models import User, Blog, Comment


@view('test_users.html')
@get('/')
def test_users():
    users = User.find_all()
    return dict(users=users)
