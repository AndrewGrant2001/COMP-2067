# Andrew Grant
# 105226219
# Program to calculate Turkey Hunting Tournament stats and rankings based on the highest avg. turkey weight

# try-except block to catch any type errors that may arise from incorrect input file set-ups
try:
    # Defining variables for use throughout the program
    dictionary = []
    numberOfTeams = 5  # this can be changed to however many teams the tournament has (more accurate the faster the run-time)
    array = [[0] * 12 for _ in range(numberOfTeams)]
    x = 0
    y = 0
    errorCode = 0
    arrayList = []
    rank = 1

    # Opening the input file and placing the info into the list
    with open('105226219_Asn3input.txt', 'r') as file1:
        for line in file1:
            line = line.strip("\n")  # removes the \n from string
            if line == "-1":
                break
            else:
                dictionary.append(line)

    # looping through the input info and storing it correctly in a 2d array
    for item in dictionary:
        if y % 4 == 0:
            array[x][0] = item
            y += 1
            if len(array[x][0]) > 10:
                errorCode = 1
                break
        elif y % 4 == 1:
            array[x][1] = int(item)
            y += 1
            if not 0 <= array[x][1] <= 5:
                errorCode = 2
                break
        elif y % 4 == 2:
            item = item.split()
            count = 0
            for i in item:
                if not 0 < float(i) < 100:
                    errorCode = 4
                array[x][2 + count] = round(float(i), 2)
                count += 1
            item = [eval(i) for i in item]
            array[x][7] = round(sum(item), 2)
            array[x][8] = round(max(item), 2)
            array[x][9] = round(min(item), 2)
            array[x][10] = round(sum(item) / len(item), 2)

            if array[x][1] != count:
                errorCode = 3
                break
            y += 1
        else:
            x += 1
            y += 1

    # checking for incorrect input and leads to termination if something is wrong and gives reason why.
    if errorCode == 0:
        # Calculating the rank of each team
        arrayList = [row[10] for row in array]
        arrayList.sort(reverse=True)
        for i in arrayList:
            for j in range(numberOfTeams):
                if i == array[j][10]:
                    array[j][11] = rank
                    rank += 1

        # Creating the outputString to write to the file
        outputString = "Team Name   Count   W1     W2     W3     W4     W5    Total-WT  Heaviest-Tky  Lightest-Tky " \
                       " Av.-WT  T-Rank\n"

        # loop through rows of array to get the information and store in the outputString variable
        for j in range(numberOfTeams):
            if array[j][0] != 0:
                outputString += f"{array[j][0]:^10} {array[j][1]:^7} {array[j][2]:^6} {array[j][3]:^6} {array[j][4]:^6} " \
                                f"{array[j][5]:^6} {array[j][6]:^6} {array[j][7]:^9} {array[j][8]:^13} {array[j][9]:^14}" \
                                f"{array[j][10]:^8} {array[j][11]:^6}\n"
        # print(outputString) - if you want the table printed in the terminal

        # Printing the table to the output file
        f = open("105226219Asn3result.txt", "a")
        f.write(outputString)
        f.close()
    else:
        # Printing the error code so the user can fix the issue
        print(f'''We have received an error code of {errorCode}. Please fix the issue with the information and re-run the program. 
        Error Code - Issue
                 1 - A Team Title exceeds the 10 characters maximum - shorten the Team Title
                 2 - Number of Turkey's does not fall between 0 and 5 (inclusive) - adjust number
                 3 - Number of Turkey's and Number of Weights do not match - ensure same number of Turkey's and Weights
                 4 - The Turkey's Weight is out of the bounds 0 to 100 (exclusive) - ensure weights are correct''')
except:
    print("An Error has occurred. Please ensure the input file is properly organized.")
