import requests


def build_url(prsnbankruptsId, regionId='95'):
    '''Build str url for parse'''
    start_url = "https://bankrot.fedresurs.ru/backend/prsnbankrupts?searchString="
    middle_url = "&isActiveLegalCase=true&regionId="
    end_url = "&limit=15&offset=0"
    return start_url + prsnbankruptsId + middle_url + regionId + end_url

def main():
    prsnbankruptsId = input('Введите ФИО или ИНН или СНИЛС ')
    url = build_url(prsnbankruptsId)
    "https://bankrot.fedresurs.ru/backend/prsnbankrupts?searchString=Романов&isActiveLegalCase=true&regionId=95&limit=15&offset=0"
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "ru-RU,ru;q=0.9,en-RU;q=0.8,en;q=0.7,en-US;q=0.6",
        "Connection": "keep-alive",
        "Cookie": "_ym_uid=1700107103592041594; _ym_d=1716266926; qrator_msid=1723728014.226.j2YTgLfBJOAmPXHf-0tqah7dmflbeihg9s4gcea2gn707dkbq; _ym_isad=2; _ym_visorc=w",
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
    print(response.encoding)
    response.encoding = 'utf-8'
    print(response.text)
    print(response.headers)

def func(): 
    '''Get str in russian and codinng in str in url'''
    

    

if __name__ == "__main__":
    main()