import pandas as pd
import matplotlib.pyplot as plt

books = pd.read_csv("books.csv")
tags = pd.read_csv("tags.csv")
book_ratings = pd.read_csv("ratings.csv")

books['pb_yr'] = books['original_publication_year'].astype(str).str.extract('(\d{4})')
book_rng_and_pbyr = pd.merge(books[['book_id', 'pb_yr']], book_ratings, on='book_id')
rng_by_yr = book_rng_and_pbyr.groupby('pb_yr').agg({'book_id': 'count'})
print(rng_by_yr)

plt.plot(rng_by_yr.index.astype(int), rng_by_yr, label='Number of Ratings')
plt.legend()
plt.xlabel('Publishing Year')
plt.ylabel('No. of Ratings')
plt.title('Plot between No. of Ratings andPublishing year')
plt.show()