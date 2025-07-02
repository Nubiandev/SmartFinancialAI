📊 Smart Financial Insights AI Assistant


Welcome to Smart Financial Insights AI Assistant — an AI-powered financial transaction classifier designed to help users automatically categorize business expenses and income using natural language processing and machine learning.

🧠 Overview

Managing financial data manually is tedious and error-prone. This assistant simplifies bookkeeping by predicting the appropriate category (e.g., Travel, Meals, Housing) for each transaction description. Built with Python and Streamlit, it's fast, intuitive, and easy to deploy.

📦 Features

🔍 Transaction Description Analysis

🤖 Category Prediction Using ML Model

📁 Sample CSV Upload & ETL Pipeline

🧪 Automated Testing with Pytest

🌐 Streamlit Web Interface for User Input

🛠️ Technologies Used

Python 3.11

Pandas, NumPy

Scikit-learn (for modeling)

Streamlit (for UI)

Pytest (for testing)

Joblib (for model serialization)

🚀 Getting Started

1. Clone the Repo

git clone https://github.com/Nubiandev/SmartFinancialAI.git
cd SmartFinancialAI

2. Set Up Virtual Environment

python3 -m venv venv
source venv/bin/activate  # or "source venv/bin/activate.fish" if using fish shell
pip install -r requirements.txt

3. Run the App Locally

streamlit run app.py

Then visit: http://localhost:8501

🧪 Run Tests

pytest

Test coverage includes ETL functions and model logic.

📁 Sample Data

A sample CSV file is included at:

sample_data/financial_transactions.csv

Feel free to upload your own CSV using the same format:

Date,Description,Amount,Category

👩🏽‍💻 About the Developer

Built with ❤️ by Erica Smith — Junior AI Developer, certified Scrum Master, and Python enthusiast.

🔗 GitHub

💼 Passionate about AI/ML, FinTech, automation, and helping users simplify complex processes.


📄 License

MIT License

