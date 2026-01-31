## To Run the Project Locally

1. Clone the repository:

```bash
git clone https://github.com/BEHARAPRADEEPKUMAR/slooze-data-engineering-challenge.git
cd slooze-data-engineering-challenge
Install all required dependencies:

pip install -r requirements.txt
Run the web scraper (Part A – Data Collection):

python main.py
This will collect product listing data and generate the following output files:

data/raw_products.json

data/clean_products.csv

Run the EDA script (Part B – Exploratory Data Analysis):

python eda/eda_analysis.py
This will display summary statistics, keyword trends, data quality checks, and visualizations.
