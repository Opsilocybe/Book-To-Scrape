import requests
from bs4 import BeautifulSoup
import csv
import os

def get_book_data(url: str) -> list:
    """retourne les données du livre passé en paramètre

    Args:
        url (str): url du livre

    Returns:
        list: liste contenant les données du livre
    """

    page= requests.get(url)
    soup= BeautifulSoup(page.text, "html.parser")

    product_page_url= url

    soupfind= soup.find_all("td")
    
    title= soup.find ("h1").text
    

    upc= soupfind[0].text

    price_including_tax= soupfind[2].text

    price_excluding_tax= soupfind[3].text

    number_available= soupfind[5].text 

    product_description = soup.find(id="content_inner").find_all("p")[3].text
    clean_description = product_description.replace('"', '')
   

    category= soup.find("ul", class_="breadcrumb").find_all("li")[2].text
    clean_category = category.replace('\n', '')
    

    findrating= soup.find("p", class_="instock availability")

    review_rating= findrating.find_next_sibling().get("class")[1]

    image=soup.find("img")
    base_url_image=image.get("src")
    clean_url_image = base_url_image.replace('../..', 'https://books.toscrape.com')

   

    return [
        title, upc, price_including_tax, price_excluding_tax, number_available, clean_category, review_rating, clean_description, clean_url_image
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
    allcategory = soup.select("ul.nav-list > li > ul > li") 

    for link in allcategory:
        lien = link.find('a')
        href = lien['href']
        titrecategorie = lien.get_text(strip=True)
        allurl.append(['https://books.toscrape.com/' + href, titrecategorie])
        
        
    
    return allurl


def create_csv(nom_category):

    collone= ["Title", "UPC", "Price (incl. tax)", "Price (excl. tax)", "Availability", "Category", "Review Rating", "Description", "image_url"]
   
    with open(nom_category + ".csv", "w", newline="", encoding="utf-8") as fichier:

        writer = csv.writer(fichier)
        writer.writerow(collone)


def populate_csv(all_data, nom_csv):
    with open(nom_csv, 'a', newline='',  encoding='utf-8') as new:
        writer = csv.writer(new)
        writer.writerow(all_data)


def create_folder():
    All_the_data= "Info_livre"
    dossier_images = "Info_livre/images_produits"
    dossier_csv = "Info_livre/all_the_csv"

    os.makedirs(All_the_data, exist_ok=True)  
    os.makedirs(dossier_csv, exist_ok=True)  
    os.makedirs(dossier_images, exist_ok=True)  
   

  
def dl_image(url,filename):

    response = requests.get(url)  
    if response.status_code == 200:  
        with open(filename, "wb") as file:  
            file.write(response.content)  
        
    else:
        print("Erreur lors du téléchargement :", response.status_code)

       