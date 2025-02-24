import os
import requests
from bs4 import BeautifulSoup

base_url = "https://books.toscrape.com/catalogue/page-{}.html"
dossier_images = "images_produits"
os.makedirs(dossier_images, exist_ok=True)

page_number = 1

while True:
    response = requests.get(base_url.format(page_number))
    soup = BeautifulSoup(response.content, 'html.parser')
    product_links = soup.find_all("h3")
    if not product_links: continue

    for link in product_links:
        product_url = "https://books.toscrape.com/catalogue/" + link.a["href"].lstrip("./")
        product_response = requests.get(product_url)
        product_soup = BeautifulSoup(product_response.content, 'html.parser')
        
        
        book_title = product_soup.find("h1").text.strip().replace("/", "-") 
        img_tag = product_soup.find("img")
        if img_tag:
            img_url = "https://books.toscrape.com/" + img_tag["src"].lstrip("./")
            img_path = os.path.join(dossier_images, f"{book_title}.jpg")

            with open(img_path, "wb") as img_file:
                img_file.write(requests.get(img_url).content)
    page_number += 1









# url = "https://books.toscrape.com/index.html"
# dossier_images = "images_site"

# if not os.path.exists(dossier_images):
#     os.makedirs(dossier_images)

# response = requests.get(url)
# soup = BeautifulSoup(response.content, 'html.parser')
# images = soup.find_all("img")

# for index, img in enumerate(images):
#     img_url = img.get("src")  
#     if not img_url:
#         continue  

#     if not img_url.startswith("http"):
#         img_url = f"https://books.toscrape.com/{img_url.lstrip('./')}"

   
#     img_data = requests.get(img_url).content
#     img_name = os.path.join(dossier_images, f"image_{index + 1}.jpg")
#     with open(img_name, "wb") as img_file:
#         img_file.write(img_data)




