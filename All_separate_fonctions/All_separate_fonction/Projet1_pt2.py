import requests
from bs4 import BeautifulSoup

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

category_url = "https://books.toscrape.com/catalogue/category/books/fiction_10/index.html"
urls = get_category_books(category_url)
print(urls)
