import sys, os, time
import pandas as pd


def transform_data(extracted_dataframe):
    # Perform your data cleaning/transformation here

    new_column_names = {
        "Release": "release_date",
        "Movie": "movie_title",
        "Bond": "bond_actor",
        "Bond_Car_MFG": "car_manufacturer",
        "US_Gross": "income_usa",
        "World_Gross": "income_world",
        "Budget": "movie_budget",
        "Film_Length": "film_length",
        "Avg_User_IMDB": "imdb",
        "Avg_User_Rtn_Tom": "rotten_tomatoes",
        "Martinis": "martinis_consumed",
        "Kills_Bond": "bond_kills",
    }

    data = extracted_dataframe.rename(columns=new_column_names)

    print("")
    print("")
    print("Initial Data Information")
    print("--------------------")

    print(data.iloc[:])

    time.sleep(2)

    print("")
    print("")
    print("Data Columns")
    print("--------------------")

    print(data.columns)

    time.sleep(2)

    print("")
    print("")
    print("Data Information")
    print("--------------------")

    data.info()

    time.sleep(2)

    print("")
    print("")
    print("Check Null Data")
    print("--------------------")

    print(data.loc[data.isna().any(axis="columns")])

    time.sleep(2)

    print("")
    print("")
    print("Check Column Data For Further Processing")
    print("--------------------")

    print(data[["income_usa", "income_world", "movie_budget", "film_length"]].head())
    
    time.sleep(2)

    print("")
    print("")
    print("Check Column For Mispelled Data")
    print("--------------------")

    print(data["bond_actor"].value_counts())

    time.sleep(2)

    print("")
    print("")
    print("Check Column For Data Information")
    print("--------------------")

    print(data[["film_length", "martinis_consumed"]].describe())

    time.sleep(2)

    print("")
    print("")
    print("Remove null data")
    print("--------------------")

    data.dropna(inplace=True) 

    time.sleep(2)

    print("")
    print("")
    print("Fix Column Data Information")
    print("--------------------")

    data = (

        data.assign(
            income_usa=lambda data: (
                data["income_usa"]
                .replace("[$,]", "", regex=True)
                .astype("Float64")
            ),
            income_world=lambda data: (
                data["income_world"]
                .replace("[$,]", "", regex=True)
                .astype("Float64")
            ),
            movie_budget=lambda data: (
                data["movie_budget"]
                .replace("[$,]", "", regex=True)
                .astype("Float64")
                * 1000
            ),
            release_date=lambda data: pd.to_datetime(
                data["release_date"], format="%B, %Y"
            ),
            release_year=lambda data: (
                data["release_date"]
                .dt.year
                .astype("Int64")
            ),
        
            film_length=lambda data: (
                data["film_length"]
                .str.removesuffix("mins")
                .astype("Int64")
                .replace(1200,120)
            ),
                bond_actor=lambda data: (
                data["bond_actor"]
                .str.replace("Shawn", "Sean")
                .str.replace("MOORE", "Moore")
            ),
                martinis_consumed=lambda data: (
                data["martinis_consumed"].replace(-6, 6)
         ),
     )
    .drop_duplicates(ignore_index=True)
    )

    time.sleep(2)

    print("")
    print("")
    print("Check Data Information After Cleaning")
    print("--------------------")

    print(data[["film_length", "martinis_consumed"]].describe())

    time.sleep(2)

    print("")
    print("")
    print("Check For Duplicated Data")
    print("--------------------")

    print(data.loc[data.duplicated(keep=False)])

    time.sleep(2)
        

    print("")
    print("")
    print("Final Data Returned")
    print("--------------------")
    print(data)

    return data