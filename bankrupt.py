import requests


def main():
    url = "https://bankrot.fedresurs.ru/backend/prsnbankrupts?searchString=%D0%91%D0%B0%D0%B1%D0%BA%D0%B8%D0%BD%D0%B0%20%D0%9B%D0%B0%D1%80%D0%B8%D1%81%D0%B0%20%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%BD%D0%B0&isActiveLegalCase=true&regionId=95&limit=15&offset=0"
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


if __name__ == "__main__":
    main()