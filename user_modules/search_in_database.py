import datetime
import pandas as pd
import csv
from constants import SEARCH_FIELD, SEARCH_KEYWORD, USER_NAME


def create_search_object():
    user_name = input("User Name (default = unknown) : ") or USER_NAME
    search_keyword = input(
        "Search Keyword (default = startup) : ") or SEARCH_KEYWORD
    search_field = input(
        "Search field (default = Article_Title) : ") or SEARCH_FIELD
    search_date = datetime.date.today()
    search_object = {
        "user_name": user_name,
        "search_keyword": search_keyword,
        "search_field": search_field,
        "search_date": search_date
    }
    return search_object


def save_to_logs_csv(search_object):
    with open("./user_modules/database/search_logs.csv", mode="a", newline="", encoding='utf-8') as file:
        writer = csv.writer(file)
        user_name = search_object["user_name"]
        search_keyword = search_object["search_keyword"]
        search_field = search_object["search_field"]
        search_date = search_object["search_date"]
        writer.writerow([user_name, search_keyword, search_field, search_date])


def create_search_output(search_object):
    search_keyword = search_object["search_keyword"]
    search_field = search_object["search_field"]
    df = pd.read_csv("./user_modules/database/articles_normalized.csv")
    filtered_df = df[df[search_field].str.contains(search_keyword, case=False)]
    filtered_df.to_csv(
        f"./user_modules/output/{search_keyword}.csv", index=False)


search_object = create_search_object()
save_to_logs_csv(search_object)
create_search_output(search_object)

print("Done !!")
