import pandas as pd
import matplotlib.pyplot as plt

books = pd.read_csv("books.csv")
tags = pd.read_csv("tags.csv")
book_ratings = pd.read_csv("ratings.csv")
book_tags = pd.read_csv("book_tags.csv")


tag_21cf = tags[tags['tag_name'] == '21st-century-fiction']['tag_id'].values[0]
tag_hnf = tags[tags['tag_name'] == 'historical-non-fiction']['tag_id'].values[0]

books_21cf = book_tags[(book_tags['tag_id'] == tag_21cf)]
books_hnf = book_tags[(book_tags['tag_id'] == tag_hnf)]


book_id_21cf = books_21cf['goodreads_book_id'].values
book_id_hnf = books_hnf['goodreads_book_id'].values


rng_21cf = book_ratings[book_ratings['book_id'].isin(book_id_21cf)]
rng_hnf = book_ratings[book_ratings['book_id'].isin(book_id_hnf)]


no_rng_21cf = len(rng_21cf)
no_rng_hnf = len(rng_hnf)

print('Number of ratings for 21st-century-fiction books:', no_rng_21cf)
print('Number of ratings for historical-non-fiction books:', no_rng_hnf)

plt.bar(['21st-century-fiction', 'historical-non-fiction'], [no_rng_21cf, no_rng_hnf])
plt.xlabel('Genre')
plt.ylabel('Number of Ratings')
plt.title('Comparison of Ratings for 21st-Century-Fiction and Historical-Non-Fiction Books')
plt.show()
