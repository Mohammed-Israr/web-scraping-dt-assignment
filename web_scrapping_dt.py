import requests
from bs4 import BeautifulSoup


websites = {
    'Nestle': 'http://www.nestle.com',
    'General Mills': 'http://www.generalmills.com',
    'Unilever' : 'http://www.unilever.com',
    'Tyson Foods' : 'http://www.tysonfoods.com',
    'Johnson & Johnson' : 'http://www.jnj.com',
}
terms_to_search = ["brand","investors","milk","beverages","food","Recipe","chocolate","careers","latest news","ingredients"]

def scrape_and_search_terms(url, terms):
    try:
        response = requests.get(url)
        response.raise_for_status() 
        soup = BeautifulSoup(response.content, "html.parser")
        page_text = soup.get_text().lower()
        found_terms = {}
        for term in terms:
            found_terms[term] = term in page_text
        return found_terms
    except requests.RequestException as e:
        print(f"An error occurred for {url}: {e}")
        return {}


for name, url in websites.items():
    print(f"\nSearching terms in {name} ({url})...")
    results = scrape_and_search_terms(url, terms_to_search)
    for term, is_present in results.items():
        if is_present:
            print(f"'{term}' is present on the {name}.")
        else:
            print(f"'{term}' is not present on the {name} .")
