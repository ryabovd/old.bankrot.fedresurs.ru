import requests
from datetime import date
import csv
import ctypes
import pprint
import json


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
    middle_url = "&isActiveLegalCase=true&regionId="
    end_url = "&limit=15&offset=0"
    return start_url + prsnbankruptsId + middle_url + regionId + end_url


def get_prsnbankruptsId():
    '''Get Id return Id (str)'''
    prsnbankruptsId = input('Введите ФИО или ИНН или СНИЛС ')
    return prsnbankruptsId


def main():
    prsnbankruptsId = get_prsnbankruptsId()
    print(prsnbankruptsId, type(prsnbankruptsId))
    #url = build_url(prsnbankruptsId)
    #"https://bankrot.fedresurs.ru/backend/prsnbankrupts?searchString=Романов&isActiveLegalCase=true&regionId=95&limit=15&offset=0"
    #headers = {
    #    "Accept": "application/json, text/plain, */*",
    #    "Accept-Language": "ru-RU,ru;q=0.9,en-RU;q=0.8,en;q=0.7,en-US;q=0.6",
    #    "Connection": "keep-alive",
    #    "Cookie": "_ym_uid=1700107103592041594; _ym_d=1716266926; qrator_msid=1723728014.226.j2YTgLfBJOAmPXHf-0tqah7dmflbeihg9s4gcea2gn707dkbq; _ym_isad=2; _ym_visorc=w",
    #    "Referer": "https://bankrot.fedresurs.ru/bankrupts?searchString=^%^D0^%^BF^%^D0^%^B8^%^D1^%^81^%^D1^%^82^%^D1^%^83^%^D0^%^BD^%^D0^%^BE^%^D0^%^B2^%^D0^%^B8^%^D1^%^87^%^20^%^D1^%^81^%^D0^%^B5^%^D1^%^80^%^D0^%^B3^%^D0^%^B5^%^D0^%^B9&regionId=95&isActiveLegalCase=true&offset=0&limit=15^",
    #    "Sec-Fetch-Dest": "empty",
    #    "Sec-Fetch-Mode": "cors",
    #    "Sec-Fetch-Site": "same-origin",
    #    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    #    "sec-ch-ua": 'Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127',
    #    "sec-ch-ua-mobile": "?0",
    #    "sec-ch-ua-platform": "Windows"
    #    }
    #response = requests.get(url, headers=headers)
    #print(response.encoding)
    #response.encoding = 'utf-8'
    #string = response.text
    #res_dict = json.loads(string)
    #print(type(res_dict))
    #print(response.headers)
    string = str_resp_7
    #print(type(string))
    #print(string)
    res_dict = json.loads(string)
    #print(type(res_dict))
    #print(res_dict)
    #print(res_dict.keys())
    #print(res_dict['pageData'])
    #print(type(res_dict['pageData']))
    #print(len(res_dict['pageData']))
    #print(type(res_dict['pageData'][0]))
    for dict in res_dict['pageData']:
        if prsnbankruptsId in dict.values():
            print('fio', dict['fio'])
            print('snils', dict['snils'])
            print('inn', dict['inn'])
    


def date_today():
    '''Func that returned today date'''
    today = date.today()
    return str(today)


def make_full_report(data): 
    '''Get data (? list) and return report (? list)'''
    
    
def make_main_report(data):
    '''get data (? list) and return (? list)'''
    pass

def read_file(file_name):
    pass

def write_file(file_name):
    pass


def base_file_write(base_file, data):
    with open(file=base_file, mode="a", encoding="UTF-8", newline='') as base:
        writer = csv.writer(base, delimiter=';')
        writer.writerow(data)
        print(green_text + "Внесена запись" + end_text)
        print(data)


def write_change_base_file(base_file, base_list):
    '''Func recieved name base file and new base list. 
    Then write base file from list.'''
    with open(file=base_file, mode="w", encoding="UTF-8", newline='') as base:
        writer = csv.writer(base, delimiter=';')
        for line in base_list:
            writer.writerow(line)
    print(red_text + "Файл базы данных ЗАПИСАН" + end_text + "\n")


