def del_(line: str) -> list:
    """ delete unnecessary information as \"\" and 0.0000 """
    line = line.split('\n')
    line = [data for data in line if data != '']
    line = [line[0], line[1], line[3]]
    return line


def card(data: list):
    cnt = 0
    for i in range(len(data)):
        if data[i][0] == "USD":
            cnt += 1
        if cnt == 2:
            data[i][0] += "_CARD"


def get_info(soup: "<class 'bs4.BeautifulSoup'>") -> tuple:
    """
    :param soup: input html code of UA bank.
    :return: (name_of_bank, [ [cur1, "99.9", "100.1"], ...])
    """
    try:
        title = soup.find("h1").text[13:][:-1]
        lines = soup.findAll("tr")
        cur = []
        for i in range(len(lines)):
            if lines[i] != lines[0]:
                cur.append(del_(lines[i].text))
            else:
                continue
    except TypeError:
        return None

    card(cur)

    return (title, cur)

