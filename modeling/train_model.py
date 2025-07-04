import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
import joblib

def load_data(path):
    df = pd.read_csv(path)
    df.dropna(subset=['Description', 'Category'], inplace=True)
    return df

def train_model(data):
    X = data['Description']
    y = data['Category']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('clf', LogisticRegression(max_iter=1000))
    ])

    pipeline.fit(X_train, y_train)
    y_pred = pipeline.predict(X_test)

    print("\n🧪 Classification Report:\n")
    print(classification_report(y_test, y_pred))

    joblib.dump(pipeline, 'modeling/category_predictor.joblib')
    print("✅ Model saved to: modeling/category_predictor.joblib")

if __name__ == "__main__":
    path = input("📂 Enter path to the financial transactions CSV file: ")
    df = load_data(path)
    train_model(df)