str_resp = '{"pageData":[{"snils":"10749272160","category":"Физическое лицо","region":"Республика Хакасия","arbitrManagerFio":"КРУГЛОВ ГЕОРГИЙ КОНСТАНТИНОВИЧ","address":"Республика Хакасия, Боградский район, с. Первомайское, ул. Кирова, д. 5, кв. 3","lastLegalCase":{"number":"А74-8815/2023","status":{"code":"CitizenAssetsDisposal","description":"Реализация имущества гражданина"}},"guid":"0677d445-f2e1-47a8-9230-302973cf3368","fio":"Пистунович Сергей Анатольевич","inn":"190111676789"}],"total":1}'
str_resp_7 = '{"pageData":[{"snils":"14397220165","category":"Физическое лицо","region":"Республика Хакасия","arbitrManagerFio":"Малюка Анна Алексеевна","address":"655602, Республика Хакасия, г. Саяногорск, мкр. Центральный, д. 34, кв. 11","lastLegalCase":{"number":"А74-3211/2024","status":{"code":"CitizenDebtRestructuring","description":"Реструктуризация долгов гражданина"}},"guid":"2a264a9a-1db2-11ef-a609-00620be2fa80","fio":"Горошко Светлана Андреевна","inn":"242000604230"},{"snils":"06414866972","category":"Физическое лицо","region":"Республика Хакасия","arbitrManagerFio":"Михайлова Наталья Александровна","address":"РХ, г. Саяногорск, рп. Майна, ул. Рабовича, д. 14Б","lastLegalCase":{"number":"А74-2672/2024","status":{"code":"CitizenAssetsDisposal","description":"Реализация имущества гражданина"}},"guid":"5d6a6e58-38fc-11ef-b2c8-00620be2fa80","fio":"Иванова Евгения Алексеевна","inn":"190200302922"},{"snils":"17416655279","category":"Физическое лицо","region":"Республика Хакасия","arbitrManagerFio":"Пискунова Ольга Александровна","address":"Республика Хакасия, г. Абакан, ул. Семнадцатая, д. 7","lastLegalCase":{"number":"А74-5511/2024","status":{"code":"CitizenAssetsDisposal","description":"Реализация имущества гражданина"}},"guid":"e8f9516a-545d-11ef-b1c1-00620be2fa80","fio":"Иванова Ксения Валерьевна","inn":"190119272940"},{"snils":"12497895514","category":"Физическое лицо","region":"Республика Хакасия","arbitrManagerFio":"Беспалова Светлана Николаевна","address":"Республика Хакасия, Усть-Абаканский район, аал Чарков, ул. Степная, д. 8, кв. 1","lastLegalCase":{"number":"А74-1252/2024","status":{"code":"CitizenDebtRestructuring","description":"Реструктуризация долгов гражданина"}},"guid":"d56d6548-01ea-11ef-986b-00620be2fa80","fio":"Иванова Мария Андреевна","inn":"245506290181"},{"snils":"17298472416","category":"Физическое лицо","region":"Республика Хакасия","arbitrManagerFio":"Часовской Николай Сергеевич","address":"655111, Республика Хакасия, г. Сорск, ул. Геологов, д.1, кв. 1","lastLegalCase":{"number":"А74-3690/2024","status":{"code":"CitizenAssetsDisposal","description":"Реализация имущества гражданина"}},"guid":"6e99662c-353f-11ef-8582-00620be2fa80","fio":"Иванова Надежда Александровна","inn":"190309950030"},{"snils":"13771787700","category":"Физическое лицо","region":"Республика Хакасия","arbitrManagerFio":"Новикова Вера Александровна","address":"Хакасия Респ, Черногорск г, Кирова 1-я линия ул, д. 15А","lastLegalCase":{"number":"А74-736/2024","status":{"code":"CitizenDebtRestructuring","description":"Реструктуризация долгов гражданина"}},"guid":"62fa1b06-e5e7-11ee-b5d7-00620be2fa80","fio":"Марьясова Ксения Александровна","inn":"170103764284"},{"snils":"10619085237","category":"Физическое лицо","region":"Республика Хакасия","arbitrManagerFio":"Тюриков Денис Юрьевич","address":"655603, Республика Хакасия, г. Саяногорск, мкр. Южный, д. 7, кв. 24","lastLegalCase":{"number":"А74-2152/2022","status":{"code":"CitizenAssetsDisposal","description":"Реализация имущества гражданина"}},"guid":"068230b4-c17a-4637-9832-55d61ff5b377","fio":"Трубникова Ольга Константиновна","inn":"190205855127"}],"total":7}'

