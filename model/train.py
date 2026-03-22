import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

data = pd.read_csv("../data/dataset.csv")

x = data["task"]
y = data["priority"]

vectorizer = CountVectorizer()
X_vec = vectorizer.fit_transform(x)

model = MultinomialNB()
model.fit(X_vec, y)

pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))