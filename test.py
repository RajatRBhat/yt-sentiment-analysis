import joblib
vectorizer = joblib.load("tfidf_vectorizer.pkl")
comments = ["I love this video", "i hate this video"]
transformed_comments = vectorizer.transform(comments)
print(transformed_comments)