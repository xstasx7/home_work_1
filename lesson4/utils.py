from requests import utils, get

URL = utils.get_unicode_from_response(get("http://www.cbr.ru/scripts/XML_daily.asp"))


def currency_rates(val):
    """
    Принимает в качестве аргумента код валюты и
    возвращает курс этой валюты по отношению к рублю.
    :param val currency code
    :return:float(str)
    """
    attribute = URL.split('<Valute ID=')
    for i in attribute:
        if val.upper() in i:
            print(val.upper(), end=": ")
            return float(i.replace("/", "").split("<Value>")[-2].replace(",", "."))

