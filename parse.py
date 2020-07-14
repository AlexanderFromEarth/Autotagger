import requests
from bs4 import BeautifulSoup


def habr_load(id):
    request = requests.get(f'https://m.habr.com/ru/post/{str(id)}/')
    # парсим мобилку потому что быстрее
    # хотя названия классов на мобилке выглядят ужасно
    soup = BeautifulSoup(request.text, 'html5lib')
    title = soup.find('h1', {'class': 'tm-article-snippet__title'})
    if not title:
        return None  # нет заголовка - нет статьи
    title = title.text
    text = soup.find('div', {'class': 'tm-article-body__content'}).text
    tags = [
        tag.text
        for tag in soup.findAll('a', 'tm-article-body__tags-item-link')
    ]
    return {'id': id, 'title': title, 'text': text, 'tags': tags}


def law_load(id):
    request = requests.get(
        f'http://xn--90afdbaav0bd1afy6eub5d.xn--p1ai/{id}/print')
    soup = BeautifulSoup(request.text, 'html5lib')
    title = soup.find('h2')
    text = soup.find('td')
    if not title or not text:
        return None
    title = title.text
    text = text.text
    return {'id': id, 'title': title, 'text': text}


def find_laws(page_num):
    request = requests.get(
        f'http://xn--90afdbaav0bd1afy6eub5d.xn--p1ai/search?page={page_num}')
    soup = BeautifulSoup(request.text, 'html5lib')
    return (law.attrs['href'][1:] for law in soup.find(id='list').findAll('a'))
