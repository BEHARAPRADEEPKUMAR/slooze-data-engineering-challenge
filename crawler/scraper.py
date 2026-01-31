import requests
from bs4 import BeautifulSoup
from crawler.config import BASE_URL, CATEGORY, MAX_PAGES, DELAY
from crawler.utils import polite_delay

HEADERS = {"User-Agent": "Mozilla/5.0"}


# To Extract extra info from product detail page

def scrape_product_details(url):
    try:
        res = requests.get(url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")

        # Supplier Name
        supplier_tag = soup.select_one(".company-name a")
        supplier = supplier_tag.get_text(strip=True) if supplier_tag else "N/A"

        # Price
        price_tag = soup.select_one(".price")
        price = price_tag.get_text(strip=True) if price_tag else "N/A"

        # MOQ
        moq_tag = soup.find("div", string=lambda x: x and "Min. Order" in x)
        moq = moq_tag.get_text(strip=True) if moq_tag else "N/A"

        return supplier, price, moq

    except:
        return "N/A", "N/A", "N/A"


# Main Scraper
def scrape_products():
    products = []

    for page in range(1, MAX_PAGES + 1):

        url = f"{BASE_URL}{CATEGORY}.html?pv_id=1&page={page}"
        print("\nScraping Listing Page:", url)

        response = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(response.text, "html.parser")

        items = soup.select(".product-name")

        print("Found:", len(items), "products")

        for item in items[:10]:  # limit for safety

            name = item.get_text(strip=True)
            link = item.get("href")

            if link and not link.startswith("http"):
                link = "https://www.made-in-china.com" + link

            # Visit product detail page
            supplier, price, moq = scrape_product_details(link)

            products.append({
                "Product_Name": name,
                "Supplier": supplier,
                "Price": price,
                "MOQ": moq,
                "Product_URL": link,
                "Category": CATEGORY,
                "Page": page
            })

            polite_delay(2)

    return products
