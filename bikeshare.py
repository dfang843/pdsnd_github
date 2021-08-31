import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}
cities = ['chicago', 'new york city', 'washington']
months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
dates = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # Get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = str(input("Which city do you want to get input from: chicago, new york city, or washington?")).lower()
    while city not in cities:
        city = str(input("Sorry, that city does not exist in this database. Please try again.")).lower()
    # Get user input for month (all, january, february, ... , june)
    month = str(
        input("Which month do you want to get input from: all, january, february, march, april, may or june?")).lower()
    while month not in months:
        month = str(input("Sorry, that month does not exist. Please try again.")).lower()
    # Get user input for day of week (all, monday, tuesday, ... sunday)
    day = str(input(
        "Which day do you want to get input from: all, monday, tuesday, wednesday, thursday, friday, saturday, sunday")).lower()
    while day not in dates:
        day = str(input("Sorry, that day does not exist. Please try again.")).lower()
    print('-' * 40)
    return city, month, day

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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        global months
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    global months
    # Display the most common month
    print("Most common month: " + months[df['month'].mode()[0] - 1])
    # Display the most common day of week
    print("Most common day of week: " + df['day_of_week'].mode()[0])
    # Display the most common start hour
    hour = df['Start Time'].dt.hour.mode()[0]
    print('The most common start hour is: {}:00'.format(hour))
    time1 = round(time.time() - start_time, 2)
    print("\nThis took %s seconds." % (time1))
    print('-' * 40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # Display most commonly used start station
    print("Most popular start station: " + df['Start Station'].mode()[0])
    # Display most commonly used end station
    print("Most popular end station: " + df['End Station'].mode()[0])
    # Display most frequent combination of start station and end station trip
    print("Most popular combination of stations: " + (df['Start Station'] + ", " + df['End Station']).mode()[0])
    time1 = round(time.time() - start_time, 2)
    print("\nThis took %s seconds." % (time1))
    print('-' * 40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Total Time'] = df['End Time'] - df['Start Time']

    print("Total Travel Time: " + str(df['Total Time'].sum()))

    print("Mean Travel Time: " + str(df['Total Time'].mean()))
    time1 = round(time.time() - start_time, 2)

    print("\nThis took %s seconds." % (time1))
    print('-' * 40)

def user_stats1(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("User Type Statistics:")
    print(df['User Type'].value_counts())

    # Display counts of gender
    print("Gender Statistics:")
    print(df['Gender'].value_counts())

    # Display earliest, most recent, and most common year of birth
    print("Earliest Year of Birth: ", end="")
    print(int(df['Birth Year'].min()))
    print("Latest Year of Birth: ", end="")
    print(int(df['Birth Year'].max()))
    print("Most common year of birth: " + str(int(df['Birth Year'].mode()[0])))
    time1 = round(time.time() - start_time, 2)

    print("\nThis took %s seconds." % (time1))
    print('-' * 40)

def user_stats2(df):
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("User Type Statistics:")
    print(df['User Type'].value_counts())

    print("Gender and Birth Date data is unavailable at this time, sorry")
    time1 = round(time.time() - start_time, 2)
    print("\nThis took %s seconds." % (time1))
    print('-' * 40)

def main():
    lst = ['yes', 'no']
    while True:
        i = 0
        city, month, day = get_filters()
        df = load_data(city, month, day)
        data = input("Do you want to see the first 5 lines of raw data?")
        while data.lower() not in lst:
            data = input("That was not valid. Please try again.")
        while data.lower() == "yes":
            print(df[i: i + 5])
            data = input("Do you want to show 5 more rows of raw data?")
            i += 5
        time = input("Do you want to learn about the most frequent times of travel based on your filters? Yes or no.")
        while time.lower() not in lst:
            time = input("That was not valid. Please try again.")
        if time.lower() == "yes": time_stats(df)
        station = input("Do you want to learn about the most popular stations based on your filters?")
        while station.lower() not in lst:
            station = input("That was not valid. Please try again.")
        if station.lower() == "yes": station_stats(df)
        trip_duration = input("Do you want to learn about the total and average trip duration based on your filters?")
        while trip_duration.lower() not in lst:
            trip_duration = input("That was not valid. Please try again.")
        if trip_duration.lower() == "yes": trip_duration_stats(df)
        user = input("Do you want to learn about the user statistics based on your filters?")
        while user.lower() not in lst:
            user = input("That was not valid. Please try again.")
        if user.lower() == "yes":
            if city == "washington":
                user_stats2(df)
            else:
                user_stats1(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes': break

if __name__ == "__main__":
    main()