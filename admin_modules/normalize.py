import pandas as pd

df = pd.read_csv("./admin_modules/database/articles.csv")

df_normalized = df.drop_duplicates(subset="Article_Title")

df_normalized.to_csv(
    "./admin_modules/database/articles_normalized.csv", index=False)

print("Non-duplicated data saved to 'database/articles_normalized.csv' file !")