'''{"pageData": [{"snils": "14397220165", "category": "Физическое лицо", "region": "Республика Хакасия", "arbitrManagerFio": "Малюка Анна Алексеевна", "address": "655602, Республика Хакасия, г. Саяногорск, мкр. Центральный, д. 34, кв. 11", "lastLegalCase": {"number": "А74-3211/2024", "status": {"code": "CitizenDebtRestructuring", "description": "Реструктуризация долгов гражданина"}}, "guid": "2a264a9a-1db2-11ef-a609-00620be2fa80", "fio": "Горошко Светлана Андреевна", "inn": "242000604230"}, {"snils": "06414866972", "category": "Физическое лицо", "region": "Республика Хакасия", "arbitrManagerFio": "Михайлова Наталья Александровна", "address": "РХ, г. Саяногорск, рп. Майна, ул. Рабовича, д. 14Б", "lastLegalCase": {"number": "А74-2672/2024", "status": {"code": "CitizenAssetsDisposal", "description": "Реализация имущества гражданина"}}, "guid": "5d6a6e58-38fc-11ef-b2c8-00620be2fa80", "fio": "Иванова Евгения Алексеевна", "inn": "190200302922"}, {"snils": "17416655279", "category": "Физическое лицо", "region": "Республика Хакасия", "arbitrManagerFio": "Пискунова Ольга Александровна", "address": "Республика Хакасия, г. Абакан, ул. Семнадцатая, д. 7", "lastLegalCase": {"number": "А74-5511/2024", "status": {"code": "CitizenAssetsDisposal", "description": "Реализация имущества гражданина"}}, "guid": "e8f9516a-545d-11ef-b1c1-00620be2fa80", "fio": "Иванова Ксения Валерьевна", "inn": "190119272940"}, {"snils": "12497895514", "category": "Физическое лицо", "region": "Республика Хакасия", "arbitrManagerFio": "Беспалова Светлана Николаевна", "address": "Республика Хакасия, Усть-Абаканский район, аал Чарков, ул. Степная, д. 8, кв. 1", "lastLegalCase": {"number": "А74-1252/2024", "status": {"code": "CitizenDebtRestructuring", "description": "Реструктуризация долгов гражданина"}}, "guid": "d56d6548-01ea-11ef-986b-00620be2fa80", "fio": "Иванова Мария Андреевна", "inn": "245506290181"}, {"snils": "17298472416", "category": "Физическое лицо", "region": "Республика Хакасия", "arbitrManagerFio": "Часовской Николай Сергеевич", 
"address": "655111, Республика Хакасия, г. Сорск, ул. Геологов, д.1, кв. 1", "lastLegalCase": {"number": "А74-3690/2024", "status": {"code": "CitizenAssetsDisposal", "description": "Реализация имущества гражданина"}}, "guid": "6e99662c-353f-11ef-8582-00620be2fa80", "fio": "Иванова Надежда Александровна", "inn": "190309950030"}, {"snils": "13771787700", "category": "Физическое лицо", "region": "Республика Хакасия", "arbitrManagerFio": "Новикова Вера Александровна", "address": "Хакасия Респ, Черногорск г, Кирова 1-я линия ул, д. 15А", "lastLegalCase": {"number": "А74-736/2024", "status": {"code": "CitizenDebtRestructuring", "description": "Реструктуризация долгов гражданина"}}, "guid": "62fa1b06-e5e7-11ee-b5d7-00620be2fa80", "fio": 
"Марьясова Ксения Александровна", "inn": "170103764284"}, {"snils": "10619085237", "category": "Физическое лицо", "region": "Республика Хакасия", "arbitrManagerFio": "Тюриков Денис Юрьевич", "address": "655603, Республика Хакасия, г. Саяногорск, мкр. Южный, д. 7, кв. 24", "lastLegalCase": {"number": "А74-2152/2022", "status": {"code": "CitizenAssetsDisposal", "description": "Реализация имущества гражданина"}}, "guid": "068230b4-c17a-4637-9832-55d61ff5b377", "fio": "Трубникова Ольга Константиновна", "inn": "190205855127"}], "total": 7}'
'''

'''
Structure of response
{"pageData":
    [
0        {
            "snils":"10749272160",
            "category":"Физическое лицо",
            "region":"Республика Хакасия",
            "arbitrManagerFio":"КРУГЛОВ ГЕОРГИЙ КОНСТАНТИНОВИЧ",
            "address":"Республика Хакасия, Боградский район, с. Первомайское, ул. Кирова, д. 5, кв. 3",
            "lastLegalCase":
                {
                "number":"А74-8815/2023",
                "status":
                    {
                    "code":"CitizenAssetsDisposal",
                    "description":"Реализация имущества гражданина"
                    }
                },
            "guid":"0677d445-f2e1-47a8-9230-302973cf3368",
            "fio":"Пистунович Сергей Анатольевич",
            "inn":"190111676789"
        }
    ],
    "total":1
}

Dictionary dict_keys include keys:
    'pageData': value list from dictionaries (dictionaries) with data
    'total': value - total of dictionaries))

    
'''

'''
func for read data file(? csv)
func for clean data 
func for create data list for check
func for check person
func for make full report
func for make main report

'''
    

    

if __name__ == "__main__":
    main()