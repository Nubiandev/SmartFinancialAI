import joblib

def predict_category(description):
    try:
        model = joblib.load("modeling/category_predictor.joblib")
        prediction = model.predict([description])[0]
        print(f"\n Predicted Category: {prediction}")
        return prediction
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    desc = input("Enter a transaction description: ")
    predict_category(desc)
