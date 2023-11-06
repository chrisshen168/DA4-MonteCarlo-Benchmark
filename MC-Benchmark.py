#!/usr/bin/env python
# coding: utf-8

# ## Python-SQLite times

# In[1]:


#import libraries
import sqlite3
import pandas as pd
import csv
import time


# In[2]:


#connect to database or create if doesn't exist
sq3_conn = sqlite3.connect('testDBlite.db')


# ### Define the CRUD functions for SQLite

# In[3]:


# Define the CRUD functions
def create_tableLite(sq3_conn, table_name, datatype):
    s = sq3_conn.cursor()
    s.execute(f"DROP TABLE IF EXISTS {table_name}")
    s.execute(f"CREATE TABLE {table_name}(id INTEGER, value {datatype})")
    
def insert_dataLite(sq3_conn, table_name):
    data = pd.read_csv(f"data/{table_name}.csv")
    data.to_sql(f"{table_name}", sq3_conn, if_exists='replace', index=False)

def read_all_recordsLite(sq3_conn, table_name):
    s = sq3_conn.cursor()
    s.execute(f"SELECT * FROM {table_name}")
    for row in s.fetchall():
        pass
    
def print_all_recordsLite(sq3_conn, table_name, n):
    s = sq3_conn.cursor()
    s.execute(f"SELECT * FROM {table_name} ORDER BY id DESC LIMIT {n}")
    for i in s.fetchall():
        print(i)    

def update_recordLite(sq3_conn, table_name, table_name2, datatype):
    s = sq3_conn.cursor()  
    s.execute(f"UPDATE {table_name} SET value = t2.value FROM {table_name2} t2 WHERE {table_name}.id = t2.id")
    sq3_conn.commit()

def delete_all_recordsLite(sq3_conn, table_name):
    s = sq3_conn.cursor()
    s.execute(f"DELETE FROM {table_name}")
    s.execute(f"DROP TABLE IF EXISTS {table_name}")
    sq3_conn.commit()
    


# ### Check the CRUD functions for SQLite

# In[4]:


# Check Create geo
table_name = 'geo02mb01'
table_name2 = 'geo02mb02'
datatype = 'point'
n = 5

create_tableLite(sq3_conn, table_name, datatype)
insert_dataLite(sq3_conn, table_name)
print_all_recordsLite(sq3_conn, table_name, n)


# In[5]:


# Check Update geo
table_name = 'geo02mb01'
table_name2 = 'geo02mb02'
datatype = 'point'
n = 5

create_tableLite(sq3_conn, table_name, datatype)
insert_dataLite(sq3_conn, table_name)
print_all_recordsLite(sq3_conn, table_name, n)

create_tableLite(sq3_conn, table_name2, datatype)
insert_dataLite(sq3_conn, table_name2)
update_recordLite(sq3_conn, table_name, table_name2, datatype)
print_all_recordsLite(sq3_conn, table_name, n)


# In[6]:


# Check Create json
table_name = 'json02mb01'
table_name2 = 'json02mb02'
datatype = 'json'
n = 5

create_tableLite(sq3_conn, table_name, datatype)
insert_dataLite(sq3_conn, table_name)
print_all_recordsLite(sq3_conn, table_name, n)


# In[7]:


# Check Update json
table_name = 'json02mb01'
table_name2 = 'json02mb02'
datatype = 'json'
n = 5

create_tableLite(sq3_conn, table_name, datatype)
insert_dataLite(sq3_conn, table_name)
create_tableLite(sq3_conn, table_name2, datatype)
insert_dataLite(sq3_conn, table_name2)
update_recordLite(sq3_conn, table_name, table_name2, datatype)
print_all_recordsLite(sq3_conn, table_name, n)


# In[8]:


# Check Create/Delete text
table_name = 'text02mb01'
table_name2 = 'text02mb02'
datatype = 'text'
n = 2

create_tableLite(sq3_conn, table_name, datatype)
insert_dataLite(sq3_conn, table_name)
print_all_recordsLite(sq3_conn, table_name, n)
try:
    delete_all_recordsLite(sq3_conn, table_name)
except Exception as e:
    pass
print(f'''Table '{table_name}' does not exist''')


# ### Run CRUD and measure times for SQLite

# In[9]:


