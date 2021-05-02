# script performing the border crossing problem

import csv

# address of the csv_file

csv_file = (r'https://raw.githubusercontent.com/gauravsh0812/Border_Crossing_problem/master/border-crossing-analysis-master/insight_testsuite/tests/test_1/input/Border_Crossing_Entry_Data.csv?token=ANTY66BRQPHJSMCI5PNBS3C6JUSVY')

# function for writing list that will be used to produce final csv file

def write_List(date, List, Dict_Canada, Dict_Mexico):
   
    #since here we only have 2 borders-> US-Canada and US_Mexico, hence we have two dictionaires.
    
    dict_list = [Dict_Canada, Dict_Mexico]
    
    for d in dict_list:
        
        if len(d) != 0:
       
            if d == Dict_Canada:
                Border = 'US-Canada Border'
            
            else:
                Border = 'US-Mexico Border'
    
      # seperating keyss and values of the dictionary into seperate list to use them in next step.      
           
            keys_list = []
            values_list = []
        
            for (key, value) in zip(d.keys(), d.values()):
                keys_list.append(key)
                values_list.append(value)
                
     # appending the list as per the dictionaies values.     
     
            for i in range(0, len(d)):
                
                List.append([Border, date, str(keys_list[i]), str(values_list[i][0]), str(round(values_list[i][0]/values_list[i][1]))])
         
    return(List)
    
# writing the results into final csv file    
    
def write_csv(final_list):
    
    with open('solution.csv', mode = 'w') as file:
        
        csv_writer = csv.writer(file, delimiter = ',' )
        
        csv_writer.writerow(['Border', 'Date', 'Measure', 'Value', 'Average'])
        
        for data in final_list:
            csv_writer.writerow([data[0], data[1], data[2], data[3], data[4]])
    
    
# initializing two dictionaries for each borders and `respective empty lists
    
Dict_canada_key_value = {}
Dict_mexico_key_value = {}
        
measure_arr_canada = []
measure_arr_mexico= []


arr = []

#starting date which can be taken from the dataset 

date_1 = '03/01/2019 12:00:00 AM'

# reading csv_file using csv.reader and seperating the different values we will be going to need

with open(csv_file, mode = 'r') as file:
    
    csv_reader = csv.reader(file, delimiter = ',') 
    csv_reader.__next__()
    
    for line in csv_reader:
        
        Border  = line[3]
        date    = line[4]
        measure = line[5]
        value   = line[6]
        n = 1
        
        
    # making an array of unique values of measure as per the border
        
        if Border == 'US-Canada Border':
                
            if (measure not in measure_arr_canada):
                
                measure_arr_canada.append(measure)
                Dict_canada_key_value.update({str(measure) : [int(value), 1]})
                
            else:
                
                 Dict_canada_key_value['{}'.format(measure)][0] += int(value)
                 Dict_canada_key_value['{}'.format(measure)][1] += 1
                 
               
        else:
            
            if (measure not in measure_arr_mexico):
            
                measure_arr_mexico.append(measure)
                Dict_mexico_key_value.update({str(measure) : [int(value), 1]})
              
            else:
                
                 Dict_mexico_key_value['{}'.format(measure)][0] += int(value)
                 Dict_mexico_key_value['{}'.format(measure)][1] += 1      
        
        print(Dict_mexico_key_value)
        print(Dict_canada_key_value)
        print(date, date_1)
        
    # splitting data per month using the change in the date and writing it.
        
        if date_1 != date:
            
            final_list = write_List(date_1, arr, Dict_canada_key_value, Dict_mexico_key_value)
            print(final_list)
            arr = final_list         
            date_1 = date
            Dict_canada_key_value = {}
            Dict_mexico_key_value = {}
        
            measure_arr_canada = []
            measure_arr_mexico= []
        
write_csv(final_list)             
