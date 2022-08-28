>**Note**: Please **fork** the current Udacity repository so that you will have a **remote** repository in **your** Github account. Clone the remote repository to your local machine. Later, as a part of the project "Post your Work on Github", you will push your proposed changes to the remote repository in your Github account.

### Date created
Original creation date: 08/07/2022
Updated: 08/28/2022

### Project Title
bikeshare python project

### Description
The program interacts with the user with the command line to provide bikeshare
statistics for data for a given city (Chicago, NY, and Washington) provided by
an input file in csv format. The script takes the raw input to create an
interactive experience in the terminal to present these statistics.

In this project, uses data provided by Motivate, a bike share system provider
for many major cities in the United States, to uncover bike share usage
patterns. You will compare the system usage between three large cities:
Chicago, New York City, and Washington, DC.

**You should have Python 3, NumPy, and pandas installed using Anaconda**

#### Command Line
bikeshare.py

### Files Used
input files: chicago.csv, new_york_city.csv, and washington.csv
Randomly selected data for the first six months of 2017 are provided for all
three cities. All three of the data files contain the same core six (6) columns:
* Start Time (e.g., 2017-01-01 00:07:57)
* End Time (e.g., 2017-01-01 00:20:53)
* Trip Duration (in seconds - e.g., 776)
* Start Station (e.g., Broadway & Barry Ave)
* End Station (e.g., Sedgwick St & North Ave)
* User Type (Subscriber or Customer)
The Chicago and New York City files also have the following two columns:
* Gender
* Birth Year

### Statistics Computed
1. Popular times of travel (i.e., occurs most often in the start time)
* most common month
* most common day of week
* most common hour of day
2. Popular stations and trip
* most common start station
* most common end station
* most common trip from start to end (i.e., most frequent combination of start station and end station)
3. Trip duration
* total travel time
* average travel time
4. User info
* counts of each user type
* counts of each gender (only available for NYC and Chicago)
* earliest, most recent, most common year of birth (only available for NYC and Chicago)

### Credits
https://pandas.pydata.org/pandas-docs/stable/reference/frame.html
https://numpy.org/devdocs/user/index.html