# Define the function to run the CRUD operations and measure the time
def run_crud_operationsLite(sq3_conn, table_name, table_name2, datatype, num_cycles):
    # Create empty lists to store the time values
    create_times = []
    read_times = []
    create_times2 = []
    update_times = []
    update_timesO = []
    delete_times = [] 
    total_times = []

    # Perform the CRUD operations for the specified number of cycles
    for i in range(num_cycles):
        # Create the table and insert data from the CSV file
        start_time0 = time.time()
        create_tableLite(sq3_conn, table_name, datatype)
        insert_dataLite(sq3_conn, table_name)
        end_time = time.time()
        create_times.append(end_time - start_time0)

        # Read all records in the table
        start_time = time.time()
        read_all_recordsLite(sq3_conn, table_name)
        end_time = time.time()
        read_times.append(end_time - start_time)

        # Update using data in the CSV file
        start_time1 = time.time()
        create_tableLite(sq3_conn, table_name2, datatype)
        insert_dataLite(sq3_conn, table_name2)
        end_time1 = time.time()
        create_times2.append(end_time1 - start_time1)
        
        start_time2 = time.time()
        update_recordLite(sq3_conn, table_name, table_name2, datatype)
        end_time2 = time.time()
        update_times.append(end_time2 - start_time2)
        
        # Overall update time
        update_timesO.append(end_time2 - start_time1)         

        # Delete all records and the table
        start_time = time.time()
        delete_all_recordsLite(sq3_conn, table_name)
        end_time9 = time.time()
        delete_times.append(end_time9 - start_time)
        
                
        # Overall CRUD time 
        total_times.append(end_time9 - start_time0)

    # Calculate the average time for each operation
    avg_create_time = sum(create_times) / num_cycles
    avg_read_time = sum(read_times) / num_cycles
    avg_update_time = sum(update_times) / num_cycles
    avg_delete_time = sum(delete_times) / num_cycles
    avg_create_time2 = sum(create_times2) / num_cycles
    avg_update_timeO = sum(update_timesO) / num_cycles
    avg_total_time = sum(total_times) / num_cycles
    
    SD_create_time = (sum([((x - avg_create_time) ** 2) for x in create_times])/num_cycles)**0.5
    SD_read_time = (sum([((x - avg_read_time) ** 2) for x in read_times])/num_cycles)**0.5
    SD_update_time = (sum([((x - avg_update_time) ** 2) for x in update_times])/num_cycles)**0.5
    SD_delete_time = (sum([((x - avg_delete_time) ** 2) for x in delete_times])/num_cycles)**0.5
    SD_create_time2 = (sum([((x - avg_create_time2) ** 2) for x in create_times2])/num_cycles)**0.5
    SD_update_timeO = (sum([((x - avg_update_timeO) ** 2) for x in update_timesO])/num_cycles)**0.5
    SD_total_time = (sum([((x - avg_total_time) ** 2) for x in total_times])/num_cycles)**0.5

    # Print the results
    print(f"Average time for {num_cycles} cycles of SQ3_CRUD of {table_name}:")
    print(f"Create time: {avg_create_time:.2f} +/- {SD_create_time:.2f} seconds")
    print(f"Read time: {avg_read_time:.2f} +/- {SD_read_time:.2f} seconds")
    print(f"Update time: {avg_update_time:.2f} +/- {SD_update_time:.2f} seconds")
    print(f"Delete time: {avg_delete_time:.2f} +/- {SD_delete_time:.2f} seconds")
    print(f"Create time2: {avg_create_time2:.2f} +/- {SD_create_time2:.2f} seconds")
    print(f"Update timeO: {avg_update_timeO:.2f} +/- {SD_update_timeO:.2f} seconds")
    print(f"Total time: {avg_total_time:.2f} +/- {SD_total_time:.2f} seconds")
    
    sq3_conn.commit()


# In[10]:


table_name = 'int02mb01'
table_name2 = 'int02mb02'
datatype = 'int'
num_cycles = 100

run_crud_operationsLite(sq3_conn, table_name, table_name2, datatype, num_cycles)


# In[11]:


table_name = 'int04mb01'
table_name2 = 'int04mb02'
datatype = 'int'
num_cycles = 100

