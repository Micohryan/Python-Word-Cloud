import re
import pandas as pd
import numpy as np
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

stopwords = set(STOPWORDS)

data = pd.read_csv('DisneylandReviews.csv', encoding='latin-1')
df = pd.DataFrame()
df['Text'] = data['Review_Text']
df['Text'] = df['Text'].str.lower() # Convert all strings to lowercase
df['Text'] = df['Text'].str.replace('[^\w\s]', '', regex= True) #remove all punctuations

review_words = ''
# iterate through the dataframe
for val in df.Text:
 
    # split the value
    tokens = val.split()
     
    review_words += " ".join(tokens)+" "

#create word Cloud Object
wordcloud = WordCloud(max_words = 100, width = 800, height = 600,
                background_color ='white',
                stopwords = stopwords,
                min_font_size = 10).generate(review_words)

#Create Figure
plt.imshow(wordcloud)
plt.axis('off')
plt.show()