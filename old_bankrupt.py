import requests
from datetime import date
from datetime import datetime
import csv
import ctypes
import pprint
import json
from urllib.parse import quote
import pandas as pd
import time
import random


kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

'''
Colors!
Write a module and import in future.
'''
red_text = '\033[31m'
green_text = '\033[32m'
yellow_text = '\033[33m'
blue_text = '\033[34m'
white_text_on_blue = '\033[37m\033[44m'
marked_text = '\033[43m'
end_text = '\033[0m'
numbers = white_text_on_blue



def build_url(prsnbankruptsId, regionId='95'):
    '''Build str url for parse'''
    start_url = "https://bankrot.fedresurs.ru/backend/prsnbankrupts?searchString="
    middle_url = "&isActiveLegalCase=null&regionId=" # Это для всех дел независимо от статуса
#    middle_url = "&isActiveLegalCase=true&regionId=" # Это для активных дел
#    middle_url = "&isActiveLegalCase=false&regionId=" # Это для завершенных дел

    end_url = "&limit=15&offset=0"
    encoding_prsnbankruptsId = quote(prsnbankruptsId)
    return start_url + encoding_prsnbankruptsId + middle_url + regionId + end_url


def get_prsnbankruptsId():
    '''Get Id return Id (str)'''
    prsnbankruptsId = input('Введите ФИО или ИНН или СНИЛС ').lower().strip()
    return prsnbankruptsId


def read_xls(filename='debtors.xls'):
    '''Не читаем первую строку, т.к. в ней нет данных'''
    table = pd.read_excel(filename, skiprows=1)
    return(table)


def get_column(table):
    column = table['Unnamed: 2']
    return column


def get_debtors():
#    print()
    table = read_xls()
    debtors = list(get_column(table))
    debtors = debtors[:-1]
#    print()
#    print(debtors)
    return debtors


def check_debtors(debtors):
    for debtor in debtors:
        id = debtor.strip().lower()
#        print('id', id)
        print(f'Проверка {debtors.index(debtor) + 1} из {len(debtors)} - {(debtors.index(debtor) + 1) * 100 // len(debtors)}% завершено')
        check_person(id)
        asleep = random.randint(2000, 5000) / 1000
#        print('sleep', asleep)
        time.sleep(asleep)
        pass


def check_person(id):
    get_response(id)
    pass


data = {'name': [],
#        'debt': [],
        'procedure': [],
        'case': [],
        'link_fedresurs': [],
#        'link_kad': [],
        'inn': [],
        'snils': [],
        'address': []}


def get_response(id):
    #url = 'https://old.bankrot.fedresurs.ru/DebtorsSearch.aspx'
    url = 'https://old.bankrot.fedresurs.ru/DebtorsSearch.aspx'
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "ru-RU,ru;q=0.9,en-RU;q=0.8,en;q=0.7,en-US;q=0.6",
        "cache-control": "max-age=0",
        "Connection": "keep-alive",
        "content-length": "15395",
        "content-type": "application/x-www-form-urlencoded",
        "Cookie": "bankrotcookie=6da7022bc3261c3be0d6b7e379396e18; ASP.NET_SessionId=w40ohvvehrbeaigux0rn5lxo; _ym_uid=1727798102350149238; _ym_d=1727798102; _ym_isad=2; _ym_visorc=w; qrator_msid=1727797939.702.6Q5srhCit6Uqr8Ni-2523jnq19lmgfhsnlh8pm9grivmicptn; debtorsearch=typeofsearch=Persons&orgname=&orgaddress=&orgregionid=&orgogrn=&orginn=&orgokpo=&OrgCategory=&prslastname=%d0%a0%d0%be%d1%81%d0%bb%d1%8f%d0%ba%d0%be%d0%b2&prsfirstname=&prsmiddlename=&prsaddress=&prsregionid=95&prsinn=&prsogrn=&prssnils=&PrsCategory=&pagenumber=0",
        "set-cookie": "debtorsearch=typeofsearch=Persons&orgname=&orgaddress=&orgregionid=&orgogrn=&orginn=&orgokpo=&OrgCategory=&prslastname=&prsfirstname=&prsmiddlename=&prsaddress=&prsregionid=&prsinn=&prsogrn=&prssnils=&PrsCategory=&pagenumber=0; path=/",
        "Referer": "https://bankrot.fedresurs.ru/bankrupts?searchString=^%^D0^%^BF^%^D0^%^B8^%^D1^%^81^%^D1^%^82^%^D1^%^83^%^D0^%^BD^%^D0^%^BE^%^D0^%^B2^%^D0^%^B8^%^D1^%^87^%^20^%^D1^%^81^%^D0^%^B5^%^D1^%^80^%^D0^%^B3^%^D0^%^B5^%^D0^%^B9&regionId=95&isActiveLegalCase=true&offset=0&limit=15^",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
        "sec-ch-ua": 'Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows"
        }
    response = requests.get(url, headers=headers)
