# Initial variable to track game play
user_play = "y"
start_number = 0
# While we are still playing...
while user_play == "y":

    # Ask the user how many numbers to loop through
    total_numbers = int(input("How many numbers would you like to loop through?: "))
    # Loop through the numbers. (Be sure to cast the string into an integer.)
    for n in range(start_number, total_numbers + start_number):

        # Print each number in the range
       print(n)

    start_number = total_numbers + start_number

    # Once complete...
    user_play = input("Continue: (y)es or (n)o? ")