import requests
from bs4 import BeautifulSoup
import csv

def get_book_data(url: str) -> list:
    """retourne les données du livre passé en paramètre

    Args:
        url (str): url du livre

    Returns:
        list: liste contenant les données du livre
    """
    url= "https://books.toscrape.com/catalogue/do-androids-dream-of-electric-sheep-blade-runner-1_149/index.html"
    page= requests.get(url)
    soup= BeautifulSoup(page.text, "html.parser")

    product_page_url= url

    soupfind= soup.find_all("td")
    
    title= soup.find ("h1").text

    upc= soupfind[0].text

    price_including_tax= soupfind[2].text

    price_excluding_tax= soupfind[3].text

    number_available= soupfind[5].text

    product_description = soup.find(id="product_description") 

    if product_description is True:
        product_description = soup.find(id="product_description") 
    else: 
        next_element= product_description.find_next_sibling().text


    category= soup.find("ul", class_="breadcrumb").find_all("li")[2].text

    findrating= soup.find("p", class_="instock availability")
    review_rating= findrating.find_next_sibling().get("class")[1]

    image=soup.find("img")
    image_url=image.get("src")


    return [
        title, upc, price_including_tax, price_excluding_tax, number_available, category, review_rating, product_description, next_element, image_url
    ]

def get_category_books(base_url):
    all_urls = []  
    page_number = 1
    
    while True:
        if page_number == 1:
            url = base_url
        else:
            url = f"{base_url.replace('index.html', '')}page-{page_number}.html"

        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        books = soup.find_all("h3")
        if not books:
            break

        for book in books:
            book_link = book.a["href"]
            full_url = base_url.replace('index.html', '') + book_link
            all_urls.append(full_url) 

        page_number += 1
    
    return all_urls

def get_all_categories(url):
    url = "https://books.toscrape.com/index.html"
    allurl = []
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    ul_element = soup.find('ul', class_='nav nav-list')
    links_in_ul = ul_element.find_all('a')
    for link in links_in_ul:
        allurl.append('https://books.toscrape.com/' + link['href'])
    return allurl

def create_csv(all_data):

    with open("functions.csv", "w", newline="", encoding="utf-8") as fichier:
        
        writer = csv.writer(fichier)
        writer.writerow(["Title", "UPC", "Price (incl. tax)", "Price (excl. tax)", "Availability", "Category", "Review Rating", "Description"])
        writer.writerows(all_data)  # Écrit toutes les données dans le CSV
