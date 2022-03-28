# Election_Analysis
Election analysis Python work for Module 3

## Overview
In this project we assisted Tom and Seth with an election audit for the Colorado Board of Elections.  We will be using Python to examine a csv list of election data.  Our project will deliver the total number of votes cast in the election, with counts and percentages of the total for each candidate and county in the election.  It will also display the winner and the county placing the greatest amount of votes in the election.

## Election Audit Results

### Methodology
Working with Python 3.7.6 in Virtual Studio Code 1.65.2 allowed us to determine the results of this election.  We first imported the csv and os modules in order to reference the election data and create an output text file.  We then initialized several variables, lists, strings, and dictionaries to store the output from our statements.  After that, we used for loops and if statements to tally votes by candidate and by county.  Once the votes are counted, a winner can be determined with conditionals.  We then use print and write statements to output f strings containing our storage objects to the terminal and output text file, respectively, in order to present the results concisely.

### Results
- There were 369,711 total votes cast in this election
- There were three counties in the election precinct.
  - Jefferson county had 38,855 voters, 10.5% of the total.
  - Denver county had 306,055 voters, 82.8% of the total.
  - Araphoe county had 24,801 voters, 6.7% of the total.
- Denver county had the largest number of votes
- There were three candidates receiving votes in the election.
  - Charles Casper Stockham received 85,213 votes, 23.0% of the total.
  - Diana DeGette received 272,892 votes, 73.8% of the total.
  - Raymon Anthony Doane received 11,606 votes, 3.1% of the total.
- Diana DeGette won the election with 272,892 of the votes cast, which was 73.8% of the total votes.

## Election Audit Summary
This script can be generalized to count votes in other elections as well, so the election commission may choose to reuse it.  If they wished to repurpose it for other elections, they would just need to edit the file_to_load declaration statement to refer to corresponding data for that election.  They would need to have indexed or more specifically-named input and output files so things will be searchable, as otherwise they will just overwrite the election_analysis.txt output each time they run the script.  I recommend adding vote counters within the county for loops so votes for each candidate within each county can be examined as well.  That would help this code be applied to city or county-level elections as well, and it is also useful added detail for results and analysis.  In the same way we used counties in this code, results could be viewed at the district, city, or county level as well depending on the initial data collected.
