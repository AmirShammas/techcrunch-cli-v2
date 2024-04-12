# Techcrunch-CLI-V2

This app scrapes into the [techcrunch](https://search.techcrunch.com) website and saves the scraped articles data into a csv file. Then the user can search into this database and scrape the detailed contents of a selected article.

## Installation

This app is developed using python 3.11.

After making venv, install the necessary packages using the command below:

```
pip install -r requirements.txt
```

## Usage

Run `./admin_modules/scrape.py` file and enter your optional values for `User Name` (default = unknown) and `Search Keyword` (default = startup) and `Search Page Count` (default = 1). The scraped_data will be saved in `./admin_modules/database/articles.csv` file. The scraping _log will be saved in `./admin_modules/database/scrape_logs.csv` file.

Run `./admin_modules/normalize.py` file in order to delete the duplicated items. The normalized data will be saved in `./admin_modules/database/articles_normalized.csv` file.

Run `./admin_modules/visualize.py` file in order to plot the number of articles in each category.

Copy `./admin_modules/database/articles_normalized.csv` file into `./user_modules/database/` folder.

Run `./user_modules/search_in_database.py` file and enter your optional values for `User Name` (default = unknown) and `Search Keyword` (default = startup) and `Search field` (default = Article_Title). The searched_data will be saved in `./user_modules/output/<search_keyword>.csv` file. The searching _log will be saved in `./user_modules/database/search_logs.csv` file.

Copy the path of your selected search file under `csv_file_path` variable in `./user_modules/scrape_single_article.py` file.

Run `./user_modules/scrape_single_article.py` file and enter the line number of your selected article. The contents and images of this article will be saved in `./user_modules/output_single_article/result.zip` file.
