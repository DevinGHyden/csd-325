# Name: Devin G. Hyden
# Date: 03 July 2026
# Assignment: hyden_assignment4_2
# Purpose: Show graphs for low and high temperatures in Sitka

import csv
import sys
from datetime import datetime
from matplotlib import pyplot as plt

# Define the source files containing the weather dataset
filename = 'sitka_weather_2018_simple.csv'


def load_weather_data():
    # Create empty lists to store parsed data columns
    dates, highs, lows = [], [], []
    # Opens the file safely
    with open(filename) as f:
        reader = csv.reader(f)
        # Reads and skips the header row
        header_row = next(reader)
        # Loop through data rows in the weather file
        for row in reader:
            # Extract and convert the data string into a datetime object
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            # Extract and convert temperature strings to integers
            high = int(row[5])
            low = int(row[6])
            # Append processed values to their respective lists
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
    # Return the data arrays to the calling function
    return dates, highs, lows


# Prints starting text menu
def show_menu():
    print('\nSitka Weather Menu')
    print('Type Highs to view daily high temperatures.')
    print('Type Lows to view daily low temperatures.')
    print('Type Exit to close program.')


def plot_temperature(dates, temperatures, graph_color, title):
    # Create a figure object and a single subplot axis
    fig, ax = plt.subplots()
    # Plot the line graph with the chosen dataset and line color
    ax.plot(dates, temperatures, c=graph_color)
    # Set the main graph title and its text sizing
    plt.title(title, fontsize=24)
    # Configure x-axis layout
    plt.xlabel('', fontsize=16)
    # Automatically tilt the date labels diagonally for no overlap on the x-axis
    fig.autofmt_xdate()
    # Label the y-axis
    plt.ylabel('Temperature (F)', fontsize=16)
    # Increase the text sizing of the tick markers for both axes for legibility
    plt.tick_params(axis='both', which='major', labelsize=16)
    # Show the interactive graphical plotting window
    plt.show()


def main():
    # Load all processed lists
    dates, highs, lows = load_weather_data()
    # Start infinite loop to keep program interactive until exit is input
    while True:
        show_menu()
        # Capture input, strip tailing whitespaces, and lowercase it for input validation
        choice = input('Enter Highs, Lows, or Exit: ').strip().lower()
        # Option based on the user selection
        if choice == 'highs':
            plot_temperature(
                dates,
                highs,
                'red',
                'Daily high temperatures - 2018',
            )
        elif choice == 'lows':
            plot_temperature(
                dates,
                lows,
                'blue',
                'Daily low temperatures - 2018',
            )
        elif choice == 'exit':
            print('Thank you for using the Sitka Weather program, Goodbye!')
            # Terminate the program
            sys.exit()
        else:
            # Catch-all for invalid inputs
            print('Invalid choice. Please type Highs, Lows, or Exit.')


if __name__ == '__main__':
    main()
