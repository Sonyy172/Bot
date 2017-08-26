# -*- coding: utf-8 -*-
from ApiMessenger import Attachment, Template
from ApiMessenger.payload import QuickReply
from ApiMessenger.fbmq import Page

import CoreChatbot.Preparation.messenger
from CoreChatbot.Preparation.config import CONFIG
from CoreChatbot.Preparation.fbpage import page

import datetime
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.Phuc
users = db.user


def greeting(sender_id):
    # get user info
    user_profile = page.get_user_profile(sender_id)  # return dict
    first_name = user_profile["first_name"]
    last_name = user_profile["last_name"]
    id_user = user_profile["id"]

    space = " "
    a = "Chào"
    b = "😍. Cùng mình cập nhật những tin tức “nóng hổi” của chương trình “Giọng Hát Việt Nhí” 2017 tại chatbot này bạn nhé 😉. Ngoài ra, bạn còn có cơ hội tham gia các màn dự đoán “nẩy lửa” và nếu may mắn bạn có thể “rinh” về những phần quà vô cùng hấp dẫn nữa đấy. Giờ thì còn chần chừ gì mà không bắt đầu cuộc “trò chuyện thân mật” này nào !!!\n⏩⏩⏩ Quay về tính năng chính bằng cách ấn phím “Home” hoặc gõ vào chữ “Home” hoặc “Menu” 👇\n⏩⏩⏩ Chương trình “Giọng Hát Việt Nhí” 2017 sẽ được phát sóng vào lúc 21h10 thứ 7 hằng tuần trên kênh VTV3📺"
    a = a.decode('utf-8')
    b = b.decode('utf-8')
    seq = (a, first_name, b)
    buttons = [
        Template.ButtonPostBack(
            "Home", "home")
    ]
    page.send(sender_id, Template.Buttons(text, buttons))

    check_voter = users.find_one({'id_user': sender_id})
    if bool(check_voter):
        pass
    else:
        new_user = {
            'first_name': first_name,
            'last_name': last_name,
            'id_user': id_user,
            'HLV_da_binh_chon': '',
            'subscribe': 'no'
            # 'thoi_gian': datetime.datetime.now().strftime("%y-%m-%d-%H-%M")
        }
        users.insert_one(new_user)

    # page.send(sender_id, "da them new_user")
    return
