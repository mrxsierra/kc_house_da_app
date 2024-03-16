import pandas as pd
import numpy as np
import os

file_path = "../data/unclean_data_kc_house.csv"

# Check if the file exists
if not os.path.isfile(file_path):
    # House Sales in King County, USA Data
    unclean_kc_house_data = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/FinalModule_Coursera/data/kc_house_data_NaN.csv"
    df = pd.read_csv(unclean_kc_house_data)
    df.to_csv(file_path)

def wrangle(path=file_path):
    """
    Import and Clean the King County House Data.

    - Data Wrangling
        - Drop unnecessary columns
        - Handle Missing value
        - Converting date to_datetime
        - Extract Date Components

    return: cleaned data in csv to "data" folder.
    """
    # Import
    df = pd.read_csv(path)
    print("Data Imported Sucessfully..")

    print("--------------Wrangling Data----------------")

    # drop index and id column
    print(f"Droping columns {df.columns[[0, 1]].index.values}..")
    df.drop(df.columns[[0, 1]], axis=1, inplace=True)

    # Handling Missing Value
    nan_columns = df.columns[df.isna().any()].tolist()
    df.loc[:, nan_columns] = df[nan_columns].replace(np.nan, df[nan_columns].mean())

    # Converting date to_datetime
    df['date'] = pd.to_datetime(df['date'], format='%Y%m%dT%H%M%S')

    # Extract Date Components
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['day'] = df['date'].dt.day

    # Save cleaned csv and return path
    cleaned_data_path = "../data/cleaned_data_kc_house.csv"
    df.to_csv(cleaned_data_path)

    return cleaned_data_path

if __name__ == "__main__":
    wrangle()