#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2018/5/3
# @Outhor :sixgod
# http://qwd.jd.com/fcgi-bin/qwd_searchitem_ex?skuid=26878432382%7C1658610413%7C26222795271%7C25168000024%7C11731514723%7C26348513019%7C20000220615%7C4813030%7C25965247088%7C5327182%7C19588651151%7C1780924%7C15495544751%7C10114188069%7C27036535156%7C10123099847%7C26016197600%7C10503200866%7C16675691362%7C15904713681
# \"skuid\":\"(\d+)\",\s\"\S+\s\"skuurl\":\"(\S+)\"

import re

import os
from pip._vendor import requests

url = "http://qwd.jd.com/fcgi-bin/qwd_searchitem_ex?skuid=26878432382%7C1658610413%7C26222795271%7C25168000024%7C11731514723%7C26348513019%7C20000220615%7C4813030%7C25965247088%7C5327182%7C19588651151%7C1780924%7C15495544751%7C10114188069%7C27036535156%7C10123099847%7C26016197600%7C10503200866%7C16675691362%7C15904713681"

session = requests.session()
r = session.get(url)
html = r.text
print(html)


reg = re.compile(r"\"skuid\":\"(\d+)\",\s+\S+\s+\"skuurl\":\"\S+\s+\"skuimgurl\":\"(\S+)\"")
result = reg.findall(html)
print(result)

import codecs

regUpstream = re.compile(r"(upstream\s+(\S+)\s+{[^}]+})")

with codecs.open("a.conf") as f:
    textlist = regUpstream.findall(f.read())


    if not os.path.exists("upstream"):
        os.mkdir("upstream")
    os.chdir("upstream")

    for i in textlist:
        with codecs.open(i[1],"w") as fw:
            fw.write(i[0])
    os.chdir("..")

regLocation = re.compile(r"(location\s+/(\S+)/\s+{[^}]+})")

with codecs.open("a.conf") as f2:
    textlist2 = regLocation.findall(f2.read())

    if not os.path.exists("location"):
        os.mkdir("location")
    os.chdir("location")

    for i2 in textlist2:
        file = i2[1] + ".location.conf"
        with codecs.open(file,"w") as f2w:
            f2w.write(i2[0])

    os.chdir("..")