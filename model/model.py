import pickle

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

def predict_priority(task):
    vec = vectorizer.transform([task])
    return model.predict(vec)[0]
