# Python-Word-Cloud

I wanted to create a word cloud visualization in Python. Word Cloud allows us to visually see what words frequently show up in a text. The most common application of word clouds in business is usually customer feedback. I decided to go on Kaggle to find a customer survey dataset that I could use to create a wordcloud Visualization. I found this Kaggle dataset https://www.kaggle.com/datasets/arushchillar/disneyland-reviews that had customer reviews of three disneyland branches. I created a Python script to clean the data and to create a word cloud visualization of the 100 most used words in the survey. My focus for this project was more on working with a larger dataset and cleaning it while also creating a word cloud visualization with that dataset.

## About the dataset

There were 42,656 rows that had reviews in the review_text column. It was important that I removed punctuation and capitalization in all of the reviews as the script would recognize any punctuations as words and any words with capitzalizations as unique words. 

## Libraries 
* re
* pandas
* numpy
* wordcloud
* matplotlib

## Improvements or ideas moving forward.
The biggest flaw with the script is that it will count plural words or verbs with multiple forms as unique words. Another problem with this script is that it's slow it takes about 20 seconds for the visualization to generate due to the for loop having to go through so many iterations. There is probably a faster way to get the word frequency but I am happy that it gets the job done.

![Word_cloud](https://user-images.githubusercontent.com/112991083/221319964-6df0fd20-003d-492e-a881-69ecb7b00db6.jpeg)
