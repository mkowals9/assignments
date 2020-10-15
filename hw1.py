from typing import List

import pandas as pd

CONFIRMED_CASES_URL = f"https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data" \
                      f"/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv "

"""
When downloading data it's better to do it in a global scope instead of a function.
This speeds up the tests significantly
"""
confirmed_cases = pd.read_csv(CONFIRMED_CASES_URL, error_bad_lines=False)


def poland_cases_by_date(day: int, month: int, year: int = 2020) -> int:
    """
    Returns confirmed infection cases for country 'Poland' given a date.

    Ex.
    >>> poland_cases_by_date(7, 3, 2020)
    5
    >>> poland_cases_by_date(11, 3)
    31

    :param year: 4 digit integer representation of the year to get the cases for, defaults to 2020
    :param day: Day of month to get the cases for as an integer indexed from 1
    :param month: Month to get the cases for as an integer indexed from 1
    :return: Number of cases on a given date as an integer
    """
    
    # Your code goes here (remove pass)
    return confirmed_cases.loc[confirmed_cases["Country/Region"]=="Poland"][f"{month}/{day}/20"].values[0]


def top5_countries_by_date(day: int, month: int, year: int = 2020) -> List[str]:
    """
    Returns the top 5 infected countries given a date (confirmed cases).

    Ex.
    >>> top5_countries_by_date(27, 2, 2020)
    ['China', 'Korea, South', 'Cruise Ship', 'Italy', 'Iran']
    >>> top5_countries_by_date(12, 3)
    ['China', 'Italy', 'Iran', 'Korea, South', 'France']

    :param day: 4 digit integer representation of the year to get the countries for, defaults to 2020
    :param month: Day of month to get the countries for as an integer indexed from 1
    :param year: Month to get the countries for as an integer indexed from 1
    :return: A list of strings with the names of the coutires
    """

    # Your code goes here (remove pass)
    data="%d/%d/20"%(month,day)
<<<<<<< HEAD
    df=(confirmed_cases[["Country/Region",data]].sort_values(by=data,ascending=True).tail(5)).sort_values(by=data,ascending=False)
    return df["Country/Region"].values[0:5]

=======
    df=confirmed_cases[["Country/Region",data]]
    #print(df[["Country/Region",data]])
    df=df.groupby("Country/Region",as_index=False).sum().sort_values(by=data,ascending=True).tail(5).sort_values(by=data,ascending=False)
    return (df["Country/Region"].values[0:5]).tolist()
>>>>>>> master

import datetime
def no_new_cases_count(day: int, month: int, year: int = 2020) -> int:
    """
    Returns the number of countries/regions where the infection count in a given day was the same as the previous day.

    Ex.
    >>> no_new_cases_count(11, 2, 2020)
    35
    >>> no_new_cases_count(3, 3)
    57

    :param day: 4 digit integer representation of the year to get the cases for, defaults to 2020
    :param month: Day of month to get the countries for as an integer indexed from 1
    :param year: Month to get the countries for as an integer indexed from 1
    :return: Number of countries/regions where the count has not changed in a day
    """
    
    # Your code goes here (remove pass)
<<<<<<< HEAD
     data="%d/%d/20"%(month,day)
    yesterday=datetime.date(year,month,day)-datetime.timedelta(days=1)
    datayest=str("/".join([str(yesterday.month),str(yesterday.day),str(yesterday.year)[-2:]]))
    df=[]
    yes=confirmed_cases[datayest]
    tod=confirmed_cases[data]
    for i in confirmed_cases.index:
        if ((yes[i])!=(tod[i])):
            df.append(confirmed_cases[["Country/Region",datayest,data]])
    return len(df)
=======
    data="%d/%d/20"%(month,day)
    #datayest="%d/%d/20"%(month,day-1)
    yesterday=datetime.date(year,month,day)-datetime.timedelta(days=1)
    datayest=str("/".join([str(yesterday.month),str(yesterday.day),str(yesterday.year)[-2:]]))
    df=[]
    #print(confirmed_cases[["Country/Region",datayest,data]].index)
    #print(confirmed_cases[[datayest,data]].values)
    #print((confirmed_cases[datayest].values)!=(confirmed_cases[data].values))
    yes=confirmed_cases[datayest]
    tod=confirmed_cases[data]
    #print(yes)
    for i in confirmed_cases.index:
        if ((yes[i])!=(tod[i])):
            df.append(confirmed_cases[["Country/Region",datayest,data]])
    #print(df)
    return len(df)
>>>>>>> master
