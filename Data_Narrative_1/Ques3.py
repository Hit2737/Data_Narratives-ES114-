import pandas as pd

books = pd.read_csv("books.csv")
tags = pd.read_csv("tags.csv")
book_ratings = pd.read_csv("ratings.csv")

hi_rng_till_now = 0
for i in books['average_rating']:
  if i>hi_rng_till_now:
    hi_rng_till_now = i

hi_avg_rng_book = books[books['average_rating']==hi_rng_till_now]['original_title'].values[0]
corr_author = books[books['average_rating']==hi_rng_till_now]['authors'].values[0]
print("The book with highest average rating is:",hi_avg_rng_book)
print("The corresponding author is:",corr_author)


athr_books_rngs = books[books['authors']==corr_author]['average_rating'].values


std_dev_rngs = athr_books_rngs.std()
print("The standard deviation of ratings of the required book is:",std_dev_rngs)