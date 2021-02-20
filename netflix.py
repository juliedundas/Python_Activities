#Import modules
import os
import csv

#Prompt the user for what video they are looking for
video = input("Which program are you looking for? ").title() #added .title to capitalize all words in user input

#Set path for csv file
csvpath = os.path.join("Resources", "netflix_ratings.csv")

#Set variable to check if program is on list
exists = False

#Open the csv
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",") #programs separated by commas in csv file

    #Loop through the file to locate the desired program
    for row in csvreader:
        if row[0] == video:
            print(row[0] + " is rated " + row[1] + " with a rating of " + row[5])

            #Set variable to confirm is program is listed
            exists = True

            #Stop running code if one exists so that no duplicates are returned
            break

    #If the video does not exist, notify the requester
    if exists is False:
        print("We do not have what you are requesting. Please try another title.")    