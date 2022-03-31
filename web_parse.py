import requests
from bs4 import BeautifulSoup

def web_parse(art):
    url = "https://www.wildberries.ru/catalog/{}/detail.aspx".format(art)

    # Проверка связи с сайтом
    try:
        response = requests.get(url)
    except:
        print('No internet connection')
        return '-'
    soup = BeautifulSoup(response.text, 'lxml')

    # Проверка вебсайта на наличие ключевых слов
    text = soup.get_text().split()
    try:
        ind1 = text.index('Состав')
        ind2 = text.index('Описание')
    except:
        return '-'

    consist = []
    for i in range(ind1+1, ind2, 1):
        consist.append(text[i])
    return ' '.join(consist)
