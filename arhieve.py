def data_into_dict(data: list) -> dict:
    """
    :param data: [ [cur1, "99.9", "100.1"], ...]
    :return: { cur1: (99.9, 100.1), ...}
    """
    data_D = {}
    for i in data:
        try:
            data_D[i[0]] = (float(i[1]), float(i[2]))
        except ValueError:
            continue
    return data_D


class Bank(object):
    def __init__(self, title: str, data: list):
        self.title = title
        self.data = data_into_dict(data)

    def get_all_cur(self) -> list:
        """returns available currencies"""
        return [i for i in self.data.keys()]

    def get_rate(self, cur: str) -> tuple:
        """returns exchange rates"""
        if cur not in self.data:
            print("There is no such currency in this bank. There are only", self.data.keys())
            return None
        return self.data[cur]

class Arhieve(object):
    def __init__(self):
        self.data = {}

    def add_new_cur(self, bank):
        new_cur = bank.data
        title = bank.title
        for i in new_cur:
            if i not in self.data:
                self.data[i] = [(title, new_cur[i][0]), (title, new_cur[i][1])]
                continue
            if new_cur[i][0] > self.data[i][0][1]:
                self.data[i][0] = (title, new_cur[i][0])
            if new_cur[i][1] < self.data[i][1][1]:
                self.data[i][1] = (title, new_cur[i][1])


    def data_to_str(self, state: str) -> str:
        ret_str = f"  BEST EXCHANGE RATES IN {state.upper()}\n"
        for cur in self.data:
            ret_str += f"    {cur}: \nsell in {self.data[cur][0][0]} {self.data[cur][0][1]}\nbuy in {self.data[cur][1][0]} {self.data[cur][1][1]}\n"
        return ret_str

    def data_to_html_text(self, state: str) -> str:
        ret_html = f"<h1>BEST EXCHANGE RATES IN {state.upper()}</h1>"
        for cur in self.data:
            ret_html += f"<h2>{cur}:</h2>\
                 <p>sell in {self.data[cur][0][0]} {self.data[cur][0][1]}\
                 buy in {self.data[cur][1][0]} {self.data[cur][1][1]}</p>"
        return ret_html

