import json
import pandas as pd
from crawler.scraper import scrape_products

def run_pipeline():
    print("\nStarting Made-in-China Data Collection...\n")

    data = scrape_products()

    # Save Raw JSON
    with open("data/raw_products.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print("✅ Raw JSON saved: data/raw_products.json")

    # Convert to CSV
    df = pd.DataFrame(data)
    df.to_csv("data/clean_products.csv", index=False)

    print("✅ Clean CSV saved: data/clean_products.csv")
    print("\nPipeline Completed Successfully!\n")

if __name__ == "__main__":
    run_pipeline()
