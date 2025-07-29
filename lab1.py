# Take input 'marks' from the user as a string
marks = input("Enter the Score: ")

# Loop continues until the user types "EXIT"
while marks != "EXIT":
    # Check if the input contains only digits (valid positive integer)
    if marks.isdecimal():
        # Convert to integer and validate score range
        if int(marks) > 100 or int(marks) < 0:
            print("Invalid input")  # Out-of-range scores are invalid
        else:
            # Determine grade based on score thresholds
            if int(marks) >= 90:
                print("A")
            elif int(marks) >= 75:
                print("B")
            elif int(marks) >= 60:
                print("C")
            elif int(marks) >= 40:
                print("D")
            else:
                print("F")
    else:
        # Reject inputs that are not numbers or are negative
        print("Invalid input")
        
    # Prompt for next score or "EXIT" to terminate
    marks = input("Enter the Score: ")

exit()  # End program explicitly
