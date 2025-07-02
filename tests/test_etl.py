import pandas as pd
from data_pipeline.etl import load_and_clean_data, summarize_by_category

def test_load_and_clean_data():
    # Sample data
    data = {
        "Date": ["2024-01-01", "2024-01-02"],
        "Description": ["Test 1", "Test 2"],
        "Amount": [100.0, -50.0],
        "Category": ["Income", "Travel"]
    }
    # Convert to DataFrame & save as temp CSV
    df_expected = pd.DataFrame(data)
    df_expected.to_csv("tests/test_transactions.csv", index=False)

    df = load_and_clean_data("tests/test_transactions.csv")

    assert df is not None
    assert len(df) == 2
    assert set(df.columns) == {"Date", "Description", "Amount", "Category"}

def test_summarize_by_category():
    df = pd.DataFrame({
        "Amount": [100.0, -50.0],
        "Category": ["Income", "Travel"]
    })

    summary = summarize_by_category(df)

    assert isinstance(summary, pd.Series)
    assert summary["Income"] == 100.0
    assert summary["Travel"] == -50.0
