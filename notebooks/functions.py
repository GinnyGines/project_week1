import pandas as pd


def load_dataset(url):
    """
    Load the dataset from the specified URL into a pandas DataFrame.
    
    Args:
    - url (str): The URL of the dataset.
    
    Returns:
    - df (DataFrame): The loaded DataFrame.
    """
    df = pd.read_csv(url)
    return df

def sort_by_date(df):
    """
    Sort the DataFrame by date in ascending order.
    
    Args:
    - df (DataFrame): The DataFrame to be sorted.
    
    Returns:
    - df_sorted (DataFrame): The sorted DataFrame.
    """
    df_sorted = df.sort_values(by='Date')
    return df_sorted

def main():
    # URL of the dataset
    url = 'https://www.football-data.co.uk/mmz4281/1920/E0.csv'

    # Load the dataset
    df = load_dataset(url)

    # Display the first few rows of the original DataFrame
    print("Original DataFrame:")
    print(df.head())
    print()

    # Sort the DataFrame based on Date
    df_sorted = sort_by_date(df)

    # Display the sorted DataFrame
    print("Sorted DataFrame based on Date:")
    print(df_sorted.head())