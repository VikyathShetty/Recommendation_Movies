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


###Text Combination

Text from all selected columns was combined into a single field to streamline further processing.


###Bag of Words (BoW)

The Bag of Words (BoW) technique, a fundamental method in Natural Language Processing (NLP), was applied to represent the text data.
Each document was treated as a collection of words, ignoring grammar, word order, and structure.
A vocabulary was built from unique words across all documents.
Documents were represented as vectors based on the frequency or presence of words in the vocabulary.


###Stop Word Removal

Stop words were removed to retain only meaningful and relevant text data, improving the quality of the analysis.


