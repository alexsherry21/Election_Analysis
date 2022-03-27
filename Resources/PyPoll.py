# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote


#Import dependencies and assign a variable for the file to load and the path
import csv
import os

#Assign a variable to load the file from a path
file_to_load = os.path.join("Resources", "election_results.csv")

#Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("Analysis", "election_analysis.txt")

#Open the election results and read the file
with open(file_to_load) as election_data:

#Read the file object with the reader function
    file_reader = csv.reader(election_data)
    
    # Read and print the header row
    headers = next(file_reader)
    print(headers)


#Use the Open statement to open the file as a text file
with open(file_to_save, "w") as txt_file:

#Write some data to the file
    txt_file.write("Araphoe\nDenver\nJefferson")

