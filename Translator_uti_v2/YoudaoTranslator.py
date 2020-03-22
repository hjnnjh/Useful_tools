#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-03-16 22:16
# @Author  : Jinnan Huang
# @Site    : 
# @File    : YoudaoTranslator.py
# @Software: PyCharm

"""
英文文本分句初步解决了，舒服了。
"""

import hashlib
import random
import time
import urllib.request as requests
import json
import urllib.parse
import re

"""
向有道翻译发送data，得到翻译结果
"""

class Youdao():
    def __init__(self, msg):
        self.msg = msg
        self.url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        self.D = "Nw(nmmbP%A-r6U3EUn]Aj"
        self.salt = self.get_salt()
        self.sign = self.get_sign()
        self.ts = self.get_ts()

    def get_md(self, value):
        # md5加密
        m = hashlib.md5()
        # m.update(value)
        m.update(value.encode('utf-8'))
        return m.hexdigest()

    def get_salt(self):
        # 根据当前时间戳获取salt参数
        s = int(time.time() * 1000) + random.randint(0, 10)
        return str(s)

    def get_sign(self):
        # 使用md5函数和其他参数，得到sign参数
        s = "fanyideskweb" + self.msg + self.salt + self.D
        return self.get_md(s)

    def get_ts(self):
        # 根据当前时间戳获取ts参数
        s = int(time.time() * 1000)
        return str(s)

    def get_result(self):
        Form_Data = {
            'i': self.msg,
            'type': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': self.salt,
            'sign': self.sign,
            'ts': self.ts,
            'bv': 'c6b8c998b2cbaa29bd94afc223bc106c',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'ue': 'UTF-8',
            'typoResult': 'true',
            'action': 'FY_BY_CLICKBUTTION'

        }
        Form_Data = urllib.parse.urlencode(Form_Data).encode('utf-8')

        headers = {
            # 'Accept': 'application/json, text/javascript, */*; q=0.01',
            # 'Accept-Encoding': 'gzip, deflate',
            # 'Accept-Language': 'zh-CN,zh;q=0.9,mt;q=0.8',
            # 'Connection': 'keep-alive',
            # 'Content-Length': '240',
            # 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': 'OUTFOX_SEARCH_USER_ID=-2022895048@10.168.8.76;',
            # 'Host': 'fanyi.youdao.com',
            # 'Origin': 'http://fanyi.youdao.com',
            'Referer': 'http://fanyi.youdao.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; rv:51.0) Gecko/20100101 Firefox/51.0',
            # 'X-Requested-With': 'XMLHttpRequest'
        }
        req = requests.Request(self.url, Form_Data, headers, method='POST')
        response = requests.urlopen(req)

        html = response.read().decode('utf-8')
        translate_results = json.loads(html)
        # 找到翻译结果
        if 'translateResult' in translate_results:
            translate_results = translate_results['translateResult'][0][0]['tgt']
            # print("翻译的结果是：%s" % translate_results)
            return translate_results
        else:
            # print(translate_results)
            return translate_results

class Youdao_translator():
    """
    翻译之前处理文本
    """
    def __init__(self, rawtext):
        self.rawtext = rawtext

    def splittext(self):
        # 英文分句，主要思想为.后面必须是大写字母
        text_split = re.split(r'([.?!;]+[\s]*)([A-Z])', self.rawtext)
        final_text = []
        for i in range(len(text_split)):
            if re.match(r'^[A-Z]$', text_split[i]) != None:
                text_split[i+1] = text_split[i] + text_split[i+1]
            if re.match(r'[.?!;]+[\s]*', text_split[i]) != None:
                text_split[i-1] = text_split[i-1] + text_split[i]
        for sentence in text_split:
            if (re.match(r'^[A-Z]$', sentence) == None) and (re.match(r'[.?!;]+[\s]*', sentence) == None):
                final_text.append(sentence)
        return final_text

    def Yd_translate(self):
        text_split_list = self.splittext()
        result_list = []
        for text in text_split_list:
            # 去掉可能的无字符的元素
            if re.match('.+', text) != None:
                translator = Youdao(text)
                result = translator.get_result()
            # 去掉翻译报错的文本
            if type(result) == str:
                result_list.append(result)
        final_result = "".join(result_list)
        return final_result

if __name__ == "__main__":
    # y = Youdao('P,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.')
    # y.get_result()
    # y = youdao_split_text("this is an apple; that is a tree. ,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.?")
    # y.splittext_translate()
    # tran = Youdao_translator("P,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.")
    tran = Youdao_translator("The process of consensus requires opinion exchange and communication between experts and a moderator, and needs a balance of interests of both sides. From the viewpoint of a moderator, he/she hopes to achieve the highest level of consensus while paying the minimum total cost (Ben-Arieh & Easton, 2007; Ben-Arieh et al., 2009; Liu et al., 2012; Zhang et al., 2011). From each expert’s perspective, he/she expects to gain the maximum compensation for his/her changing opinions (Gong, Xu, Lu, Li, & Xu, 2015; Gong, Xu, Zhang, et al., 2015; Gong, Zhang et al., 2015; Zhang, Gong, & Chiclana, 2017). Mathematically, these two goals are dual to each other. Let yi, i ∈ M, denotes the unit return that expert ei expect to be compensated. In Gong, Xu, Lu, et al. (2015), Gong, Xu, Zhang, et al. (2015), Gong, Zhang et al. (2015), and Zhang et al. (2017), the authors proposed several group decision consensus on minimum cost models and maximum return models based on linear programming from the viewpoints of moderators and individual experts. Two consensus models were constructed as follows (Gong, Xu, Zhang, et al., 2015; Gong, Zhang et al., 2015):")
    print(tran.Yd_translate())