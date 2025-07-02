import pandas as pd

def load_and_clean_data(filepath):
    try:
        # Load CSV
        df = pd.read_csv(filepath)

        # Basic cleaning
        df.dropna(how='all', inplace=True)  # Drop empty rows
        df.columns = df.columns.str.strip()  # Remove leading/trailing spaces
        df = df.fillna(0)  # Replace NaNs with 0 (or customize later)

        # Preview the first few rows
        print("Data loaded successfully:")
        print(df.head())

        return df

    except Exception as e:
        print(f"Error loading data: {e}")
        return None


def summarize_by_category(df):
    try:
        print("\n📊 Total Amount by Category:\n")
        summary = df.groupby("Category")["Amount"].sum().sort_values()
        print(summary)
        return summary

    except Exception as e:
        print(f"Error summarizing data: {e}")
        return None


if __name__ == "__main__":
    path = input("📂 Enter path to the financial transactions CSV file: ")
    df = load_and_clean_data(path)

    if df is not None:
        summarize_by_category(df)