run_crud_operationsLite(sq3_conn, table_name, table_name2, datatype, num_cycles)   


# In[12]:


table_name = 'int08mb01'
table_name2 = 'int08mb02'
datatype = 'int'
num_cycles = 100

run_crud_operationsLite(sq3_conn, table_name, table_name2, datatype, num_cycles)  


# In[13]:


table_name = 'int16mb01'
table_name2 = 'int16mb02'
datatype = 'int'
num_cycles = 100

run_crud_operationsLite(sq3_conn, table_name, table_name2, datatype, num_cycles)  


# In[14]:


table_name = 'dec02mb01'
table_name2 = 'dec02mb02'
datatype = 'float'
num_cycles = 100

run_crud_operationsLite(sq3_conn, table_name, table_name2, datatype, num_cycles)


# In[15]:


table_name = 'dec04mb01'
table_name2 = 'dec04mb02'
datatype = 'float'
num_cycles = 100

run_crud_operationsLite(sq3_conn, table_name, table_name2, datatype, num_cycles)


# In[16]:


table_name = 'dec08mb01'
table_name2 = 'dec08mb02'
datatype = 'float'
num_cycles = 100

run_crud_operationsLite(sq3_conn, table_name, table_name2, datatype, num_cycles)


# In[17]:


table_name = 'dec16mb01'
table_name2 = 'dec16mb02'
datatype = 'float'
num_cycles = 100

run_crud_operationsLite(sq3_conn, table_name, table_name2, datatype, num_cycles)


# In[18]:


table_name = 'text02mb01'
table_name2 = 'text02mb02'
datatype = 'text'
num_cycles = 100

run_crud_operationsLite(sq3_conn, table_name, table_name2, datatype, num_cycles)


# In[19]:


table_name = 'text04mb01'
table_name2 = 'text04mb02'
datatype = 'text'
num_cycles = 100

run_crud_operationsLite(sq3_conn, table_name, table_name2, datatype, num_cycles)


# In[20]:


table_name = 'text08mb01'
table_name2 = 'text08mb02'
datatype = 'text'
num_cycles = 100

run_crud_operationsLite(sq3_conn, table_name, table_name2, datatype, num_cycles)


# In[21]:


table_name = 'text16mb01'
table_name2 = 'text16mb02'
datatype = 'text'
num_cycles = 100

run_crud_operationsLite(sq3_conn, table_name, table_name2, datatype, num_cycles)


# In[22]:


table_name = 'json02mb01'
table_name2 = 'json02mb02'
datatype = 'json'
num_cycles = 2

run_crud_operationsLite(sq3_conn, table_name, table_name2, datatype, num_cycles)


# In[23]:


table_name = 'json04mb01'
table_name2 = 'json04mb02'
datatype = 'json'
num_cycles = 100

run_crud_operationsLite(sq3_conn, table_name, table_name2, datatype, num_cycles)


# In[14]:


table_name = 'json08mb01'
table_name2 = 'json08mb02'
datatype = 'json'
num_cycles = 100

run_crud_operationsLite(sq3_conn, table_name, table_name2, datatype, num_cycles)


# In[25]:


table_name = 'json16mb01'
table_name2 = 'json16mb02'
datatype = 'json'
num_cycles = 100

run_crud_operationsLite(sq3_conn, table_name, table_name2, datatype, num_cycles)


# In[26]:


table_name = 'geo02mb01'
table_name2 = 'geo02mb02'
datatype = 'point'
num_cycles = 100

run_crud_operationsLite(sq3_conn, table_name, table_name2, datatype, num_cycles)


# In[27]:


table_name = 'geo04mb01'
table_name2 = 'geo04mb02'
datatype = 'point'
num_cycles = 100

run_crud_operationsLite(sq3_conn, table_name, table_name2, datatype, num_cycles)


# In[28]:


table_name = 'geo08mb01'
table_name2 = 'geo08mb02'
datatype = 'point'
num_cycles = 100

run_crud_operationsLite(sq3_conn, table_name, table_name2, datatype, num_cycles)


# In[29]:


table_name = 'geo16mb01'
table_name2 = 'geo16mb02'
datatype = 'point'
num_cycles = 100

run_crud_operationsLite(sq3_conn, table_name, table_name2, datatype, num_cycles)