"""    response.encoding = 'utf-8'
    string = response.text
    res_dict = json.loads(string)"""
#    print('res_dict', res_dict) # Печатаем полученный словарь
"""    if res_dict['total'] > 0:
        for dict in res_dict['pageData']:
            if id == dict['fio'].lower():
                print('fio', dict['fio'])
                data['name'].append(dict['fio'])
                if 'snils' in dict:
                    print('snils', dict['snils'])
                    data['snils'].append(dict['snils'])
                else:
                    print('snils', '0')
                    data['snils'].append('0')
                print('inn', dict['inn'])
                data['inn'].append(dict['inn'])
                data['case'].append(dict['lastLegalCase']['number'])
                data['procedure'].append(dict['lastLegalCase']['status']['description'])
                data['address'].append(dict['address'])
                data['link_fedresurs'].append('https://fedresurs.ru/persons/' + dict['guid'] + ' ')
    else:
        pass
"""

def start_time():
    start_time = datetime.now()
    return start_time


def process_time(start_time):
#    start_time = time.time()
    end_time = datetime.now()  # время окончания выполнения
    execution_time = end_time - start_time  # вычисляем время выполнения
    print(green_text + "Время выполнения программы: " + str(execution_time) + " секунд" + end_text + "\n")


def date_today():
    '''Func that returned today date'''
    today = date.today()
    return today


def main():
    name = 'Барабаш'
    prslastname = ''
    prsfirstname = ''
    prsmiddlename = ''
    

    prslastname, prsfirstname, prsmiddlename = quote(input('Фамилия? ').strip()), quote(input('Имя? ').strip()), quote(input('Отчество? ').strip())
    print('prslastname', prslastname)
    print('prsfirstname', prsfirstname)
    print('prsmiddlename', prsmiddlename)

    s = requests.Session()
    url = 'https://old.bankrot.fedresurs.ru/DebtorsSearch.aspx/'
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-encoding': 'gzip, deflate, br, zstd',
        'accept-language': 'ru-RU,ru;q=0.9,en-RU;q=0.8,en;q=0.7,en-US;q=0.6',
        'cache-control': 'no-cache',
        'connection': 'keep-alive',
        'cookie': '_ym_uid=1728029516311134247; _ym_d=1728029516; ASP.NET_SessionId=0bohgc1sylhu0kmbtchgkc11; _ym_isad=2; bankrotcookie=fac94585d97b923e5b4447836196b410; _ym_visorc=w; debtorsearch=typeofsearch=Persons&orgname=&orgaddress=&orgregionid=&orgogrn=&orginn=&orgokpo=&OrgCategory=' + '&prslastname=' + prslastname + '&prsfirstname=' + prsfirstname + '&prsmiddlename=' + prsmiddlename + '&prsaddress=&prsregionid=&prsinn=&prsogrn=&prssnils=&PrsCategory=&pagenumber=0; qrator_msid=1728820063.842.5fEIfvU8SkJAvMc1-lscmto11bij4aoseoijabb61qkui5pr5',
        'host': 'old.bankrot.fedresurs.ru',
        'pragma': 'no-cache',
        'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'

    }
    cookies = {
        'ASP.NET_SessionId': 'sljw4ny104xlpbsk54vb3wqh',
        '_ym_isad': '2',
        '_ym_visorc': 'b',
        'bankrotcookie': 'fac94585d97b923e5b4447836196b410',
        'debtorsearch': '_ym_uid=1700107103592041594; _ym_d=1728816354; _ym_isad=2; _ym_visorc=w; bankrotcookie=371074958e57176c98581f5d2475c9e6; ASP.NET_SessionId=sljw4ny104xlpbsk54vb3wqh; qrator_msid=1728816196.249.8it5rT4nD2I1od7w-4jhegtgqe8dq77684peggm9ebbnqe6s1; debtorsearch=typeofsearch=Persons&orgname=&orgaddress=&orgregionid=&orgogrn=&orginn=&orgokpo=&OrgCategory=&prslastname=%d0%9f%d0%b8%d1%81%d1%82%d1%83%d0%bd%d0%be%d0%b2%d0%b8%d1%87&prsfirstname=&prsmiddlename=&prsaddress=&prsregionid=&prsinn=&prsogrn=&prssnils=&PrsCategory=&pagenumber=0',
        'qrator_msid': '1728801687.622.z0pB0Qc7dphfomI9-ka9calmjflbcalfmp9bd7i6jtng9gd82',
        '_ym_d': '1728029516',
        '_ym_uid': '1728029516311134247'
    }


    data = s.get(url, headers=headers)
    #data = s.get(url).content
    print(data.content)
    print()
    print(data.text)
    count = data.text.count(name)
    print(count)
    x = 1
    text = data.text
    while x != count:
        start = text.find(name)
        text = text[start + 1 :]
        x += 1
    print(text[: 500])    

    #print(data.text)

     
    

if __name__ == "__main__":
    main()
