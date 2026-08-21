"""
data_loader.py

Handles loading and cleaning the customer shopping dataset.
Centralizing this logic here means every notebook in this project loads
and cleans data identically, avoiding copy-pasted inconsistencies.
"""

import os
import pandas as pd


def load_raw_data(file_path):
    """
    Loads the raw CSV file from disk.

    Parameters
    ----------
    file_path : str
        Full path to the raw customer_shopping_data.csv file.

    Returns
    -------
    pd.DataFrame
        Unmodified dataset as read from disk.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Dataset not found at: {file_path}")

    df = pd.read_csv(file_path)
    return df


def clean_and_engineer(df):
    """
    Applies the full Phase 1-2 cleaning and feature engineering pipeline.

    Parameters
    ----------
    df : pd.DataFrame
        Raw dataset as returned by load_raw_data().

    Returns
    -------
    pd.DataFrame
        Cleaned dataset with derived time, revenue, and age group columns.
    """
    df = df.drop_duplicates().copy()

    df["invoice_date"] = pd.to_datetime(df["invoice_date"], format="%d/%m/%Y")
    df["year"] = df["invoice_date"].dt.year
    df["month"] = df["invoice_date"].dt.month
    df["month_name"] = df["invoice_date"].dt.strftime("%b")
    df["quarter"] = df["invoice_date"].dt.quarter
    df["weekday"] = df["invoice_date"].dt.day_name()

    df["total_amount"] = (df["quantity"] * df["price"]).round(2)

    age_bins = [17, 24, 34, 44, 54, 64, 100]
    age_labels = ["18-24", "25-34", "35-44", "45-54", "55-64", "65+"]
    df["age_group"] = pd.cut(df["age"], bins=age_bins, labels=age_labels)

    return df


def load_clean_dataset(raw_path):
    """
    Convenience wrapper: loads and cleans in a single call.

    Parameters
    ----------
    raw_path : str
        Full path to the raw CSV file.

    Returns
    -------
    pd.DataFrame
        Fully cleaned, feature-engineered dataset ready for analysis.
    """
    df = load_raw_data(raw_path)
    df = clean_and_engineer(df)
    return df


def save_processed(df, output_path):
    """
    Saves a cleaned DataFrame to the processed data folder.

    Parameters
    ----------
    df : pd.DataFrame
        Cleaned dataset to persist.
    output_path : str
        Full path where the CSV should be written.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Processed dataset saved to: {output_path}")