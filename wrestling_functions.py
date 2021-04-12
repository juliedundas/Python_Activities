import os
import csv

# Path to collect data from the Resources folder
wrestling_csv = os.path.join('.', 'Resources', 'WWE-Data-2016.csv')

# Set variable to see if wrestler exists

exists = False

# Define the function and have it accept the 'wrestlerData' as its sole parameter
def show_percentages(wrestler_data):
    #Print various statistics
    wrestler_name = str(wrestler_data[0])
    wins = int(wrestler_data[1])
    losses = int(wrestler_data[2])
    draws = int(wrestler_data[3])

    exists = True

# Find the total number of matches wrestled
    total_matches = wins + losses + draws

    #print(f"The total number of matches wrestled is {total_matches}")

# Find the percentage of matches won
    win_percentage = round((wins / total_matches) * 100,2)

# Find the percentage of matches lost
    loss_percentage = round((losses / total_matches) * 100,2)

# Find the percentage of matches drawn
    draw_percentage = round((draws / total_matches) * 100,2)

# If the loss percentage is over 50, type_of_wrestler is "Jobber". Otherwise it is "Superstar".
    if loss_percentage > 50:
        type_of_wrestler = "Jobber"
    else:
        type_of_wrestler = 'Superstar'

# Print out the wrestler's name and their percentage stats
    print(f"Stats for {wrestler_name}:")
    print(f"Win Percent for {wrestler_name}: {str(win_percentage)}%")
    print(f"Loss Percent for {wrestler_name}: {str(loss_percentage)}%")
    print(f"Draw Percent for {wrestler_name}: {str(draw_percentage)}%")
    print(f"{wrestler_name} is a {type_of_wrestler}")

# Read in the CSV file
with open(wrestling_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Set variable to check if we found the wrestler
    exists = False

    # Prompt the user for what wrestler they would like to search for
    name_to_check = input("What wrestler do you want to look for? ").title()

    # Loop through the data
    for row in csvreader:

        # Set variable for wrestler name
        name = row[0]

        # If the wrestler's name in a row is equal to that which the user input, run the 'show_percentages()' function
        if(name_to_check == name):
            show_percentages(row)      

        # Set variable to confirm we have found the wrestler
        exists = True

if exists is False:
    print(f"Sorry, that name is not in our directory. Please choose another wrestler.")  
 