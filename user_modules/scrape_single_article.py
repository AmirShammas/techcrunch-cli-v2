import asyncio
import os
import shutil
import pandas as pd
import requests
import zipfile
from bs4 import BeautifulSoup
from datetime import datetime


async def select_article(csv_file_path):
    df = pd.read_csv(csv_file_path)
    selected_index = int(
        input("Select an article by entering its line number: ")) - 2
    selected_article_url = df.loc[selected_index, 'Article_Url']
    return selected_article_url


async def download_image(image_url, output_folder):
    image_name = datetime.now().strftime("%Y%m%d%H%M%S%f") + ".jpg"
    output_path = os.path.join(output_folder, image_name)
    response = requests.get(image_url, stream=True)
    with open(output_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                file.write(chunk)


async def scrape_article(selected_article_url, output_folder):
    response = requests.get(selected_article_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    article_content = soup.get_text()
    article_content = "\n".join(
        line for line in article_content.splitlines() if line.strip())
    output_file = os.path.join(output_folder, "content.txt")
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(article_content)

    image_urls = [img['src'] for img in soup.find_all('img')]
    tasks = [download_image(image_url, output_folder)
             for image_url in image_urls]
    await asyncio.gather(*tasks)


async def main():
    csv_file_path = "./user_modules/output/google.csv"
    selected_article_url = await select_article(csv_file_path)

    output_folder = "./user_modules/output_single_article/result"
    os.makedirs(output_folder, exist_ok=True)

    await scrape_article(selected_article_url, output_folder)

    zip_file = "./user_modules/output_single_article/result.zip"
    with zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(output_folder):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(
                    file_path, output_folder))

    shutil.rmtree(output_folder)

    print("Extraction and zipping completed successfully !!")

asyncio.run(main())
