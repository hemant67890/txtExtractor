#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8023334352:AAF0JovhXU2GOhBRK1sOSz7nV0AjHIF7g_s")
    API_ID = int(os.environ.get("API_ID", "26512964"))
    API_HASH = os.environ.get("API_HASH", "e5d187c6c7a0919ccb8866f76f655701")
    AUTH_USERS = os.environ.get("AUTH_USERS", "6326227068")
