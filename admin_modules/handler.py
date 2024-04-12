import csv
import datetime
from constants import SEARCH_PAGE_COUNT, USER_NAME, SEARCH_KEYWORD


class ScraperHandler:
    def create_scrape_object():
        user_name = input("User Name (default = unknown) : ") or USER_NAME
        search_keyword = input(
            "Search Keyword (default = startup) : ") or SEARCH_KEYWORD
        search_page_count = int(
            input("Search Page Count (default = 1) : ") or SEARCH_PAGE_COUNT)
        search_date = datetime.date.today()
        scrape_object = {
            "user_name": user_name,
            "search_keyword": search_keyword,
            "search_page_count": search_page_count,
            "search_date": search_date
        }
        return scrape_object

    def save_to_scrape_logs(scrape_object):
        with open("./admin_modules/database/scrape_logs.csv", mode="a", newline="", encoding='utf-8') as file:
            writer = csv.writer(file)
            user_name = scrape_object["user_name"]
            search_keyword = scrape_object["search_keyword"]
            search_page_count = scrape_object["search_page_count"]
            search_date = scrape_object["search_date"]
            writer.writerow([user_name, search_keyword,
                            search_page_count, search_date])

    def get_article_blocks(soup):
        article_blocks = []
        article_li_s = soup.find_all("li", attrs={"class": "ov-a"})
        for article_li in article_li_s:
            article_blocks.append(article_li)
        return article_blocks

    def create_article_object(article_block, search_keyword):
        article_category = search_keyword
        article_title = article_block.find(
            "a", attrs={"class": "fz-20"}).get_text()
        article_url = article_block.find(
            "a", attrs={"class": "fz-20"}).get("href")
        author_name = article_block.find(
            "span", attrs={"class": "mr-15"}).get_text().strip("By ")
        image_url = article_block.find("img", attrs={"class": "s-img"})["src"]
        article_object = {
            "article_category": article_category,
            "article_title": article_title,
            "article_url": article_url,
            "author_name": author_name,
            "image_url": image_url
        }
        return article_object

    def save_to_articles_csv(article_object):
        with open("./admin_modules/database/articles.csv", mode="a", newline="", encoding='utf-8') as file:
            writer = csv.writer(file)
            article_category = article_object["article_category"]
            article_title = article_object["article_title"]
            article_url = article_object["article_url"]
            author_name = article_object["author_name"]
            image_url = article_object["image_url"]
            writer.writerow([article_category, article_title,
                            article_url, author_name, image_url])
