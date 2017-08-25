# coding: utf-8
import os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0, parentdir)

from ApiMessenger.fbmq import Page
from CoreChatbot.Preparation.config import CONFIG

page = Page(CONFIG['FACEBOOK_TOKEN'])


@page.after_send
def after_send(payload, response):
    # print('AFTER_SEND : ' + payload.to_json())
    # print('RESPONSE : ' + response.text)
    print ('day la ham after_send: Preparation/fbpage.py')
