import eel
import settings


eel.init("web")

@eel.expose
def get_inform(country):
    html_text = settings.main_func(country)
    if html_text[1] != None:
        file = open(f"data/{country}.txt", "w")
        file.write(html_text[1])
        file.close()
    return html_text[0]


eel.start("main.html", size = (400, 800))