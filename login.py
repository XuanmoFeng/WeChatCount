#!/usr/bin/env python
# coding=utf-8
import sys
from wxpy import *
reload(sys)
sys.setdefaultencoding('utf8')
robot=Bot()
my_chat=robot.chats(update=True)#,contact_only=False)
my_frinds=robot.friends()
print my_frinds
my_group=robot.groups(update=True,contact_only=False)
manfriend=my_frinds.search(provice="陕西")

my_mps=robot.mps()
manfriend=my_frinds.search(sex=MALE)

womanfriend=my_frinds.search(sex=FEMALE)
girl=len(womanfriend)
boy=len(manfriend)
total=len(my_frinds)
womanfriend=my_frinds.search(sex=FEMALE)
Unkownsex=total-boy-girl
s="女生：%d个\r\n"%girl
y="男生: %d个\r\n"%boy
b="不明性别者:%d个\r\n"%Unkownsex
o="总计:%d个\r\n"%total
s=s+y+b+o

sunyongjian=my_frinds.search(u"赵亚欣")[0]
sunyongjian.send(s)
