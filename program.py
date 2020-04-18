#load modules
import pandas as pd
import time
from datetime import date
from datetime import timedelta


#Variable Declarations
count = 0
gap = 0
#Lists to store required attributes
start_date_list =[]
end_date_list =[]
gap_list =[]
bbgid_list = []
#Dictionary to hold output values
Dict = {}       
start_date = None
end_date = None

#log start time
start_time = time.time()
#load input data set
data = pd.read_pickle(r'/Users/nitish/Documents/Interviews/ConnectiveCapital/Project/px.xz')
#Dropping duplicates if any(Data Filter)
data.drop_duplicates(inplace=True)  #Keep the first row if duplicate found
rows = len(data.index) # Finding total number of rows

for row in range(rows):
    count = count + 1 # For skipping the first entry
    if(count > 1):
        gap = (data['dt'].values[row] - prev_date).days - 1
        start_date = prev_date + timedelta(1)
        end_date = data['dt'].values[row] - timedelta(1)
        end_date_list.append(end_date)
        start_date_list.append(start_date)
        gap_list.append(gap)
        bbgid_list.append(data['bbgid'].values[row])       
    prev_date = data['dt'].values[row]
        
#Appending values to the keys        
Dict['start'] = start_date_list
Dict['end'] = end_date_list
Dict['Length'] = gap_list 
Dict['bbgid'] = bbgid_list

#Converting dictionary to output dataframe
output = pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in Dict.items()]))
#Sorting DataFrame by Length: descending
#                     Bbgid: ascending
#                     Start: ascending
output = output.sort_values(by=['Length','bbgid','start'],ascending = [False,True,True])#Sorting data frame
#Restricting Output values to first 1000 records
output.iloc[0:1000].to_excel(r'/Users/nitish/Documents/Interviews/ConnectiveCapital/Project/px_stats2.xlsx', index=False)
# Printing execution time
print("--- %s seconds ---" % (time.time() - start_time))


