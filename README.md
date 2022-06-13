# MODULE 3: PyPoll with Python

## Overview of the Analysis
In this module, I will be assisting a Colorado Board of Elections employee, Tom, in an election audit of the tabulated results for a U.S. Congressional precinct in Colorado.  I am tasked with reporting the total number of votes casted, the total number of votes for each candidate, and the winner of the election based on the popular vote. 

This task is usually managed in Excel but Tom’s manager wanted to know if there is a way to successfully automate the process using Python, possibly implementing this code to audit not only other congressional districts but also senatorial districts and local elections. 

### Purpose
* Generate a vote count report to certify this U.S. congressional race.

## Results of the Analysis
1. How many votes were cast in this congressional election? 

369,711 votes were cast in this congressional election

2. Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.

**Table 2.1. County Analysis Breakdown**

| COUNTY | PERCENTAGE OF VOTES | VOTE COUNT
| ----------- | ----------- | -----------
| Denver | 82.8% | 306,055
| Jefferson | 10.5% | 38,855
| Araphaoe | 6.7% | 24,801

3. Which county had the largest number of votes?

Denver county is the county with the largest number of votes, having 306,055 votes, representing 82.2% of the total votes.

4. Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.

**Table 2.2. Candidate Analysis Breakdown**

| CANDIDATE | PERCENTAGE OF VOTES | VOTE COUNT
| ----------- | ----------- | -----------
| Diana DeGette | 73.8% | 272,892
| Charles Casper Stockham | 23.0% | 85,213
| Raymon Anthony Doane | 3.1% | 11,606

5. Which candidate won the election, what was their vote count, and what was their percentage of the total votes? 

Diana DeGette is the winning candidate, having 272,892 votes, representing 73.8% of the total votes

## Summary of the Analysis
As a part of this audit, I would like to assess the possibility of making some changes to the current code in order to make it more suitable for a nation-wide implementation. The first one would be implementing libraries such as Python Pandas as it would help the csv file reading/writing (instead of using the open function) as well as save several lines of code. Second one would be trying to reduce the amount of for loops as my experience as a programmer, specially analyzing Wall Street data with VBA 😜, has taught me that for loops are computationally expensive. For this reason, I would modify the code and implement one for loop instead of two.
