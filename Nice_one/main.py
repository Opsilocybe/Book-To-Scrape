from scraper import get_book_data, get_category_books, get_all_categories, create_csv, populate_csv, create_folder, dl_image
from tqdm import tqdm
import os

def main():
    index_url = "https://books.toscrape.com/index.html"
    
    create_folder()

    

    # récupérer toutes les catégories du site
    categories = get_all_categories(index_url)

    # pour chaque catégorie, récupérer les liste des urls de tous les livres contenus dedans
    for cat_url in (categories):
        url_propre = cat_url[0]
        nom_propre = cat_url[1]
        create_csv("Info_livre/all_the_csv/" + nom_propre)
        books = get_category_books(url_propre)
        #écrire le csv
        all_data = []
        for book_url in tqdm(books):
            data = get_book_data(book_url)
            base_url_image = data[8]
            clean_url_image = base_url_image.replace('../..', 'https://books.toscrape.com')
            titre= data[1]
            dl_image(clean_url_image, "Info_livre/images_produits/" + titre + ".jpg")

            populate_csv(data, "Info_livre/all_the_csv/" + nom_propre + ".csv")
            all_data.append(data)

    


    

            

        



if __name__ == "__main__":
    main()