import requests
from bs4 import BeautifulSoup


def scrapAllTitles(url):
    alltitle = []
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    alltitles = soup.find_all('h3')
    for title in alltitles:
        alltitle.append(title.find('a').text)
    return alltitle


def getAllcategory():
    url = "https://books.toscrape.com/index.html"
    allurl = []
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    ul_element = soup.find('ul', class_='nav nav-list')
    links_in_ul = ul_element.find_all('a')
    for link in links_in_ul:
        allurl.append('https://books.toscrape.com/' + link['href'])
    return allurl


for url in getAllcategory():
    data = scrapAllTitles(url)
    print(data)


