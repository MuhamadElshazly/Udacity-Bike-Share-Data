import time
import pandas as pd
#import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
list_of_city = ('chicago' , 'new york city' , 'washington' )
list_of_months = ('january', 'february', 'march', 'april', 'may', 'june', 'all')
list_of_days = ('monday','tuesday','wednesday','thursday','friday','saturday','sunday','all')


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ""
    for cit in list_of_city :
        cities += cit + ", "

    city = input ("\n enter name of the city you want to analyze from this list :\n " + cities + ": ").lower()
    while city not in CITY_DATA :
        print('\n That\'s not a valid city!')
        city = input ("\n enter name of the city you want to analyze from this list :\n " + cities + ": ").lower()



    # TO DO: get user input for month (all, january, february, ... , june)

    months = ""
    for mon in list_of_months :
        months += mon + ", "

    month = input ('\n enter name of the month to filter by from this list :\n ' + months + ', or "all" to apply no month filter ').lower()
    while month not in list_of_months :
        print('\n That\'s not a valid month!')
        month = input ('\n enter name of the month to filter by from this list :\n ' + months + ', or "all" to apply no month filter ').lower()


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ""
    for da in list_of_days :
        days += da + ", "
    day = input('\n name of the day of week to filter by from this list :\n ' + days + ', or "all" to apply no month filter ').lower()
    while day not in list_of_days :
        print('\n That\'s not a valid day!')
        day = input('\n name of the day of week to filter by from this list :\n ' + days + ', or "all" to apply no month filter ').lower()



    print('-'*40)
    print (city + "-" + month + "-" + day)
    print('-'*40)
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
    # loading data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # converting the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, day of week and hour from Start Time to create new columns
    df['Month'] = df['Start Time'].dt.month
    df['Day Of The Week'] = df['Start Time'].dt.weekday_name
    df['Hour'] = df['Start Time'].dt.hour

    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['Month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['Day Of The Week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['Month'].mode()[0]
    print('Most Popular Month:', popular_month)

    # TO DO: display the most common day of week
    popular_day = df['Day Of The Week'].mode()[0]
    print('Most Popular Day Of The Week:', popular_day)

    # TO DO: display the most common start hour
    popular_hour = df['Hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_Start_Station = df['Start Station'].mode()[0]
    print('Most Popular Start Station:', popular_Start_Station)

    # TO DO: display most commonly used end station
    popular_End_Station = df['End Station'].mode()[0]
    print('Most Popular End Station:', popular_End_Station)

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = 'from ( ' + df['Start Station'] + ' ) station, to ( ' + df['End Station' ] + ' ) station '
    comp_Station = df['combination'].mode()[0]
    print('Most frequent combination of start station and end station trip : \n', comp_Station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Trip Duration = '+ str(total_travel_time) + ' sec.')

    # TO DO: display mean travel time
    travel_time_mean = df['Trip Duration'].mean()
    print('travel time mean  = '+ str(travel_time_mean) + ' sec.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_of_user_types = df['User Type'].value_counts()
    print( counts_of_user_types )

    # TO DO: Display counts of gender

    if 'Gender' in df :
        counts_of_gender = df['Gender'].value_counts()
        print( counts_of_gender )
    else :
        print('There is no column gender in this city data')


    # TO DO: Display earliest, most recent, and most common year of birth
    #'Birth Year'
    if 'Birth Year' in df :
        earliest_y = df['Birth Year'].min()
        print( earliest_y )
        most_recent_y = df['Birth Year'].max()
        print( most_recent_y )
        most_common_y = df['Birth Year'].mode()[0]
        print( most_common_y )
    else :
        print('There is no column Birth Year in this city data')



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    """ Displaying 5 lines of raw data """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?").lower()
    start_loc = 5
    while (view_data == 'yes'):
        print(df.iloc[0:start_loc])
        start_loc += 5
        view_display = input("Do you wish to continue?: ").lower()
        if view_display.lower() != 'yes':
            break


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)





def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        #print(df.head(5))
        display_data(df)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
