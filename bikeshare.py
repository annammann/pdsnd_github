import time
import datetime as dt
import pandas as pd
import numpy as np
import tabulate as tabulate

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = {'january':1, 'february':2, 'march': 3, 'april': 4, 'may': 5, 'june':6}
days = {'monday':0, 'tuesday':1, 'wednesday':2, 'thursday':3, 'friday':4, 'saturday':5, 'sunday':6}
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Would you like to see data for Chicago, New York City (NYC), or Washington?: ')
    city = city.lower()
    # allowing user input to be nyc/NYC/nYc/NyC... convert to new york city for logic compares
    if city == 'nyc':
        city = 'new york city'
    while (city != 'chicago' and
           city != 'new york city' and
           city != 'washington'):
           print('-'*40)
           # allow user to decide if they want to continue if they entered in an invalid option
           cont = input('Seems the city you entered is not Chicago, New York City (NYC), or Washington.\nWould you like to continue & try again? Enter yes or no. ')
           if (cont == 'no'):
               exit()
           city = input('Would you like to see data for Chicago, New York City (NYC), or Washington?: ')
           city = city.lower()
           if city == 'nyc':
               city = 'new york city'

    # get user input for month (all, january, february, ... , june)
    # default filters to 'all'
    month = 'all'
    day = 'all'
    filter = input('Would you like to filter by month, day, or not at all? ')
    if (filter.lower() == 'month'):
        month = input('Enter month (January, February, March, April, May, or June? Please type out the full month name.): ')
        user_input = month
        month = month.lower()
        while (month not in months):
               print('-'*40)
               # allow user to decide if they want to continue if they entered in an invalid option
               cont = input('Seems like you entered a month (' + user_input + ') that is not: January, February, March, April, May, or June.\nWould you like to continue & try again? Enter yes or no. ')
               if (cont == 'no'):
                   exit()
               month = input('Enter month (January, February, March, April, May, or June? Please type out the full month name.): ')
               user_input = month
               month = month.lower()
        further_filter = input('Would you like to further filter by day? Enter yes or no. ')
        if (further_filter == 'yes'):
            day  = input('Enter day (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday): ')
            user_input = day
            day = day.lower()
            day = validate_day(day)

    # get user input for day of week (all, monday, tuesday, ... sunday)
    elif (filter.lower() == 'day'):
        day = input('Enter day (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday): ')
        user_input = day
        day = day.lower()
        day = validate_day(day)

    print('-'*40)
    return city, month, day

def validate_day(day):
    """
    Analyzes the day input from user and asks if they want to continue or retry entering day again.

    Returns:
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    while (day not in days):
           print('-'*40)
           user_input = day
           cont = input('Seems like you entered a day (' + user_input + ') that is not: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday.\nWould you like to continue & try again? Enter yes or no. ')
           if (cont == 'no'):
               return 'all'
           day = input('Enter day (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday): ')
           user_input = day
           day = day.lower()
    return day

def read_csv_data(city):
    """
    Loads data for the specified city with no filters. So, can parse through
    all the raw data when requested by user
    Args:
        (str) city - name of the city to analyze
    Returns:
        df - Pandas DataFrame containing city data unfiltered
    """

    df = pd.read_csv(CITY_DATA[city])
    return df

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = read_csv_data(city)

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday

    df['start_end_station'] = df['Start Station'] + " --> " + df['End Station']

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = months.get(month)
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        day = days.get(day)
        df = df[df['day_of_week'] == day]

    return df

def time_stats(df):
    """
    Displays statistics on the most frequent times of travel.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    key_list = list(months.keys())
    print('\nMost Popular month: ', key_list[common_month-1].title())

    # display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    key_list = list(days.keys())
    print('Most Popular day of week: ', key_list[common_day_of_week].title())

    # display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most common hour (from 0 to 23)
    popular_hour = df['hour'].mode()[0]
    AM_PM = "AM"
    if popular_hour > 12:
        popular_hour = int(popular_hour) - 12
        AM_PM = "PM"
    elif popular_hour == 12:
        AM_PM = "PM"
    print('Most Popular Start Hour: ', str(popular_hour) + AM_PM)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """
    Displays statistics on the most popular stations and trip.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print('Most Popular starting station: ', common_start)

    # display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print('Most Popular ending station: ', common_end)

    # display most frequent combination of start station and end station trip
    common_start_end = df['start_end_station'].mode()[0]
    print('Most frequent combination of start and end station trip: ', common_start_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """
    Displays statistics on the total and average trip duration.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time: ', total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean_travel_time: ', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """
    Displays statistics on bikeshare users.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # Display counts of gender
    try:
        gender_types = df['Gender'].value_counts()
        # Display earliest, most recent, and most common year of birth
        earliest_birth_year = df['Birth Year'].min()
        latest_birth_year = df['Birth Year'].max()
        common_birth_year = df['Birth Year'].mode()[0]
        print("\nThe earliest, most recent, and most common years of birth (respectively):")
        message = "{}, {}, {}"
        print(message.format(int(earliest_birth_year), int(latest_birth_year), int(common_birth_year)))
    except KeyError:
        gender_types = "No user data included for Washington"
    print(gender_types)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    pd.set_option("display.max_columns",200)
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        print(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        # ask user if they want to see raw data
        cont = input("Would you like to see the raw data for " + city.title() + "? Enter yes(y) or no.\n")
        if cont == 'yes' or cont == 'y':
            # reload the city data unfiltered
            df = read_csv_data(city)
            cont = 'y'
        index = 0
        # loop through as long as the user says yes and still data
        while cont.lower() == 'y' and index <= len(df): # add check for end of df
            print('*'*40)
            print(df.loc[0+index:5+index])
            cont = input("Would you like to see the next 5 rows of raw data? Enter yes(y) or no.\n")
            if cont == 'yes':
                cont = 'y'
            index += 5
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes' and restart.lower() != 'y':
            break

if __name__ == "__main__":
	main()
