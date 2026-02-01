from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC

def train_model(df):
    X = df['Message']
    y = df['Label']

    X_train, _, y_train, _ = train_test_split(
        X, y, test_size=0.2, random_state=0
    )

    vectorizer = TfidfVectorizer()
    X_train_tfidf = vectorizer.fit_transform(X_train)

    model = SVC(kernel='rbf', gamma=0.2, C=1.0)
    model.fit(X_train_tfidf, y_train)

    return model, vectorizer
