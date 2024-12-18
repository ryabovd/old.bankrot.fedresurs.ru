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


def read_xls(filename='debtors.xls'):
    '''Не читаем первую строку, т.к. в ней нет данных'''
    table = pd.read_excel(filename, skiprows=1)
    return(table)


def get_column(table):
    column = table['Unnamed: 2']
    return column


def get_debtors():
    table = read_xls()
    debtors = list(get_column(table))
    debtors = debtors[:-1]
    return debtors


def check_debtors(debtors):
    for debtor in debtors:
        prslastname, prsfirstname, prsmiddlename = debtor.lower().split()
        print(f'Проверка {debtors.index(debtor) + 1} из {len(debtors)} - {(debtors.index(debtor) + 1) * 100 // len(debtors)}% завершено')
        get_response(prslastname, prsfirstname, prsmiddlename)
        asleep = random.randint(2000, 5000) / 1000
        time.sleep(asleep)


data = {
    'name': [],
    'inn': [],
    'snils': [],
    'address': [],
    'link_old_fedresurs': []
    }
#        'debt': [],
#        'procedure': [],
#        'case': [],
#        'link_fedresurs': [],
#        'link_kad': [],


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
    bank = soup.find('table', class_ = 'bank').find('tr').find_next_siblings('tr')
    for el in bank:
        prsn_data_list_dirty = str(el.get_text()).replace('\t', '').replace('Физическое лицо', '').split('\r\n')
        #print(prsn_data)
        #print(type(prsn_data))
        prsn_data_list = clean_prsn_data(prsn_data_list_dirty)
        person_old_link_end = get_person_old_link(soup)
        #print(prsn_data_list)
        #print(person_link_end)
        person_old_link = build_person_old_link(person_old_link_end)
        #print(person_link)
        prsn_name, prsn_inn, prsn_snils, prsn_region, prsn_adress = parse_person_data(prsn_data_list)
        print(prsn_name, prsn_inn, prsn_snils, prsn_region, prsn_adress, person_old_link, sep='\n')
        get_debtor_old_card(person_old_link)


def get_debtor_old_card(person_old_link):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-encoding': 'gzip, deflate, br, zstd',
        'accept-language': 'ru-RU,ru;q=0.9,en-RU;q=0.8,en;q=0.7,en-US;q=0.6',
        'cache-control': 'max-age=0',
        'connection': 'keep-alive',
        'cookie': '_ym_uid=1728029516311134247; _ym_d=1728029516; ASP.NET_SessionId=0bohgc1sylhu0kmbtchgkc11; debtorsearch=typeofsearch=Persons&orgname=&orgaddress=&orgregionid=&orgogrn=&orginn=1922547928&orgokpo=&OrgCategory=&prslastname=&prsfirstname=&prsmiddlename=&prsaddress=&prsregionid=&prsinn=&prsogrn=&prssnils=19225479288&PrsCategory=&pagenumber=0; _ym_isad=2; bankrotcookie=c98aae444770b29b2e0d2443407caf61; _ym_visorc=b; qrator_msid=1729866689.333.Ji8tvRKDjgadFiNb-ablknlgh28g2kh3rnbq6ifakmlou2kob',
        'host': 'old.bankrot.fedresurs.ru',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
    }
    response = requests.get(person_old_link, headers=headers)
    web_card = response.text
    #print(web_card)
    soup = BeautifulSoup(web_card, 'html.parser')
    prsn_lastName = soup.find('span', id = 'ctl00_cphBody_lblLastName').text
#    print('prsn_lastName', prsn_lastName)
    prsn_firstName = soup.find('span', id = 'ctl00_cphBody_lblFirstName').text
#    print('prsn_firstName', prsn_firstName)
    prsn_middleName = soup.find('span', id = 'ctl00_cphBody_lblMiddleName').text
#    print('prsn_middleName', prsn_middleName)
    prsn_birthdate = soup.find('span', id = 'ctl00_cphBody_lblBirthdate').text
#    print('prsn_birthdate', prsn_birthdate)
    prsn_birthplace = soup.find('span', id = 'ctl00_cphBody_lblBirthplace').text
#    print('prsn_birthplace', prsn_birthplace)
    prsn_caseRegion =  soup.find('span', id = 'ctl00_cphBody_lblRegion').text
#    print('prsn_caseRegion', prsn_caseRegion)
    prsn_inn = soup.find('span', id = 'ctl00_cphBody_lblINN').text
#    print('prsn_inn', prsn_inn)
    prsn_snils = soup.find('span', id = 'ctl00_cphBody_lblSNILS').text
#    print('prsn_snils', prsn_snils)
    prsn_address = soup.find('span', id = 'ctl00_cphBody_lblAddress').text
#    print('prsn_address', prsn_address)
    prsn_fio = get_fio(prsn_lastName, prsn_firstName, prsn_middleName)
#    print('fio', prsn_fio)
    out_card = prsn_fio, person_old_link, prsn_inn, prsn_snils, prsn_address
    fill_out_card(prsn_fio, person_old_link, prsn_inn, prsn_snils, prsn_address)


def get_fio(prsn_lastName, prsn_firstName, prsn_middleName):
    fio = prsn_lastName + ' ' + prsn_firstName + ' ' + prsn_middleName
    return fio


def fill_out_card(prsn_fio, person_old_link, prsn_inn, prsn_snils, prsn_address):
    data['name'].append(prsn_fio)
    data['snils'].append(prsn_snils)
    data['inn'].append(prsn_inn)
    data['address'].append(prsn_address)
    data['link_old_fedresurs'].append(person_old_link)
    #print('fill', data)


def get_person_old_link(soup):
    link = soup.find('table', class_ = 'bank').find('a')
    person_link = link.get(('href'))
    return(person_link)


def build_person_old_link(person_old_link_end):
    person_old_link_start = 'https://old.bankrot.fedresurs.ru'
    person_old_link = person_old_link_start + person_old_link_end
    return person_old_link


def clean_prsn_data(prsn_data_list):
    clean_prsn_data_list = [i.strip() for i in prsn_data_list if i.strip()]
    return clean_prsn_data_list


def parse_person_data(prsn_data_list):
    prsn_name, prsn_inn, prsn_snils, prsn_region, prsn_adress = prsn_data_list
    return prsn_name, prsn_inn, prsn_snils, prsn_region, prsn_adress


def start_time():
    start_time = datetime.now()
    return start_time


def process_time(start_time):
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


def main():
    start = start_time()
    debtors = get_debtors()
    today_date = str(date_today())
    check_debtors(debtors)
#    print('data', data)
    df = pd.DataFrame(data)
    filename = 'bankrots_' + today_date + '.xlsx'
    df.to_excel(filename, index=False)
    print(red_text + "Файл данных ЗАПИСАН" + end_text + "\n")
    process_time(start)

    
    

if __name__ == "__main__":
    main()
