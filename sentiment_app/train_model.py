import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
import joblib  # Corrected import statement

# Load the movie review dataset from NLTK
from nltk.corpus import movie_reviews
from nltk.corpus import stopwords

# Create a DataFrame from the NLTK movie review dataset
documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]
df = pd.DataFrame(documents, columns=['text', 'label'])

# Preprocess the text data
df['text'] = df['text'].apply(lambda x: ' '.join(x))
df['text'] = df['text'].str.lower()

# Split the dataset into train and test sets
train_df = df.sample(frac=0.8, random_state=42)
test_df = df.drop(train_df.index)

# Create a pipeline with TfidfVectorizer and SVC
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words=stopwords.words('english'))),
    ('clf', SVC(kernel='linear', C=1.0))
])

# Fit the pipeline on the training data
pipeline.fit(train_df['text'], train_df['label'])

# Serialize the trained model to a file
joblib.dump(pipeline, 'movie_review_model.pkl')

# Load the model from the file
loaded_model = joblib.load('movie_review_model.pkl')


