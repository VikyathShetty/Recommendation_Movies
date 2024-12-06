# MOVIE RECOMMENDATION SYSTEM
My project contains two datasets:

### 1.Credits Dataset

Contains movie ID, title, cast, and crew.
### 2.Movies Dataset

Includes genres, keywords, title, vote average, and many other columns.

**Column Merging and Selection**

Columns were merged based on movie titles.
Only the most relevant columns were selected for analysis.
Text data was extracted from the columns, and non-textual characters were removed.


### Text Combination

Text from all selected columns was combined into a single field to streamline further processing.


### Bag of Words (BoW)

The Bag of Words (BoW) technique, a fundamental method in Natural Language Processing (NLP), was applied to represent the text data.
Each document was treated as a collection of words, ignoring grammar, word order, and structure.
A vocabulary was built from unique words across all documents.
Documents were represented as vectors based on the frequency or presence of words in the vocabulary.


### Stop Word Removal

Stop words were removed to retain only meaningful and relevant text data, improving the quality of the analysis.


### Cosine Similarity Calculation

Cosine similarity was used to compare each movie with all other movies in the dataset.
This technique represents the similarity score in vector format, where:
A value of 1 indicates the most similar movies.
A value of 0 indicates the least similar movies.


### Similarity Index

Movies were ranked based on their similarity index.
The movies with the highest similarity scores were identified.
Top 5 Similar Movies

For each movie, the top 5 most similar movies were retrieved and displayed.


### Flask-based web application 

Movie Input

The user submits the name of a movie through the Flask web interface.
Retrieve Similar Movie Names

Using the pre-computed cosine similarity scores, the system identifies the top 5 movies most similar to the input movie.
Display Results

The top 5 similar movies are displayed on the web page, allowing the user to explore recommendations effortlessly.


![Example Image](https://github.com/VikyathShetty/Recommendation_Movies/blob/main/images/Screenshot%202024-12-06%20175628.png)



