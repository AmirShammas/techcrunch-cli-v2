import asyncio
import aiohttp
from bs4 import BeautifulSoup
from handler import ScraperHandler
from constants import SEARCH_URL


if __name__ == "__main__":
    try:
        async def fetch_page(session, url):
            async with session.get(url) as response:
                return await response.text()

        async def scrape_page(search_keyword, page_number):
            url = SEARCH_URL.format(
                search_keyword=search_keyword, page_number=page_number)
            async with aiohttp.ClientSession() as session:
                html = await fetch_page(session, url)
                soup = BeautifulSoup(html, "html.parser")
                article_blocks = ScraperHandler.get_article_blocks(soup)
                for article_block in article_blocks:
                    article_object = ScraperHandler.create_article_object(
                        article_block, search_keyword)
                    ScraperHandler.save_to_articles_csv(article_object)

        async def scrape_pages():
            tasks = []
            scrape_object = ScraperHandler.create_scrape_object()
            search_keyword = scrape_object["search_keyword"]
            search_page_count = scrape_object["search_page_count"]
            print("Scraping ...! Please wait ...!")
            for page_number in range(1, search_page_count + 1):
                page_number = (page_number*10)-9
                task = asyncio.create_task(
                    scrape_page(search_keyword, page_number))
                tasks.append(task)
            await asyncio.gather(*tasks)
            ScraperHandler.save_to_scrape_logs(scrape_object)
            print("Scraping Completed Successfully !!")

        asyncio.run(scrape_pages())

    except Exception as error:
        print("ERROR !!", error)
    finally:
        print("END !!")
