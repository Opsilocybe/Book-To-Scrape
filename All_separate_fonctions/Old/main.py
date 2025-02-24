from scraper import get_book_data, get_category_books, get_all_categories, create_csv
from tqdm import tqdm

def main():
    index_url = "https://books.toscrape.com/index.html"

    # récupérer toutes les catégories du site
    categories = get_all_categories(index_url)

    # pour chaque catégorie, récupérer les liste des urls de tous les livres contenus dedans
    for cat_url in tqdm(categories):
        books = get_category_books(cat_url)
       

        #écrire le csv
        all_data = []
        for book_url in tqdm(books):
            data = get_book_data(book_url)
            all_data.append(data)

        create_csv(all_data)
        

        # sauvegarder les images
        # save_images(books
        



if __name__ == "__main__":
    main()