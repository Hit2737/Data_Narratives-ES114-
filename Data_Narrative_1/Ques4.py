import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

books = pd.read_csv("books.csv")
tags = pd.read_csv("tags.csv")
book_ratings = pd.read_csv("ratings.csv")

book_stat = book_ratings.groupby('book_id').agg({'rating': [np.mean, np.size]})
book_stat.columns = ['avg_rng', 'no_of_rngs']

plt.scatter(book_stat['avg_rng'], book_stat['no_of_rngs'], alpha=0.2)
plt.xlabel('Average Rating')
plt.ylabel('Number of Ratings')
plt.title('Plot Between Average Rating and Number of Ratings')
plt.show()