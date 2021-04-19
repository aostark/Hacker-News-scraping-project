import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, "html.parser")
links = (soup.select('.storylink'))
subtext = soup.select('.subtext')


def sort_stories_by_votes(hn_list):
    return sorted(hn_list, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for index, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[index].select('.score')
        if len(vote):
            high_votes = int(vote[0].getText().replace(' points', ''))
            if high_votes > 99:
                hn.append({'title': title, 'link': href, 'votes': high_votes})
    return sort_stories_by_votes(hn)


print(create_custom_hn(links, subtext))
