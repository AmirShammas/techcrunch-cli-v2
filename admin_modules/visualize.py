import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("./admin_modules/database/articles_normalized.csv")

category_counts = df['Article_Category'].value_counts()

category_counts.plot(kind='bar', color='skyblue')

plt.xlabel('Article Category')
plt.ylabel('Number of Articles')
plt.title('Number of Articles in Each Category')

plt.xticks(rotation=45)

plt.show()
