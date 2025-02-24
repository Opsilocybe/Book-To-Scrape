import requests
from bs4 import BeautifulSoup

url= "https://books.toscrape.com/index.html"
page= requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

product_page_url= url

soupfind= soup.find_all("td")

title= soup.find("h1").text 

upc= soupfind[0].text

price_including_tax= soupfind[2].text

price_excluding_tax= soupfind[3].text

number_available= soupfind[5].text

# product_description= soup.select(".product_page")[0].find_all("p")[3].text 
product_description= soup.find(id="product_description")
next_element= product_description.find_next_sibling().text


#gerer le next element, si il y en pas pas, on passe a autre chose 

category= soup.find("ul", class_="breadcrumb").find_all("li")[2].text

findrating= soup.find("p", class_="instock availability")
review_rating= findrating.find_next_sibling().get("class")[1]


# image=soup.find("div", class_="carousel-inner")
# image_url=image.find_next
image=soup.find("img")
image_url=image.get("src")

print(title, upc, price_including_tax, price_excluding_tax, number_available, category, review_rating, product_description)



