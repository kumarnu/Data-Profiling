# Data-Profiling
Data Profiling Using Python Script to Find Gap Statistics
Problem Statement: 
A large data set contains over 10 years of price history of 4000+ securities. However, the data set has gaps. Write an efficient Python script to profile the data set to create the gap statistics.

Input File
A Pandas data frame is saved as Python pickle file (filename: px.xz).
It contains the large data set. Two columns are present in the data frame.
•	“dt”: Date
•	“bbgid”: security identifier (composite FIGI)

Requirement
•	Multiple data gaps exist for the same security. We want to detect all of them.
•	We only care about the data gaps between the earliest date and the latest date of a security whose data are present in the given data set.
Each security has its own earliest and latest record date.
o	If a security become publicly traded (i.e., IPO’ed) after the earliest date in the data set, then it is OK for the data to be missing before the IPO (since there are no data prior).
o	If a security is delisted before the latest date in the data set, then it is OK for the data to be missing after the latest available record date of that security.

Expected Output
The reference output has the following columns
•	“start”: start date of a data gap
•	“end”: end date of a data gap
•	“bbgid”: security identifier
•	“length”: number of days of the data gap

The reference output should be sorted by the following fields:
•	Length: descending
•	Bbgid: ascending
•	Start: ascending
•	The output should be an excel sheet.
