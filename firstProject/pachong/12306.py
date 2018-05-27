import requests


# https://live.bilibili.com/5608176
def get_check():
    url = 'https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=2018-04-07&leftTicketDTO.from_station=WXH&leftTicketDTO.to_station=AQH&purpose_codes=ADULT'
    response = requests.get(url)

    result = response.json()

    return result['data']['result']


def make_order():
    url = "https://kyfw.12306.cn/otn/confirmPassenger/confirmSingleForQueue"
    header = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'keep-alive',
        'Content-Length': '526',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'JSESSIONID=3228A294A48D0B57DDE991F049FAE4B9; tk=g6xMHLF9St9j8pl_yXtBHmcmCcQTGR9FT-VVpGoQhg4pl1210; route=495c805987d0f5c8c84b14f60212447d; BIGipServerotn=2699297290.64545.0000; RAIL_EXPIRATION=1516132017456; RAIL_DEVICEID=El4Wk0W18znRD_oqc9ig3Q_OxYDRshMpmVB3O7Fdv1660ymVJHCR7GzCMQn6N9-m7BFoMMWItOI3aaBkNYQZ4c260CJCtCmjlTkkGpskMtXxhoZ4ei9hEVBmbqbTR4FHVKqorR_J1zk8DuComxqFO9QzjCjtrcea; BIGipServerpool_passport=200081930.50215.0000; _jc_save_showIns=true; current_captcha_type=Z; _jc_save_fromStation=%u65E0%u9521%2CWXH; _jc_save_toStation=%u5B89%u5E86%2CAQH; _jc_save_fromDate=2018-02-01; _jc_save_toDate=2018-01-13; _jc_save_wfdc_flag=dc',
        'Host': 'kyfw.12306.cn',
        'Origin': 'https://kyfw.12306.cn',
        'Referer': 'https://kyfw.12306.cn/otn/confirmPassenger/initDc',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }

    form_data = {
        'passengerTicketStr': 'O,0,1,郝强健,1,340824199305022213,13771073133,N',
        'oldPassengerStr': '郝强健,1,340824199305022213,3_',
        'randCode': '',
        'purpose_codes': '00',
        'key_check_isChange': 'CB5926D7BC7E6584E253A3D79362717B0D9ECFCF0549E71A10DDF164',
        'leftTicketStr': '1%2BfS3j%2FfR%2FVL2hMj71bkuXisBK6xsN%2BShSMPNawkmH32UwEoPL3FksBEy%2FA%3D',
        'train_location': 'H6',
        'choose_seats': '',
        'seatDetailType''': '000',
        'whatsSelect': '1',
        'roomType': '00',
        'dwAll': 'N',
        '_json_att': '',
        'REPEAT_SUBMIT_TOKEN': 'adedf75fdf1b255e4ed22bc10473a5c8'
    }

    html = requests.post(url, data=form_data, headers=header)
    print('订单成功！')
    print(html)


"""
车次 = 3
二等座 = 30
"""
car_list = []
# nu = 0
for i in get_check():
    tmp_list = i.split('|')
    # for n in tmp_list:
    # print(nu, a)
    # nu += 1
    if tmp_list[30] != '' and tmp_list[30] != '无':
        print(tmp_list[3], tmp_list[30])
        print(tmp_list)
        # make_order()
