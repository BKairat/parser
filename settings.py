from bs4 import BeautifulSoup
import requests
# import os.path
import get_info_ua, get_info_cz
import arhieve


urls = {
    "ua_urls": ["https://minfin.com.ua/company/privatbank/currency/",
            "https://minfin.com.ua/company/oschadbank/currency/",
            "https://minfin.com.ua/company/pumb/currency/",
            "https://minfin.com.ua/company/ukrgasbank/currency/",
            "https://minfin.com.ua/company/alfa-bank/currency/",
            "https://minfin.com.ua/company/otp-bank/currency/",
            "https://minfin.com.ua/company/accordbank/currency/",
            "https://minfin.com.ua/company/forward-bank/currency/",
            ],
    "cz_urls": ["https://www.kurzy.cz/kurzy-men/kurzovni-listek/ceska-sporitelna/",
                "https://www.kurzy.cz/kurzy-men/kurzovni-listek/komercni-banka/",
                "https://www.kurzy.cz/kurzy-men/kurzovni-listek/csob/",
                "https://www.kurzy.cz/kurzy-men/kurzovni-listek/air-bank/",
                "https://www.kurzy.cz/kurzy-men/kurzovni-listek/equa-bank/",
                "https://www.kurzy.cz/kurzy-men/kurzovni-listek/fio-banka/",
                "https://www.kurzy.cz/kurzy-men/kurzovni-listek/mbank/",
                "https://www.kurzy.cz/kurzy-men/kurzovni-listek/moneta-money-bank/",
                "https://www.kurzy.cz/kurzy-men/kurzovni-listek/oberbank-ag/",
                "https://www.kurzy.cz/kurzy-men/kurzovni-listek/postovni-sporitelna/",
                "https://www.kurzy.cz/kurzy-men/kurzovni-listek/raiffeisenbank/",
                "https://www.kurzy.cz/kurzy-men/kurzovni-listek/unicredit-bank/"
               ]

}

picked_countries = {}


def get_info_by_cntry(country: str, soup: "<class 'bs4.BeautifulSoup'>") -> tuple:
    if country == "ua":
        return get_info_ua.get_info(soup)
    elif country == "cz":
        return get_info_cz.get_info(soup)


def main_func(country: str) -> tuple:
    data = arhieve.Arhieve()
    try:
        if country in picked_countries:
            return (picked_countries[country], None)
        else:
            for url in urls[f"{country}_urls"]:
                request = requests.get(url)
                soup = BeautifulSoup(request.text, "html.parser")
                title_data = get_info_by_cntry(country, soup)
                if title_data is None:
                    print(f"something wrong with {url}")
                    continue
                bank = arhieve.Bank(title_data[0], title_data[1])
                data.add_new_cur(bank)
            html_string = data.data_to_html_text(country)
            text_string = data.data_to_str(country)
            return (html_string, text_string)
    except:
        return "<h1>Check your internet connection!"


