import requests
from bs4 import BeautifulSoup
import csv
from scraper import get_all_categories, get_book_data, get_category_books

import csv

def create_csv(title):
    all_data = []
    category_urls = get_all_categories("https://books.toscrape.com/index.html")
    
    for category_url in category_urls:
        book_urls = get_category_books(category_url)
        for book_url in book_urls:
            book_data = get_book_data(book_url)
            all_data.append(book_data)

    # Vérification si des données existent avant d'écrire dans le fichier
    if not all_data:
        print("Aucune donnée à écrire dans le fichier CSV.")
        return

    # Création du fichier CSV
    with open(title, "w", newline="", encoding="utf-8") as fichier:
        writer = csv.writer(fichier)   

        # En-tête du fichier
        writer.writerow([
            "Title", "UPC", "Price (incl. tax)", "Price (excl. tax)", 
            "Availability", "Category", "Review Rating", "Description", 
            "Next Element", "Image URL"
        ])
        
        # Écriture des données
        writer.writerows(all_data)

    print(f"Fichier '{title}' créé avec succès !")

# Exemple d'appel :
create_csv("all_books.csv")





#nommer le fichier ave le nom de la categorie
#faire le title
