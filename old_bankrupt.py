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
from bs4 import BeautifulSoup


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
        prslastname, prsfirstname, prsmiddlename = debtor.lower().split()
#        id = debtor.strip().lower()
        print(f'Проверка {debtors.index(debtor) + 1} из {len(debtors)} - {(debtors.index(debtor) + 1) * 100 // len(debtors)}% завершено')
        get_response(prslastname, prsfirstname, prsmiddlename)
        asleep = random.randint(2000, 5000) / 1000
        time.sleep(asleep)


data = {'name': [],
#        'debt': [],
        'procedure': [],
        'case': [],
        'link_fedresurs': [],
#        'link_kad': [],
        'inn': [],
        'snils': [],
        'address': []}


def get_response(prslastname='', prsfirstname='', prsmiddlename='', regionid = '95'):
    prslastname, prsfirstname, prsmiddlename = quote(prslastname), quote(prsfirstname), quote(prsmiddlename)
    regionid = '95'
    session = get_session()
    url = 'https://old.bankrot.fedresurs.ru/DebtorsSearch.aspx/'
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-encoding': 'gzip, deflate, br, zstd',
        'accept-language': 'ru-RU,ru;q=0.9,en-RU;q=0.8,en;q=0.7,en-US;q=0.6',
        'cache-control': 'no-cache',
        'connection': 'keep-alive',
        'cookie': '_ym_uid=1700107103592041594; _ym_d=1728816354; ASP.NET_SessionId=sljw4ny104xlpbsk54vb3wqh; _ym_isad=2; bankrotcookie=fac94585d97b923e5b4447836196b410; _ym_visorc=w; debtorsearch=typeofsearch=Persons&orgname=&orgaddress=&orgregionid=&orgogrn=&orginn=&orgokpo=&OrgCategory=' + '&prslastname=' + prslastname + '&prsfirstname=' + prsfirstname + '&prsmiddlename=' + prsmiddlename + '&prsaddress=&prsregionid=' + regionid + '&prsinn=&prsogrn=&prssnils=&PrsCategory=&pagenumber=0; qrator_msid=1728820063.842.5fEIfvU8SkJAvMc1-lscmto11bij4aoseoijabb61qkui5pr5',
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
    data = session.get(url, headers=headers)
    text = data.text

    soup = BeautifulSoup(text, 'html.parser')
    #print(soup.prettify())
    #print(tbody in soup.prettify())
    
#    print('buttons' in soup)
    #print('Чаптыков' in soup.prettify())
#    print('Чаптыков' in text)
    bank = soup.find('table', class_ = 'bank').find('tr').find_next_siblings('tr')
    for el in bank:
        #print(str(el.get_text()).replace('', '').replace('\t', '').replace('\n', ''))
        a = str(el.get_text()).replace('\t', '').replace('Физическое лицо', '').split('\r\n')
        #print(a.split('\n'), type(a))
        print(a)


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


def get_name():
    prslastname = ''
    prsfirstname = ''
    prsmiddlename = ''
    return prslastname, prsfirstname, prsmiddlename


def get_session():
    s = requests.Session()
    return s


def get_debtors():
    table = read_xls()
    debtors = list(get_column(table))
    debtors = debtors[:-1]
    return debtors


def start_time():
    start_time = datetime.now()
    return start_time


data = {'name': [],
#        'debt': [],
        'procedure': [],
        'case': [],
        'link_fedresurs': [],
#        'link_kad': [],
        'inn': [],
        'snils': [],
        'address': []}


def main():
    start = start_time()
    debtors = get_debtors()
    today_date = str(date_today())
    filename = 'bankrots_' + today_date + '.xlsx'
    check_debtors(debtors)
#    name = get_name()
#    name = 'Чаптыков', '', ''
#    prslastname, prsfirstname, prsmiddlename = name
"""    prslastname, prsfirstname, prsmiddlename = quote(prslastname), quote(prsfirstname), quote(prsmiddlename)
    regionid = '95'
    session = get_session()
    url = 'https://old.bankrot.fedresurs.ru/DebtorsSearch.aspx/'
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-encoding': 'gzip, deflate, br, zstd',
        'accept-language': 'ru-RU,ru;q=0.9,en-RU;q=0.8,en;q=0.7,en-US;q=0.6',
        'cache-control': 'no-cache',
        'connection': 'keep-alive',
        'cookie': '_ym_uid=1700107103592041594; _ym_d=1728816354; ASP.NET_SessionId=sljw4ny104xlpbsk54vb3wqh; _ym_isad=2; bankrotcookie=fac94585d97b923e5b4447836196b410; _ym_visorc=w; debtorsearch=typeofsearch=Persons&orgname=&orgaddress=&orgregionid=&orgogrn=&orginn=&orgokpo=&OrgCategory=' + '&prslastname=' + prslastname + '&prsfirstname=' + prsfirstname + '&prsmiddlename=' + prsmiddlename + '&prsaddress=&prsregionid=' + regionid + '&prsinn=&prsogrn=&prssnils=&PrsCategory=&pagenumber=0; qrator_msid=1728820063.842.5fEIfvU8SkJAvMc1-lscmto11bij4aoseoijabb61qkui5pr5',
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
    data = session.get(url, headers=headers)
    text = data.text
    #print(text)"""



"""    fiz = soup.find(string='Физическое лицо')[2].find_parent('tr')
    print(fiz)"""

    #print(bank.find_al('tr'))
    #print(rows)

    #data = s.get(url).content
    #print(data.content)
    #print()
    #print(data.text)
    #count = data.text.count(name)
    #print(count)
    #x = 1
    #text = data.text
    #while x != count:
    #    start = text.find(name)
    #   text = text[start + 1 :]
    #    x += 1
    #print(text[: 500])    

    #print(data.text)

     
    

if __name__ == "__main__":
    main()
