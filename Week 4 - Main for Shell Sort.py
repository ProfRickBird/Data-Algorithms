from ShellSort import ShellSort
from Client import Client
from datetime import date
import time         # use to time the code execution

# display name and date
name = 'Rick Bird'
date = date.today()
print('Name:', name)
print('Date:', date)
print()

#input_file_name = 'ClientData10.csv'
input_file_name = 'ClientData100.csv'

# create a list
clients = []

# read the records from the given file
with open(input_file_name) as infile:
    for line in infile:
        # split the line based on the commas
        s = line.split(',')
        client_id = int( s[0] )
        f_name = s[1]
        l_name = s[2]
        phone = s[3]
        email = s[4]
        # create Client object using the line of data
        clt = Client(client_id, f_name, l_name, phone, email)
        # add the Client object to our list
        clients.append(clt)

# how many client objects do we have?
num_records = len(clients)

# Scenario: Sorting records from the data file
section_title = 'Scenario: Sorting ' + str(num_records) + ' Records'
print(section_title)
print('-' * len(section_title))

# how long does it take to sort the records?
start_time = time.time()

# call the static sort method in the class
ShellSort.sort(clients)

end_time = time.time()
total_time = end_time - start_time
print(f'Seconds to sort {num_records} records: {total_time:.6f}')

# display the sorted list
for clt in clients:
    print(clt)
