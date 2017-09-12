# -*- coding: utf-8 -*-
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from ApiMessenger import Attachment, Template
from ApiMessenger.payload import QuickReply
from ApiMessenger.fbmq import Page

import CoreChatbot.Preparation.messenger
from CoreChatbot.Preparation.config import CONFIG
from CoreChatbot.Preparation.fbpage import page
from CoreChatbot.TheVoiceKid.database import *


import datetime
from pymongo import MongoClient
client = MongoClient('cb.saostar.vn', 27017)
db = client.Phuc
USER = db.USER
FAQ = db.FAQ
NEWS = db.NEWS


def answer(message, sender_id):
    found_question = False
    for data in FAQ.find():
        final_data = {}
        count = 0
        metadata = data['metadata']
        for word in metadata:
            if word in message.lower():
                count = count + 1
            else:
                break
        if count == len(data['metadata']):
            final_data = data
            print 'final_data la', final_data
            found_question = True
            break
        else:
            found_question = False

    if found_question:

        page.send(sender_id, final_data['answer'])
    else:
        print 'khong tim thay cau hoi trong FAQ'
        text = "Ôi, mình chưa hiểu rõ ý bạn lắm ☹. Có lẽ nội dung này đã vượt ngoài bộ nhớ của mình mất rồi 🤖🤖🤖. Bạn nhấn tính năng “Home” bên duới 👇 để xem thêm những thông tin của chương trình nha, biết đâu bạn sẽ tìm ra được câu trả lời cho thắc mắc của mình đấy! 😉"
        buttons = [
            Template.ButtonPostBack(
                "Home", "home")
        ]
        page.send(sender_id, Template.Buttons(text, buttons))

    return
