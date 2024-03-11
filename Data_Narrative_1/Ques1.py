import pandas as pd
import matplotlib.pyplot as plt

books = pd.read_csv("books.csv")
tags = pd.read_csv("tags.csv")
book_ratings = pd.read_csv("ratings.csv")

JKR_books = books.loc[books['authors'] == 'J.K. Rowling', 'book_id'].unique() 
JK_ratings = book_ratings.loc[book_ratings['book_id'].isin(JKR_books)]  
prob_rated_above_4 = (JK_ratings['rating'] >= 4).mean()  

print(f"The probability that J.K. Rowling's books are rated 4 or more is {prob_rated_above_4:.4f}")

plt.hist(JK_ratings['rating'], bins=10)
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.title('Distribution of Ratings for J.K. Rowling Books')
plt.show()