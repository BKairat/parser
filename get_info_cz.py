def get_info(soup: "<class 'bs4.BeautifulSoup'>") -> tuple:
    """
    :param soup: input html code of CZ bank.
    :return: (name_of_bank, [ [cur1, "99.9", "100.1"], ...])
    """
    try:
        bank_name = soup.find("h2").find("a").text
        lines = soup.findAll("table")[1].findAll("tr")[2:]
        data = []
        for line in lines:
            cur = line.find("td", align = "center").text
            ex_rates = line.findAll("td", align = "right")[1:3]
            data.append([cur, ex_rates[0].text, ex_rates[1].text])
    except TypeError:
        return None

    return (bank_name, data)
