import urllib.request
from bs4 import BeautifulSoup


def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()


def parse(html):
    soup = BeautifulSoup(html)
    table = soup.find('table', class_='items_list')
    print(table.prettify())


def main():
    parse(get_html('https://www.weblancer.net/jobs/'))


if __name__ == '__main__':
    main()
