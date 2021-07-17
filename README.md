# Python_Activities
I have created this repository to include various applications that I created with Python in an effort to keep my Python skills honed.

# First Activity:
- Rock, Paper, Scissors

## Instructions

* Using the terminal, take an input of `r`, `p` or `s` which will stand for rock, paper, and scissors.

* Have the computer randomly pick one of these three choices.

* Compare the user's input to the computer's choice to determine if the user won, lost, or tied.

# Second Activity:
- Read Netflix

## Instructions

* Prompt the user for what video they are looking for.

* Search through the `netflix_ratings.csv` to find the user's video.

* If the CSV contains the user's video then print out the title, what it is rated and the current user ratings.

  * For example "Pup Star is rated G with a rating of 82"

* If the CSV does not contain the user's video then print out a message telling them that their video could not be found.


# Third Activity

* Analyze the code and CSV provided, looking specifically for what needs to still be added to the application.

* Using the starter code provided, create a function called `print_percentages` which takes in a parameter called `wrestler_data` and does the following:

  * Uses the data stored within `wrestler_data` to calculate the percentage of matches the wrestler won, lost, and drew over the course of a year.

  * Prints out the stats for the wrestler to the terminal.

# Fourth Activity

* This assignment will give you experience creating DataFrames from scratch.

## Instructions

* First, use Pandas to create a DataFrame with the following columns and values:

  * `Character_in_show`: Arnold, Gerald, Helga, Phoebe, Harold, Eugene

  * `color_of_hair`: blonde, black, blonde, black, unknown, red

  * `Height`: average, tallish, tallish, short, tall, short

  * `Football_Shaped_Head`: True, False, False, False, False, False

* You'll note that the above column names are inconsistent and difficult to work with. Rename them to the following, respectively:

  * `Character`, `Hair Color`, `Height`, `Football Head`

* Next, create a new table that contains all of the columns in the following order...

  * `Character`, `Football Head`, `Hair Color`, `Height`
